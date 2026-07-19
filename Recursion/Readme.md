# 📘 Recursion Cheat Sheet

> A complete revision guide for DSA interviews and coding rounds.

---

# What is Recursion?

Recursion is a technique where a function calls itself until a **base case** is reached.

Every recursive solution has two parts:

1. **Base Case** → Stops recursion.
2. **Recursive Call** → Smaller version of the same problem.

```python
def recursion():
    if base_case:
        return

    recursion()
```

---

# How Recursion Works

Example:

```python
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)

fun(3)
```

Call Stack

```
fun(3)
 |
fun(2)
 |
fun(1)
 |
fun(0)
 |
return
 |
return
 |
return
```

Output

```
3
2
1
```

---

# Anatomy of Recursion

```
Function(parameters):

    Base Case

    Do Some Work

    Recursive Call

    Return
```

---

# Types of Recursion

## 1. Linear Recursion

Only one recursive call.

```python
fun(n-1)
```

Example

- Factorial
- Sum of N numbers

Complexity

```
Time : O(n)

Space : O(n)
```

---

## 2. Binary Recursion

Two recursive calls.

```python
fun(n-1)
fun(n-2)
```

Example

- Fibonacci
- Pick / Not Pick

Complexity

```
Time : O(2^n)

Space : O(n)
```

---

## 3. Multiple Recursion

More than two recursive calls.

Example

```
N Queens

Sudoku

Maze

Graph DFS
```

---

## 4. Tail Recursion

Recursive call is the last statement.

```python
def fun(n):

    if n==0:
        return

    fun(n-1)
```

Can be optimized in some languages.

Python does **NOT** optimize tail recursion.

---

## 5. Head Recursion

Recursive call happens first.

```python
def fun(n):

    if n==0:
        return

    fun(n-1)

    print(n)
```

Output

```
1
2
3
```

---

# Recursive Thinking

Don't think about the entire recursion.

Assume

```
The recursive function already works.
```

Only solve

```
Current Level
```

---

# Base Case

Always ask

```
"When should recursion stop?"
```

Example

```python
if index == len(arr):
    return
```

Without base case

```
RecursionError

Maximum recursion depth exceeded
```

---

# Parameter Recursion

Answer is carried inside parameters.

Example

```python
def sumN(n,total):

    if n==0:
        print(total)
        return

    sumN(n-1,total+n)
```

---

# Functional Recursion

Function returns answer.

Example

```python
def sumN(n):

    if n==0:
        return 0

    return n + sumN(n-1)
```

---

# Classic Recursion Problems

## Print 1 to N

```python
def fun(i,n):

    if i>n:
        return

    print(i)

    fun(i+1,n)
```

---

## Print N to 1

```python
def fun(n):

    if n==0:
        return

    print(n)

    fun(n-1)
```

---

## Factorial

```python
def fact(n):

    if n==0:
        return 1

    return n*fact(n-1)
```

Complexity

```
Time : O(n)

Space : O(n)
```

---

## Fibonacci

```python
def fib(n):

    if n<=1:
        return n

    return fib(n-1)+fib(n-2)
```

Complexity

```
Time : O(2^n)

Space : O(n)
```

---

## Reverse Array

Two Pointer

```python
def reverse(arr,l,r):

    if l>=r:
        return

    arr[l],arr[r]=arr[r],arr[l]

    reverse(arr,l+1,r-1)
```

---

## Palindrome

```python
def check(s,l,r):

    if l>=r:
        return True

    if s[l]!=s[r]:
        return False

    return check(s,l+1,r-1)
```

---

# Pick / Not Pick Pattern

Most Important Pattern.

```
Take Element

Don't Take Element
```

Template

```python
def solve(index):

    if index==n:
        return

    # Take

    solve(index+1)

    # Not Take

    solve(index+1)
```

Problems

- Subsequences
- Subset Sum
- Combination Sum
- Count Subsequences

Complexity

```
O(2^n)
```

---

# Subsequence Template

```python
def backtrack(index,path):

    if index==n:
        print(path)
        return

    path.append(arr[index])

    backtrack(index+1,path)

    path.pop()

    backtrack(index+1,path)
```

---

# Print Subsequence Sum K

```python
def solve(index,path,total):

    if index==n:

        if total==k:
            print(path)

        return

    path.append(arr[index])

    solve(index+1,path,total+arr[index])

    path.pop()

    solve(index+1,path,total)
```

---

# Print Any One Subsequence

```python
def solve(index,path,total):

    if index==n:

        return total==k

    path.append(arr[index])

    if solve(index+1,path,total+arr[index]):
        return True

    path.pop()

    if solve(index+1,path,total):
        return True

    return False
```

