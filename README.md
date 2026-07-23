<p align="center">
  <img src="https://img.shields.io/badge/Problems%20Solved-500+-blue?style=for-the-badge&logo=leetcode&logoColor=white" />
  <img src="https://img.shields.io/badge/Python%20Files-298-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Sheet-Striver's%20A--Z-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

# 🚀 Data Structures & Algorithms — Striver's A-Z Sheet

> A comprehensive, well-organized collection of **500+ DSA problems** solved in **Python**, structured around [Striver's A-Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) and supplemented with LeetCode dailies, LeetCode 75, and SDE Sheet problems.

---

## 📖 About

This repository is my personal DSA journey — every problem researched, coded, and committed as I work through Striver's A-Z roadmap and beyond. Each solution is written in clean Python with a focus on understanding the underlying approach, not just getting an accepted submission. Most files contain **multiple approaches** (Brute → Better → Optimal) with time & space complexity analysis.

**Profile:** [takeuforward.org/profile/harshwadari](https://takeuforward.org/profile/harshwadari)

---

## 📂 Repository Structure

```
StriversSheet/
│
├── 📁 BASICS/                                  # Fundamentals (16 files)
│   ├── MATH/                                    #   Count Digits, GCD, Armstrong, Palindrome, Prime (7)
│   ├── HASHING/                                 #   Frequency Count, Hashmap Intro (3)
│   └── PATTERNS/                                #   Star/Number Pattern Programs (6)
│
├── 📁 SORTING/                                  # Sorting Algorithms (6 files)
│   └── Bubble, Selection, Insertion, Merge, Quick, Counting Sort
│
├── 📁 Arrays/                                   # Array Problems (43 files)
│   ├── Easy/                                    #   Rotate Array, Max Consecutive Ones, Single Number (16)
│   ├── Medium/                                  #   Sort Colors, Longest Consecutive Seq, Leaders (13)
│   │   └── Matrix/                              #   Spiral Matrix, Search 2D Matrix, Rotate 90° (10)
│   └── Hard/                                    #   3Sum, 4Sum, Merge Intervals, Count Inversions (14)
│
├── 📁 Strings/                                  # String Problems (14 files)
│   ├── Easy/                                    #   Reverse String, basic manipulations (6)
│   ├── Medium/                                  #   Roman to Int, ATOI, Sort by Frequency, Longest Palindromic Substr (7)
│   └── Hard/                                    #   KMP Pattern Matching Algorithm (1)
│
├── 📁 BinarySearch/                             # Binary Search (29 files)
│   ├── Bson1Darrays/                            #   BS LC 704, Rotated Array, Peak Element, Floor/Ceil (14 .py)
│   ├── BSonAnswers/                             #   Koko Bananas, Median of 2 Arrays, Painter's Partition (10 .py)
│   └── BSon2DArrays/                            #   Search 2D Matrix I & II, Row with Min 1s (3)
│
├── 📁 Recursion/                                # Recursion & Backtracking (30 files)
│   ├── BASIC/                                   #   Palindrome, Fibonacci, Reverse Array, Sort Stack (6)
│   ├── Medium/                                  #   Subsets, Combination Sum, Generate Parentheses, Pow(x,n) (17)
│   └── Hard/                                    #   N-Queens, Sudoku Solver, Word Search, Word Break (7)
│
├── 📁 LinkedList/                               # Linked Lists (31 files)
│   ├── SLL/                                     #   Singly Linked List
│   │   ├── Basics/                              #     Implementation, Length, Search, Delete (5)
│   │   ├── medium/                              #     Cycle Detect, Reverse, Middle, Add Two Numbers (17)
│   │   └── Hard/                                #     Copy Random Pointer, Reverse k-Group, Flatten (4)
│   └── DLL/                                     #   Doubly Linked List
│       ├── Basic/                               #     DLL Construction, Reverse DLL (2)
│       └── Medium/                              #     Delete Key, Pairs with Sum, Remove Duplicates (3)
│
├── 📁 StackandQueues/                           # Stacks & Queues (21 files)
│   ├── Learning/                                #   Valid Parentheses, Min Stack, Stack↔Queue Impl (8)
│   ├── Pre_in_Pos_Conversion_Problems/          #   All 6 Infix/Prefix/Postfix conversions (6)
│   ├── MonotonicStack/                          #   NGE I & II, Largest Rect Histogram, Trapping Rain Water (5)
│   └── Implementation_Problems/                 #   Sliding Window Max (Deque), Online Stock Span (2)
│
├── 📁 SlidingWindow&TwoPointer/                 # Sliding Window & Two Pointer (10 files)
│   ├── MEDIUM/                                  #   Longest Substring, Max Ones III, Fruit Baskets (8)
│   └── HARD/                                    #   Min Window Substring, Subarrays with K Different Ints (2)
│
├── 📁 Binary_Trees/                             # Binary Trees (9 files)
│   ├── Traversal/                               #   Node class, Pre/In/Post Order, Level Order BFS (5)
│   ├── Medium/                                  #   Max Depth, Balanced BT, Diameter, Max Path Sum (4)
│   └── Hard/                                    #   (in progress)
│
├── 📁 BitManipulation/                          # Bit Manipulation (8 files)
│   └── EASY/                                    #   Check Bit, Set/Toggle, Count Bits, Power of 2, Divide (8)
│
├── 📁 Graphs/                                   # Graph Algorithms (31 files)
│   ├── Learning/                                #   Adjacency List & Matrix representations (1)
│   ├── Graph_traversal/                         #   BFS & DFS templates (2)
│   ├── Problems on DFSandBFS/                   #   Islands, Rotten Oranges, Flood Fill, Cycle Detection (10)
│   ├── Shortest_Path_Algorithms/                #   Dijkstra, Bellman-Ford, Floyd Warshall, Network Delay (12)
│   └── Topo_Sort_Problems/                      #   Topo Sort, Kahn's Algo, Course Schedule, Safe States (6)
│
├── 📁 Greedy_Aglorithm/                         # Greedy Algorithms (14 files)
│   ├── Easy/                                    #   Assign Cookies, Lemonade Change, Fractional Knapsack (5)
│   └── Medium/                                  #   Gas Station, Jump Game I & II, Candy, Merge Intervals (9)
│
├── 📁 DynamicProgramming/                       # Dynamic Programming (12 files)
│   ├── Intro_DP/                                #   DP state transition theory guide
│   ├── 1DP/                                     #   Fibonacci, Climbing Stairs, House Robber I & II, Frog Jump (7)
│   └── DP_ON_GRIDS/                             #   Unique Paths I/II/III, Min Path Sum, Triangle (5)
│
├── 📁 DSA_PATTERNS/                             # Pattern Guides & Cheat Sheets
│   └── TWO_POINTERS/                            #   Two Pointer problem list & README
│
├── 📁 LEETCODE_75/                              # LeetCode 75 Study Plan (8 files)
│   ├── Arrays_Strings/                          #   GCD Strings, Merge Alternately, Product Except Self (7)
│   └── Reverse Words in a String (1)
│
├── 📁 LeetCode_POTD/                            # LeetCode Problem of the Day (21 files)
│   └── Max Balloons, Sequential Digits, Highest Altitude, Ice Cream Bars, ...
│
├── 📁 SDE_SHEET/                                # SDE Sheet Extras (2 files)
│   └── ARRAYS/                                  #   Next Permutation, Set Matrix Zeroes
│
├── README.md                                    # Original README
└── NEW_README.md                                # ← You are here
```

---

## 📊 Topic-wise Breakdown

| # | Topic | Files | Difficulty Spread | Standout Problems |
|---|-------|-------|------------------|-------------------|
| 1 | **Basics & Math** | 16 | 🟢 Easy | GCD (Euclidean), Prime Check, Pattern Programs |
| 2 | **Sorting** | 6 | 🟢🟡 Easy–Med | Merge Sort $O(N \log N)$, Quick Sort (Lomuto/Hoare) |
| 3 | **Arrays** | 43 | 🟢🟡🔴 All | 3Sum, 4Sum, Count Inversions, Spiral Matrix, Merge Intervals |
| 4 | **Strings** | 14 | 🟢🟡🔴 All | KMP Algorithm, Longest Palindromic Substring, ATOI |
| 5 | **Binary Search** | 27 | 🟢🟡🔴 All | Median of 2 Sorted Arrays, Aggressive Cows, Painter's Partition |
| 6 | **Recursion & Backtracking** | 30 | 🟢🟡🔴 All | N-Queens, Sudoku Solver, Word Break, Expression Add Operators |
| 7 | **Linked List** | 31 | 🟢🟡🔴 All | Reverse k-Group, Copy Random Pointer, Flatten Multi-Level |
| 8 | **Stacks & Queues** | 21 | 🟢🟡🔴 All | Trapping Rain Water, Largest Rect Histogram, Sliding Window Max |
| 9 | **Sliding Window** | 10 | 🟡🔴 Med–Hard | Min Window Substring, Subarrays with K Different Ints |
| 10 | **Binary Trees** | 9 | 🟢🟡 Easy–Med | Max Path Sum, Diameter, Balanced Tree |
| 11 | **Bit Manipulation** | 8 | 🟢 Easy | Kernighan's Set Bits, Divide Without Operator |
| 12 | **Graphs** | 31 | 🟡🔴 Med–Hard | Dijkstra, Bellman-Ford, Floyd Warshall, Word Ladder, Topo Sort |
| 13 | **Greedy** | 14 | 🟢🟡 Easy–Med | Candy, Gas Station, Jump Game I & II, Job Sequencing |
| 14 | **Dynamic Programming** | 12 | 🟡🔴 Med–Hard | House Robber I & II, Unique Paths III, Triangle |
| 15 | **LeetCode 75** | 8 | 🟢🟡 Easy–Med | Product Except Self, Increasing Triplet |
| 16 | **LeetCode POTD** | 21 | 🟢🟡🔴 All | Diverse daily challenges |
| 17 | **SDE Sheet** | 2 | 🟡 Medium | Next Permutation, Set Matrix Zeroes |
| 18 | **DSA Patterns** | — | — | Two Pointer reference guides |

> **Totals: 305 files · 298 Python files · 500+ problems solved across platforms**

---

## 🧠 Code Style & Approach

Each solution follows a consistent methodology visible across the codebase:

```
┌─────────────────────────────────────────────────────┐
│  1. Brute Force    →  Understand the problem fully  │
│  2. Better         →  Reduce one complexity factor   │
│  3. Optimal        →  Apply the right DS / pattern   │
│  4. Complexity     →  TC and SC documented in code   │
│  5. Test Cases     →  Driver code with sample inputs │
└─────────────────────────────────────────────────────┘
```

Most Python files contain **multiple solutions** for the same problem, progressing from brute force to optimal, with clearly labeled time complexity (`TC`) and space complexity (`SC`) annotations.

---

## 🛠️ Tech Stack

| | |
|---|---|
| **Language** | Python 3 |
| **Primary Sheet** | [Striver's A-Z DSA Course](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) |
| **Platforms** | LeetCode · GeeksforGeeks · HackerRank |
| **Key Algorithms** | Dijkstra · Bellman-Ford · Floyd Warshall · KMP · Merge Sort · Quick Sort |
| **Key Techniques** | Sliding Window · Two Pointer · Monotonic Stack · Memoization · Tabulation |

---

## 🏆 Competitive Profiles

| Platform | Profile |
|----------|---------|
| 🟠 **LeetCode** | [leetcode.com/u/harshwadari](https://leetcode.com/u/harshwadari/) |
| 🟢 **GeeksforGeeks** | [geeksforgeeks.org/profile/harshwadari](https://www.geeksforgeeks.org/profile/harshwadari) |
| 🟣 **HackerRank** | [hackerrank.com/profile/harshwadari](https://www.hackerrank.com/profile/harshwadari) |
| 🔵 **Codolio** | [codolio.com/profile/harshwadari](https://codolio.com/profile/harshwadari) |
| 🟡 **Take U Forward** | [takeuforward.org/profile/harshwadari](https://takeuforward.org/profile/harshwadari) |

---

## 🎯 Goals

- ✅ Build strong problem-solving fundamentals
- ✅ Master core DSA topics — Arrays, Strings, Trees, Graphs, DP
- ✅ Implement all major graph algorithms from scratch
- 🔄 Complete the full Striver's A-Z sheet (ongoing)
- 🔄 Expand DP section — Subsequences, Strings, Stocks, LIS
- 🔄 Solve 1000+ problems across platforms
- 🎯 Crack software engineering interviews at top tech companies

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/harshwadari/Data-Structures-and-Algorithms_Practice.git

# Navigate to any topic
cd StriversSheet/Arrays/Hard/

# Run a solution
python 3Sum.py
```

Each `.py` file is self-contained with driver code — just run it directly to see the output.

---

## 📈 How to Navigate

| Want to... | Go to... |
|-----------|----------|
| Study a specific topic | Browse the topic folder (e.g., `Graphs/`) |
| Filter by difficulty | Look inside `Easy/`, `Medium/`, `Hard/` subdirectories |
| Learn algorithmic patterns | Check `DSA_PATTERNS/` for cheat sheets |
| See daily challenge solutions | Browse `LeetCode_POTD/` |
| Follow Striver's roadmap | Folders mirror the A-Z sheet structure |
| Review expression conversions | `StackandQueues/Pre_in_Pos_Conversion_Problems/` |
| Learn graph shortest paths | `Graphs/Shortest_Path_Algorithms/` (12 implementations) |

---

## 🤝 Contributing

This is a personal practice repository, but feel free to:
- ⭐ **Star** the repo if you find it helpful
- 🍴 **Fork** it to track your own progress
- 💬 **Open an issue** to discuss a solution or suggest an improvement

---

## 📜 License

This project is open source and available for educational purposes.

---

<p align="center">
  <i>Consistency beats intensity. One problem a day keeps unemployment away. 💪</i>
</p>


