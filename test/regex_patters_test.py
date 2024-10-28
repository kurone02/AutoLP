import pytest

from ..regex_patterns import CODE_PATTERN

def test_CODE_PATTERN():
    markdown = """Lorem ipsum
```python
print('foo```bar```foo')
```
Lorem ipsum
```python
print("hello words`0`")
print("hello words`1`")
```
Lorem ipsum
```
print('foo```bar```foo')
print("hello words`2`")
```
"""

    expected = [
        "print('foo```bar```foo')\n",
        "print(\"hello words`0`\")\nprint(\"hello words`1`\")\n",
        "print('foo```bar```foo')\nprint(\"hello words`2`\")\n",
    ]

    matches = CODE_PATTERN.finditer(markdown)

    matches = list(matches)

    assert len(expected) == len(list(matches))

    for i, match in enumerate(matches):
        assert len(match.groups()) == 1
        assert match.group(1) == expected[i]

    markdown = """=============== Trial 1. ===============
 ### Summary of the Problem
Candice is playing a curling game where she throws stones from position 0, and each stone travels a certain distance based on the energy with which it is thrown. Stones can collide, and the energy of a stone is reduced by 1 with each unit of movement until it stops or collides with another stone. The goal is to determine which stone ends up closest to the target position \\(G\\) and how far away it is.

### Key Details of the Problem
1. **Number of Stones (N)**: Each test case has a specific number of stones.
2. **Energy of Stones (E_i)**: Each stone is thrown with a specific energy.
3. **Target Position (G)**: The goal position to which the stones are aimed.
4. **No Collisions**: No two stones are thrown with the same energy.
5. **Constraints**: The total number of stones across all test cases is at most 2,000,000.

### Step-by-Step Plan to Solve the Problem
1. **Simulate the Movement of Stones**: For each stone, simulate its movement until it stops or collides with another stone.
2. **Track the Position of Stones**: Keep track of the position of each stone after it stops moving.
3. **Determine the Closest Stone to the Goal**: After all stones have stopped, determine which stone is closest to the goal and how far away it is.

### Pseudocode
1. **Input Reading**: Read the number of test cases \\(T\\), and for each test case, read \\(N\\) and \\(G\\).
2. **Stone Positions Calculation**:
   - For each stone, simulate its movement until it stops.
   - Track the position of each stone after it stops.
3. **Determine the Closest Stone**:
   - For each test case, find the stone closest to the goal and calculate the distance.
4. **Output the Result**: For each test case, output the index of the stone closest to the goal and the distance.

### C++ Code
Here is the C++ code implementing the above algorithm:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

void solve() {
    int N, G;
    cin >> N >> G;
    vector<int> stones(N);
    for (int i = 0; i < N; ++i) {
        cin >> stones[i];
    }

    vector<int> positions(N);
    for (int i = 0; i < N; ++i) {
        int energy = stones[i];
        int pos = 0;
        while (energy > 0) {
            if (pos < N && stones[pos] == energy) {
                energy = 0;
            } else {
                pos++;
                energy--;
            }
        }
        positions[i] = pos;
    }

    int closest_stone = 0;
    int min_distance = numeric_limits<int>::max();
    for (int i = 0; i < N; ++i) {
        int distance = abs(positions[i] - G);
        if (distance < min_distance || (distance == min_distance && positions[i] < positions[closest_stone])) {
            closest_stone = i + 1;
            min_distance = distance;
        }
    }

    cout << "Case #" << case_num << ": " << closest_stone << " " << min_distance << endl;
}

int main() {
    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        solve();
    }
    return 0;
}
```

This code reads the input, simulates the movement of each stone, and determines the closest stone to the goal position \\(G\\). It then outputs the result for each test case.
"""

    expected_code = """#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

void solve() {
    int N, G;
    cin >> N >> G;
    vector<int> stones(N);
    for (int i = 0; i < N; ++i) {
        cin >> stones[i];
    }

    vector<int> positions(N);
    for (int i = 0; i < N; ++i) {
        int energy = stones[i];
        int pos = 0;
        while (energy > 0) {
            if (pos < N && stones[pos] == energy) {
                energy = 0;
            } else {
                pos++;
                energy--;
            }
        }
        positions[i] = pos;
    }

    int closest_stone = 0;
    int min_distance = numeric_limits<int>::max();
    for (int i = 0; i < N; ++i) {
        int distance = abs(positions[i] - G);
        if (distance < min_distance || (distance == min_distance && positions[i] < positions[closest_stone])) {
            closest_stone = i + 1;
            min_distance = distance;
        }
    }

    cout << "Case #" << case_num << ": " << closest_stone << " " << min_distance << endl;
}

int main() {
    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        solve();
    }
    return 0;
}
"""

    matches = CODE_PATTERN.finditer(markdown)

    matches = list(matches)

    assert len(matches) == 1

    match = matches[0]

    assert len(match.groups()) == 1
    assert match.group(1) == expected_code