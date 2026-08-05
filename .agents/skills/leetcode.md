---
name: leetcode
description: Scaffolds LeetCode Top Interview 150 problems or specific problem numbers/names with empty solution templates and 10+ pytest test cases.
---

# LeetCode Top Interview 150 Scaffolder

When the user runs `/leetcode` followed by `next`, a problem number, a problem name, or a LeetCode URL:

## 🚫 STRICT NEGATIVE CONSTRAINTS (CRITICAL)
- **DO NOT WRITE THE SOLUTION LOGIC.**
- **DO NOT INFER OR GENERATE CODE INSIDE THE METHOD BODY.**
- The method body MUST ONLY contain `pass` or a docstring followed by `pass`.
- Your goal is strictly scaffolding structure and tests so the user can solve it themselves.

---

## 📋 Top Interview 150 Ordered Problem List

1. 88. Merge Sorted Array (Array / String)
2. 27. Remove Element (Array / String)
3. 26. Remove Duplicates from Sorted Array (Array / String)
4. 80. Remove Duplicates from Sorted Array II (Array / String)
5. 169. Majority Element (Array / String)
6. 189. Rotate Array (Array / String)
7. 121. Best Time to Buy and Sell Stock (Array / String)
8. 122. Best Time to Buy and Sell Stock II (Array / String)
9. 55. Jump Game (Array / String)
10. 45. Jump Game II (Array / String)
11. 274. H-Index (Array / String)
12. 380. Insert Delete GetRandom O(1) (Array / String)
13. 238. Product of Array Except Self (Array / String)
14. 134. Gas Station (Array / String)
15. 135. Candy (Array / String)
16. 42. Trapping Rain Water (Array / String)
17. 13. Roman to Integer (Array / String)
18. 12. Integer to Roman (Array / String)
19. 58. Length of Last Word (Array / String)
20. 14. Longest Common Prefix (Array / String)
21. 151. Reverse Words in a String (Array / String)
22. 6. Zigzag Conversion (Array / String)
23. 28. Find the Index of the First Occurrence in a String (Array / String)
24. 68. Text Justification (Array / String)
25. 125. Valid Palindrome (Two Pointers)
26. 392. Is Subsequence (Two Pointers)
27. 167. Two Sum II - Input Array Is Sorted (Two Pointers)
28. 11. Container With Most Water (Two Pointers)
29. 15. 3Sum (Two Pointers)
30. 209. Minimum Size Subarray Sum (Sliding Window)
31. 3. Longest Substring Without Repeating Characters (Sliding Window)
32. 30. Substring with Concatenation of All Words (Sliding Window)
33. 76. Minimum Window Substring (Sliding Window)
34. 36. Valid Sudoku (Matrix)
35. 54. Spiral Matrix (Matrix)
36. 48. Rotate Image (Matrix)
37. 73. Set Matrix Zeroes (Matrix)
38. 289. Game of Life (Matrix)
39. 383. Ransom Note (Hashmap)
40. 205. Isomorphic Strings (Hashmap)
41. 290. Word Pattern (Hashmap)
42. 242. Valid Anagram (Hashmap)
43. 49. Group Anagrams (Hashmap)
44. 1. Two Sum (Hashmap)
45. 202. Happy Number (Hashmap)
46. 219. Contains Duplicate II (Hashmap)
47. 128. Longest Consecutive Sequence (Hashmap)
48. 228. Summary Ranges (Intervals)
49. 56. Merge Intervals (Intervals)
50. 57. Insert Interval (Intervals)
51. 452. Minimum Number of Arrows to Burst Balloons (Intervals)
52. 20. Valid Parentheses (Stack)
53. 71. Simplify Path (Stack)
54. 155. Min Stack (Stack)
55. 150. Evaluate Reverse Polish Notation (Stack)
56. 224. Basic Calculator (Stack)
57. 141. Linked List Cycle (Linked List)
58. 2. Add Two Numbers (Linked List)
59. 21. Merge Two Sorted Lists (Linked List)
60. 138. Copy List with Random Pointer (Linked List)
61. 92. Reverse Linked List II (Linked List)
62. 25. Reverse Nodes in k-Group (Linked List)
63. 19. Remove Nth Node From End of List (Linked List)
64. 82. Remove Duplicates from Sorted List II (Linked List)
65. 61. Rotate List (Linked List)
66. 86. Partition List (Linked List)
67. 146. LRU Cache (Linked List)
68. 104. Maximum Depth of Binary Tree (Binary Tree General)
69. 100. Same Tree (Binary Tree General)
70. 226. Invert Binary Tree (Binary Tree General)
71. 101. Symmetric Tree (Binary Tree General)
72. 105. Construct Binary Tree from Preorder and Inorder Traversal (Binary Tree General)
73. 106. Construct Binary Tree from Inorder and Postorder Traversal (Binary Tree General)
74. 117. Populating Next Right Pointers in Each Node II (Binary Tree General)
75. 114. Flatten Binary Tree to Linked List (Binary Tree General)
76. 112. Path Sum (Binary Tree General)
77. 129. Sum Root to Leaf Numbers (Binary Tree General)
78. 124. Binary Tree Maximum Path Sum (Binary Tree General)
79. 173. Binary Search Tree Iterator (Binary Tree General)
80. 222. Count Complete Tree Nodes (Binary Tree General)
81. 236. Lowest Common Ancestor of a Binary Tree (Binary Tree General)
82. 199. Binary Tree Right Side View (Binary Tree BFS)
83. 637. Average of Levels in Binary Tree (Binary Tree BFS)
84. 102. Binary Tree Level Order Traversal (Binary Tree BFS)
85. 103. Binary Tree Zigzag Level Order Traversal (Binary Tree BFS)
86. 530. Minimum Absolute Difference in BST (Binary Search Tree)
87. 230. Kth Smallest Element in a BST (Binary Search Tree)
88. 98. Validate Binary Search Tree (Binary Search Tree)
89. 200. Number of Islands (Graph General)
90. 130. Surrounded Regions (Graph General)
91. 133. Clone Graph (Graph General)
92. 399. Evaluate Division (Graph General)
93. 207. Course Schedule (Graph General)
94. 210. Course Schedule II (Graph General)
95. 127. Word Ladder (Graph BFS)
96. 433. Minimum Genetic Mutation (Graph BFS)
97. 208. Implement Trie (Prefix Tree) (Trie)
98. 211. Design Add and Search Words Data Structure (Trie)
99. 212. Word Search II (Trie)
100. 17. Letter Combinations of a Phone Number (Backtracking)
101. 77. Combinations (Backtracking)
102. 46. Permutations (Backtracking)
103. 39. Combination Sum (Backtracking)
104. 52. N-Queens II (Backtracking)
105. 79. Word Search (Backtracking)
106. 108. Convert Sorted Array to Binary Search Tree (Divide & Conquer)
107. 148. Sort List (Divide & Conquer)
108. 427. Construct Quad Tree (Divide & Conquer)
109. 23. Merge k Sorted Lists (Divide & Conquer)
110. 53. Maximum Subarray (Kadane's Algorithm)
111. 918. Maximum Sum Circular Subarray (Kadane's Algorithm)
112. 35. Search Insert Position (Binary Search)
113. 74. Search a 2D Matrix (Binary Search)
114. 162. Find Peak Element (Binary Search)
115. 33. Search in Rotated Sorted Array (Binary Search)
116. 34. Find First and Last Position of Element in Sorted Array (Binary Search)
117. 153. Find Minimum in Rotated Sorted Array (Binary Search)
118. 4. Median of Two Sorted Arrays (Binary Search)
119. 215. Kth Largest Element in an Array (Heap)
120. 295. Find Median from Data Stream (Heap)
121. 373. Find K Pairs with Smallest Sums (Heap)
122. 502. IPO (Heap)
123. 190. Reverse Bits (Bit Manipulation)
124. 191. Number of 1 Bits (Bit Manipulation)
125. 136. Single Number (Bit Manipulation)
126. 137. Single Number II (Bit Manipulation)
127. 201. Bitwise AND of Numbers Range (Bit Manipulation)
128. 9. Palindrome Number (Math)
129. 66. Plus One (Math)
130. 172. Factorial Trailing Zeroes (Math)
131. 69. Sqrt(x) (Math)
132. 50. Pow(x, n) (Math)
133. 149. Max Points on a Line (Math)
134. 70. Climbing Stairs (1D DP)
135. 198. House Robber (1D DP)
136. 139. Word Break (1D DP)
137. 322. Coin Change (1D DP)
138. 300. Longest Increasing Subsequence (1D DP)
139. 120. Triangle (Multidimensional DP)
140. 64. Minimum Path Sum (Multidimensional DP)
141. 63. Unique Paths II (Multidimensional DP)
142. 5. Longest Palindromic Substring (Multidimensional DP)
143. 97. Interleaving String (Multidimensional DP)
144. 72. Edit Distance (Multidimensional DP)
145. 123. Best Time to Buy and Sell Stock III (Multidimensional DP)
146. 188. Best Time to Buy and Sell Stock IV (Multidimensional DP)
147. 221. Maximal Square (Multidimensional DP)
148. 1406. Stone Game III (Multidimensional DP)
149. 312. Burst Balloons (Multidimensional DP)
150. 87. Scramble String (Multidimensional DP)

---

## ⚙️ Workflow Logic

### 1. Identify Target Problem
- **If argument is `next`:**
  - Check the `problems/` directory across all category subfolders for existing Python files.
  - Find the **first problem** from the Top Interview 150 list above that DOES NOT have a file inside `problems/`.
  - State which problem is being scaffolded (e.g., *"Scaffolding next problem in Top Interview 150: #88 Merge Sorted Array"*).
- **If argument is a number, name, or URL:**
  - Match the specified problem against the list or fetch its signature from LeetCode.

### 2. Categorize & Map Folder
- Place files in `problems/<category_folder>/` and `tests/<category_folder>/` using lowercase `snake_case`:
  - `array_string`, `two_pointers`, `sliding_window`, `matrix`, `hashmap`, `intervals`, `stack`, `linked_list`, `binary_tree_general`, `binary_tree_bfs`, `binary_search_tree`, `graph_general`, `graph_bfs`, `trie`, `backtracking`, `divide_and_conquer`, `kadanes_algorithm`, `binary_search`, `heap`, `bit_manipulation`, `math`, `dp_1d`, `dp_multidimensional`.

### 3. Generate Problem File (`problems/<tag>/<problem_snake_case>.py`)
- Include standard typing imports (`from typing import List, Optional, Dict, Tuple, Any`).
- Include `class Solution:` definition and signature.
- **Body MUST strictly be `pass` (no solution logic).**

### 4. Generate Pytest File (`tests/<tag>/test_<problem_snake_case>.py`)
- Import `pytest` and `Solution`.
- Include **at least 10 different types of test cases** in `@pytest.mark.parametrize` (standard examples, empty inputs, single element, negative numbers, duplicates, sorted, reversed, zero values, boundary values).

### 5. Package Init Files
- Ensure `__init__.py` exists in `problems/`, `tests/`, and active subfolders.