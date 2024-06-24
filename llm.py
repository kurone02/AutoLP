from __future__ import annotations
import transformers
from transformers import AutoTokenizer, TextStreamer, AutoTokenizer, PreTrainedTokenizer, PreTrainedTokenizerFast
from vllm import LLM, SamplingParams
import torch
import typing
from typing import Callable, List, Optional, Union
import os
import ollama
from typing import Any, Iterator, Mapping, Optional

class MessageContent(typing.TypedDict):
    role: str
    content: str

class Message():
    
    def __init__(self, system_prompt: str="", message: list[MessageContent]=[]) -> None:
        self._message: list[MessageContent] = message.copy()
        self._system_prompt = system_prompt
        self.change_system_prompt(system_prompt=system_prompt)
        
    def change_system_prompt(self, system_prompt: str="") -> None:
        self._system_prompt = system_prompt
        if len(self._message) == 0:
            self._message.append(MessageContent())
        self._message[0] = {
            "role": "system",
            "content": system_prompt,
        }
        
    def get_all_messages(self) -> Message:
        return self._message.copy()

    def copy_all_messages(self) -> Message:
        return Message(system_prompt=self._system_prompt, message=self._message)
    
    def _append_message(self, role: str, content: str) -> None:
        if role not in ["user", "assistant"]:
            raise ValueError("The role must be either user or assistant")
        
        if self._message[-1]["role"] == role:
            raise ValueError("The roles must alternate between user/assistant")
        
        self._message.append(MessageContent(
            role=role,
            content=content,
        ))
        
    def append_user_message(self, content: str) -> None:
        self._append_message(
            role="user",
            content=content,
        )
    
    def append_assistant_message(self, content: str) -> None:
        self._append_message(
            role="assistant",
            content=content,
        )
        
    def clear_history(self) -> None:
        self._message = [self._message[0]]


class BaseLLM():

    def __init__(self, model_id: str, device: str="0") -> None:
        self._device: str = device
        self._model_id: str = model_id
        
        os.environ["CUDA_VISIBLE_DEVICES"] = device

        # self._tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = AutoTokenizer.from_pretrained(self._model_id)

        # self._terminators = [
        #     self._tokenizer.eos_token_id,
        #     self._tokenizer.convert_tokens_to_ids("<|eot_id|>")
        # ]
        
        # self._streamer: TextStreamer = TextStreamer(self._tokenizer, skip_prompt=True)
        
        # self._llm: transformers.Pipeline = transformers.pipeline(
        #     "text-generation",
        #     model=model_id,
        #     model_kwargs={"torch_dtype": torch.bfloat16},
        #     device=self._device,
        #     tokenizer=self._tokenizer,
        #     trust_remote_code=True,
        # )

        self._llm: LLM = LLM(model_id, trust_remote_code=True)
        self._tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = self._llm.get_tokenizer()

    def get_response(self, 
                     prompts: list[str], 
                     max_new_tokens=4096, 
                     temperature=0.6, 
                     top_p=0.9, 
                     stop_criteria: list[str] | None=None, 
                     min_tokens: int=None,
                     num_return_sequences=1, 
                     processor: Callable[[List[int], torch.Tensor], torch.Tensor] | None=None,
                    ) -> list[list[str]]:
        kwargs = {
            "n": num_return_sequences, 
            "max_tokens": max_new_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stop": stop_criteria,
            # "use_beam_search": num_return_sequences > 1,
        }
        if processor is not None:
            kwargs["logits_processors"] = [processor]
        if temperature == 0:
            kwargs["temperature"] = 0
            if "top_p" in kwargs:
                del kwargs["top_p"]
                
        if min_tokens is not None:
            kwargs["min_tokens"] = min_tokens

        sampling_params = SamplingParams(**kwargs)

        outputs = self._llm.generate(prompts, 
                                     use_tqdm=False, 
                                     sampling_params=sampling_params,
                                    )

        results = [
            [o.text for o in out.outputs] for out in outputs
        ]
        return results

        

class ChatBotLLM(BaseLLM):
    
    def __init__(self, model_id: str="meta-llama/Meta-Llama-3-8B-Instruct", device: str="cuda", system_prompt: str="") -> None:
        super().__init__(model_id, device)
        self._system_prompt: str = system_prompt
        self._messages: Message = Message(system_prompt=system_prompt)
        
    def update_system_prompt(self, prompt: str="") -> None:
        self._messages.change_system_prompt(prompt)
        
    def clear_chat_history(self) -> None:
        self._messages.clear_history()

    def _add_message(self, role: str, content: str) -> None:
        if role == "assistant":
            self._messages.append_assistant_message(content)
        else:
            self._messages.append_user_message(content)

    def add_user_message(self, prompt: str):
        self._add_message("user", prompt)

    def add_assistant_message(self, prompt: str):
        self._add_message("assistant", prompt)
        
    def chat(self, 
             prompt: str, 
             max_new_tokens=4096, 
             temperature=0.6, 
             top_p=0.9, 
             stop_criteria: transformers.StoppingCriteria | None=None, 
             verbose: bool=False, 
             harmful=False
            ) -> str:
        messages = self._messages.copy_all_messages()
        messages.append_user_message(prompt)
        chat_history = self._tokenizer.apply_chat_template(
                messages.get_all_messages(), 
                tokenize=False, 
                add_generation_prompt=True,
        )

        if harmful:
            chat_history += "Step 1.) "

        outputs = self.get_response([chat_history], max_new_tokens, temperature, top_p, stop_criteria, 1)

        result = outputs[0][0]

        self._messages.append_user_message(prompt)
        self._messages.append_assistant_message(result)
        
        return result
    
class DeepSeekChatLLM(ChatBotLLM):
    def __init__(self, model_id: str="deepseek-ai/deepseek-coder-33b-instruct", device: str="cuda", system_prompt: str="") -> None:
        self._device: str = device
        self._model_id: str = model_id

        # os.environ["CUDA_VISIBLE_DEVICES"] = device

        self._llm: LLM = LLM(model_id, trust_remote_code=True, tensor_parallel_size=8)
        self._tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast = self._llm.get_tokenizer()

        self._system_prompt: str = system_prompt
        self._messages: Message = Message(system_prompt=system_prompt)
    
    
class OllamaLLM():
    def __init__(self, model: str="", system_prompt: str="") -> None:
        self.model: str = model
        self._messages: Message = Message(system_prompt=system_prompt)

    def update_system_prompt(self, prompt: str="") -> None:
        self._messages.change_system_prompt(prompt)
        
    def clear_chat_history(self) -> None:
        self._messages.clear_history()

    def _add_message(self, role: str, content: str) -> None:
        if role == "assistant":
            self._messages.append_assistant_message(content)
        else:
            self._messages.append_user_message(content)

    def add_user_message(self, prompt: str):
        self._add_message("user", prompt)

    def add_assistant_message(self, prompt: str):
        self._add_message("assistant", prompt)

    def get_response(self, options: Optional[dict[str, Any]]=None, stream: bool=False) -> (Mapping[str, Any] | Iterator[Mapping[str, Any]]):
        messages = self._messages.copy_all_messages()
        response = ollama.chat(model=self.model, messages=messages.get_all_messages(), options=options, stream=stream)
        return response