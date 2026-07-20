# Pattern 1: Two Pointers

## Definition

Two Pointers is a technique where **two indices** are used to traverse an array or string instead of one.

Instead of checking every possible pair (**O(n²)**), two pointers often reduce the complexity to **O(n)** or **O(n log n)**.

### Typical Setup

```python
left = 0
right = len(arr) - 1

while left < right:
    # process

    if condition:
        left += 1
    else:
        right -= 1
```

---

# Core Idea

Imagine the array as a straight line.

Instead of moving one pointer, move **two pointers** toward a goal.

Each pointer has a specific purpose.

### Example

```text
1 2 3 4 5 6 7 8

L             R
```

Every pointer movement eliminates impossible answers, making the algorithm much faster.

---

# When Should I Think of Two Pointers?

Whenever you notice one or more of the following clues.

---

## Clue 1 — Sorted Array

Examples:

- Two Sum II
- Pair Sum
- Closest Pair
- Triplets
- Remove Duplicates

If the array is **sorted**, think **Two Pointers** first.

---

## Clue 2 — Pair Problems

Questions asking for:

- Find a pair
- Find two numbers
- Count pairs
- Maximum pair
- Minimum pair

These are strong indicators for Two Pointers.

---

## Clue 3 — Opposite Ends

Problems involving:

- Container
- Palindrome
- Reverse
- Squares
- Trapping Rain Water
- Merge

Visualization:

```text
Left ----->

<----- Right
```

---

## Clue 4 — Need O(n)

If the question says:

> Can you solve it in linear time?

Immediately think of:

- Hashing
- Two Pointers
- Sliding Window

---

## Clue 5 — Remove or Rearrange Elements

Examples:

- Move Zeroes
- Remove Duplicates
- Partition
- Dutch National Flag

Usually solved using:

```text
slow
fast
```

---

## Clue 6 — Merge Two Sorted Arrays

```text
A ---->

B ---->

Result
```

This almost always uses Two Pointers.

---

## Clue 7 — String Comparison

Examples:

- Valid Palindrome
- Backspace String Compare
- Reverse String
- Reverse Words

Think Two Pointers.

---

# Types of Two Pointers

---

## Type 1 — Opposite Direction

```text
L ---------------- R
```

### Used In

- Pair Sum
- Palindrome
- Container With Most Water
- Squares of Sorted Array
- Trapping Rain Water

---

## Type 2 — Same Direction (Slow & Fast)

```text
slow
fast
```

### Used In

- Remove Duplicates
- Move Zeroes
- Stable Partition
- Compress Array

---

## Type 3 — Merge

```text
i -> Array 1

j -> Array 2
```

### Used In

- Merge Arrays
- Merge Intervals
- Median of Two Sorted Arrays
- Union of Arrays
- Intersection of Arrays

---

## Type 4 — Expand & Shrink

```text
left

right
```

This is the foundation of the **Sliding Window** pattern.

---

# Thinking Process

Whenever you see a problem, ask yourself:

### Step 1

**Is the array sorted?**

```
YES
 ↓
Two Pointers
```

---

### Step 2

**Is the problem asking for a pair?**

```
YES
 ↓
Two Pointers
```

---

### Step 3

**Need to compare elements from both ends?**

```
YES
 ↓
Two Pointers
```

---

### Step 4

**Need to remove duplicates or rearrange elements?**

```
YES
 ↓
Slow & Fast Pointer
```

---

### Step 5

**Need to merge two sorted arrays?**

```
YES
 ↓
Two Pointers
```

---

# Generic Templates

## 1. Opposite Ends

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition:
        return

    elif something:
        left += 1

    else:
        right -= 1
```

---

## 2. Slow & Fast

```python
slow = 0

for fast in range(len(arr)):

    if condition:
        arr[slow] = arr[fast]
        slow += 1
```

---

## 3. Merge Two Sorted Arrays

```python
i = 0
j = 0

while i < n and j < m:

    if a[i] < b[j]:
        i += 1
    else:
        j += 1
```

---

# Common Mistakes

- ❌ Forgetting to move a pointer
- ❌ Infinite loop
- ❌ Moving the wrong pointer
- ❌ Ignoring duplicate values
- ❌ Using `<` instead of `<=` (or vice versa)
- ❌ Applying Two Pointers on an unsorted array when sorting or hashing is required

---

# Time Complexity

| Technique | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Brute Force Pair | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |
| Sorting + Two Pointers | O(n log n) | O(1) or O(log n) |

---

# Quick Revision Checklist

- ✅ Is the array sorted?
- ✅ Does the problem involve finding a pair?
- ✅ Can I start from both ends?
- ✅ Can I use slow & fast pointers?
- ✅ Is this a merge problem?
- ✅ Can I eliminate impossible answers by moving pointers?
- ✅ Will Two Pointers reduce O(n²) to O(n)?

---

# One-Line Rule

> **Whenever you can eliminate impossible answers by intelligently moving two indices instead of checking every possibility, think Two Pointers.**