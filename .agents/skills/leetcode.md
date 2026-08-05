---
name: leetcode
description: Scaffolds a LeetCode problem solution template and comprehensive pytest file (10+ test cases) in category folders based on tags.
---

# LeetCode Problem Scaffolder

When the user enters a LeetCode problem number, name, or URL:

## 🚫 STRICT NEGATIVE CONSTRAINTS (CRITICAL)
- **DO NOT WRITE THE SOLUTION LOGIC.**
- **DO NOT INFER OR GENERATE CODE INSIDE THE METHOD BODY.**
- The method body MUST ONLY contain `pass` or a docstring followed by `pass`.
- Your goal is strictly scaffolding structure and tests so the user can solve it themselves.

---

## Workflow Steps

### 1. Categorize & Map Folder
- Identify primary data structure/algorithm tag (e.g., `arrays`, `strings`, `two_pointers`, `trees`, `dynamic_programming`, `graphs`, `linked_lists`).
- Use lowercase `snake_case` folder names (`problems/<tag>/` and `tests/<tag>/`).

### 2. Generate Problem File (`problems/<tag>/<problem_name_snake_case>.py`)
- Standard typing imports (`from typing import List, Optional, Dict, Tuple, Any`).
- `class Solution:` definition.
- Exact LeetCode method signature and return type annotation.
- Docstring (if specified by LeetCode).
- Body MUST strictly be `pass`.

*Example Output (`problems/arrays/contains_duplicate.py`):*
```python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass