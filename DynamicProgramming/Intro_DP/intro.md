# 📘 Dynamic Programming (DP) - Quick Notes

## What is DP?

Dynamic Programming (DP) is an **optimization technique** used when a problem has:

### 1. Overlapping Subproblems
- The same subproblem is solved multiple times.

### 2. Optimal Substructure
- The solution of the main problem can be built from solutions of smaller subproblems.

### Goal

Avoid recomputing the same states.

Instead of solving the same problem repeatedly, **store the answer and reuse it.**

---

# 🤔 When Should I Think About DP?

If the problem asks for:

- ✅ Count ways
- ✅ Minimum / Maximum value
- ✅ Best possible answer
- ✅ Number of paths
- ✅ Subsequences
- ✅ Partition problems
- ✅ Game strategy
- ✅ Recursion with repeated calls

### Common Keywords

- Count
- Maximum
- Minimum
- Ways
- Possible
- Can we?
- Optimize

---

# 📝 General DP Steps

1. Write the recursive solution.
2. Identify the changing parameters.
3. Define the DP state.
4. Write the recurrence relation.
5. Apply Memoization.
6. Convert it to Tabulation.
7. Optimize space if possible.

---

# 🚀 DP Approaches

## 1. Pure Recursion

### Idea
Solve every possible choice.

### Store Answers?
❌ No

### Time Complexity
```
Usually O(2^N) or worse
```

### Space Complexity
```
O(N) (Recursion Stack)
```

### Pros
- Easy to think about.

### Cons
- Repeated calculations.

---

## 2. Memoization (Top-Down DP)

### Idea
Recursion + Cache previously computed answers.

### Store Answers?
✅ Yes (DP Array / HashMap)

### Time Complexity
```
O(Number of States)
```

### Space Complexity
```
O(Number of States) + O(Recursion Stack)
```

### Pros
- Easy conversion from recursion.
- Eliminates repeated work.

### Cons
- Recursion overhead.

---

## 3. Tabulation (Bottom-Up DP)

### Idea
Build answers from the smallest state to the required state.

### Store Answers?
✅ Yes

### Time Complexity
```
O(Number of States)
```

### Space Complexity
```
O(Number of States)
```

### Pros
- No recursion.
- Usually faster than Memoization.

### Cons
- Need the correct iteration order.

---

## 4. Space Optimization

### Idea
Store only the previous states that are actually required.

### Store Answers?
- Few variables
- 1-D DP Array

### Time Complexity
```
Same as Tabulation
```

### Space Complexity
```
Reduced
```

### Example (Fibonacci)

Instead of

```text
dp[0...n]
```

Use

```text
prev2
prev1
curr
```

Space Complexity

```text
O(1)
```

---

# ⏱️ Time Complexity Summary

| Approach | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Recursion | Exponential | O(N) |
| Memoization | O(States) | O(States) + O(N) |
| Tabulation | O(States) | O(States) |
| Space Optimization | O(States) | Minimum Possible |

---

# 🎯 How to Identify the DP State

Ask yourself:

> **"What changes in every recursive call?"**

Examples:

### Example 1

```python
f(index)
```

State

```text
(index)
```

---

### Example 2

```python
f(index, target)
```

State

```text
(index, target)
```

---

### Example 3

```python
f(i, j)
```

State

```text
(i, j)
```

---

### Example 4

```python
f(i, prev)
```

State

```text
(i, prev)
```

> The changing parameters become the DP dimensions.

---

# ⭐ Golden Rule

```text
Recursion
     ↓
Memoization
     ↓
Tabulation
     ↓
Space Optimization
```

❌ Never jump directly to DP.

✅ Always understand the recursive solution first.

---

# 📚 Most Common DP Patterns

1. Fibonacci Pattern
2. Climbing Stairs
3. Frog Jump
4. House Robber (Maximum Sum of Non-Adjacent Elements)
5. Ninja Training
6. Grid DP
7. Knapsack
8. Subset Sum
9. Coin Change
10. Longest Common Subsequence (LCS)
11. Longest Increasing Subsequence (LIS)
12. Matrix DP
13. Partition DP
14. Digit DP
15. Bitmask DP

---

# 🧠 DP Formula

```text
State
   ↓
Transition
   ↓
Base Case
   ↓
Answer
```

Everything in Dynamic Programming revolves around these **four concepts**.

---

# 💡 One Rule to Remember

> **Don't memorize DP solutions. Learn to derive them from recursion.**

If you can write the recursive solution, converting it into **Memoization**, **Tabulation**, and **Space Optimization** becomes much easier.