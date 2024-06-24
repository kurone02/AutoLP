from utils import read_json, read_txt, save_json, ensemble
import math
from tqdm import tqdm

SUBMISSION_LIST = [
    # Put output files here
]


SAVE_FILE = "ensemble_strategy/ensemble_30.json"


if __name__ == "__main__":
    submissions = [(read_json(file), weight) for file, weight in SUBMISSION_LIST]

    format, _ = submissions[0]

    num_question = len(submissions[0][0])

    for i in tqdm(range(num_question)):
        answer_list: list[tuple[float]] = []
        num_answer = 0
        for submission, weight in submissions:
            submission = submission[i]
            answer = list(map(lambda x: float(x), submission["results"].values()))
            num_answer = len(answer)
            is_error = True
            for ans in answer:
                if not math.isclose(ans, 0, abs_tol=1e-6):
                    is_error = False
                    break
            is_neg = False
            for ans in answer:
                if ans < 0:
                    is_neg = True
                    break
            if is_error or is_neg:
                continue
            # print(i, answer, weight)
            answer_list.extend([tuple(answer) for _ in range(weight)])
        
        if len(answer_list) == 0:
            final_answer = [0 for i in range(num_answer)]
        else:
            final_answer = ensemble(answer_list)

        for key, val in zip(format[i]["results"].keys(), final_answer):
            format[i]["results"][key] = str(val)

save_json(SAVE_FILE, format)