---

# Count Subsequences

```python
def solve(index,total):

    if index==n:

        return 1 if total==k else 0

    take = solve(index+1,total+arr[index])

    notTake = solve(index+1,total)

    return take + notTake
```

Complexity

```
O(2^n)
```

---

# For Loop Backtracking Pattern

Used in

- Combination Sum
- Permutations
- N Queens
- Sudoku

Template

```python
def backtrack(start,path):

    answer.append(path[:])

    for i in range(start,n):

        path.append(nums[i])

        backtrack(i+1,path)

        path.pop()
```

---

# Permutation (Visited Array)

```python
def backtrack():

    if len(path)==n:

        answer.append(path[:])

        return

    for i in range(n):

        if visited[i]:
            continue

        visited[i]=True

        path.append(nums[i])

        backtrack()

        path.pop()

        visited[i]=False
```

Complexity

```
O(n*n!)
```

---

# Permutation (Swap Method)

```python
def solve(index):

    if index==n:

        answer.append(nums[:])

        return

    for i in range(index,n):

        nums[index],nums[i]=nums[i],nums[index]

        solve(index+1)

        nums[index],nums[i]=nums[i],nums[index]
```

---

# Backtracking Template

```python
Choose

Explore

Unchoose
```

Code

```python
path.append(choice)

backtrack()

path.pop()
```

---

# Decision Tree

```
               []
            /      \
          Take    Not Take
         /             \
      Take             Not
     /    \           /   \
```

---

# Call Stack

```
Main

↓

Level 1

↓

Level 2

↓

Base Case

↑

Return

↑

Return

↑

Main
```

---

# Time Complexity Cheat Sheet

| Problem | Time |
|----------|------|
| Factorial | O(n) |
| Sum N | O(n) |
| Reverse Array | O(n) |
| Palindrome | O(n) |
| Fibonacci | O(2^n) |
| Subsequences | O(2^n) |
| Print Subsequences | O(n × 2^n) |
| Subsets | O(n × 2^n) |
| Combination Sum | Exponential |
| Permutations | O(n × n!) |
| N Queens | O(N!) |
| Sudoku | Exponential |

---

# Space Complexity Cheat Sheet

| Problem | Space |
|----------|-------|
| Factorial | O(n) |
| Sum N | O(n) |
| Reverse | O(n) |
| Palindrome | O(n) |
| Subsequences | O(n) |
| Combination Sum | O(n) |
| Permutations | O(n) |
| N Queens | O(n) |

---

# Recursion vs Backtracking

| Recursion | Backtracking |
|------------|--------------|
| Function calls itself | Recursion + Undo |
| Solves smaller problems | Explores all possibilities |
| Doesn't always undo | Always undo changes |
| Example: Factorial | Example: N Queens |

---

# Common Interview Templates

### Basic Recursion

```python
def solve():
    if base:
        return

    solve()
```

---

### Return Answer

```python
return current + solve()
```

---

### Boolean

```python
if solve():
    return True

return False
```

---

### Count

```python
left = solve()

right = solve()

return left + right
```

---

### Pick / Not Pick

```python
Take

Not Take
```

---

### For Loop Backtracking

```python
for choice:

    choose

    recurse

    unchoose
```

---

### Swap Backtracking

```python
swap

recurse

swap back
```

---

# Common Mistakes

❌ Missing base case

❌ Forgetting `return`

❌ Forgetting `pop()`

❌ Modifying shared lists without copying (`path[:]`)

❌ Calling `sum(path)` at every leaf instead of carrying a running sum

❌ Wrong recursion index

❌ Infinite recursion

❌ Forgetting to undo state after recursion

---

# LeetCode Problems for Practice

## Easy

- 509 Fibonacci Number
- 344 Reverse String
- 231 Power of Two
- 326 Power of Three
- 206 Reverse Linked List

---

## Medium

- 78 Subsets
- 90 Subsets II
- 39 Combination Sum
- 40 Combination Sum II
- 46 Permutations
- 47 Permutations II
- 77 Combinations
- 17 Letter Combinations
- 22 Generate Parentheses
- 131 Palindrome Partitioning
- 216 Combination Sum III

---

## Hard

- 51 N Queens
- 52 N Queens II
- 37 Sudoku Solver
- 282 Expression Add Operators
- 301 Remove Invalid Parentheses

---

# Golden Rule

> **Recursion solves one level and trusts the recursive call to solve the remaining problem.**

> **Backtracking = Choose → Explore → Undo**