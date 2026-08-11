

# 🧠 How to KNOW You Must Use Binary Search on a 1D Array

## 🔑 Core Idea

You are searching for an **element, index, position, boundary, or property** inside a **1D array** where the array has some useful ordering.

The main question is:

> **Can checking `mid` tell me which half of the array I can completely ignore?**

If YES → 🚨 Think **Binary Search**.

---

# ✅ Step-by-Step Thinking Process

## 1️⃣ Is the Array SORTED or ORDERED?

Ask:

> **Does the array have some useful order?**

Common patterns:

### Fully Sorted

```text
1  3  5  7  9  11
```

### Rotated Sorted

```text
7  9  11  1  3  5
```

### Nearly Sorted

Elements are mostly in sorted order, with a specific constraint.

### Monotonic Condition

The values themselves may not be traditionally sorted, but a condition changes in one direction:

```text
False False False True True True
```

or:

```text
0 0 0 0 1 1 1 1
```

👉 If YES → 🚨 Think Binary Search.

---

# 2️⃣ Can `mid` DISCARD HALF the Array?

This is the **most important question**.

After calculating:

```python
mid = (low + high) // 2
```

ask:

> **Can I determine that either the left half or right half cannot contain my answer?**

For example:

```text
[1, 3, 5, 7, 9, 11]
          ↑
         mid
```

If:

```text
target < nums[mid]
```

then everything to the right of `mid` is useless.

So:

```text
high = mid - 1
```

Otherwise:

```text
low = mid + 1
```

👉 If one comparison lets you eliminate half → **Binary Search**.

---

# 3️⃣ Am I Searching for an ELEMENT, INDEX, or POSITION?

Common signals:

```text
"find the element"

"find the index"

"search for target"

"first occurrence"

"last occurrence"

"search insert position"

"find minimum"

"find maximum"

"find peak"

"find boundary"

"find the smallest/largest valid position"
```

But remember:

> These keywords alone do NOT guarantee Binary Search.

You still need an ordered/monotonic search space.

---

# 4️⃣ Is the Condition MONOTONIC?

Ask:

> **Does the condition change in only one direction?**

Examples:

### Boolean condition

```text
False False False False True True True
                    ↑
                 boundary
```

You can binary search for the first `True`.

### Increasing values

```text
1  3  5  7  9  11
```

### Decreasing values

```text
11  9  7  5  3  1
```

### Rotated sorted array

```text
7  9  11  1  3  5
```

It is not globally sorted, but one side of `mid` is always sorted, allowing us to eliminate part of the search space.

👉 **Useful order / monotonicity = Binary Search candidate.**

---

# 5️⃣ Can I Maintain a SEARCH SPACE?

Think in terms of:

```text
low
mid
high
```

Initially:

```text
low = 0
high = n - 1
```

Every iteration should ideally make the search space smaller:

```text
[--------------------]
          ↓
[---------] [---------]
             ↓
        [-----]
          ↓
        [---]
          ↓
         [x]
```

If you cannot clearly explain **why `low` or `high` moves**, you probably haven't found the Binary Search logic yet.

---

# 🧩 The Golden Rule

> **Binary Search on a 1D array works when the array's ordering or a monotonic condition allows you to eliminate part of the search space after checking `mid`.**

### 🔥 Interview Shortcut

When you see a 1D array, ask:

```text
1. Is it sorted or does it have useful order?
        ↓
2. Is there a monotonic condition?
        ↓
3. Can checking mid eliminate a portion of the search space?
        ↓
4. Can I keep shrinking low...high?
        ↓
        YES
        ↓
   🚨 BINARY SEARCH
```

---

# ⚠️ Important

**Sorted array ≠ automatically Binary Search.**

Ask whether Binary Search actually helps.

The real pattern is:

```text
ORDER / MONOTONICITY
        +
ELIMINATE SEARCH SPACE
        =
BINARY SEARCH
```

---

# 🎯 Main 1D Binary Search Patterns to Master

```text
1. Basic Binary Search

2. First / Last Occurrence

3. Lower Bound

4. Upper Bound

5. Search Insert Position

6. Search in Rotated Sorted Array

7. Find Minimum in Rotated Sorted Array

8. Find Peak Element

9. Single Element in Sorted Array

10. Binary Search on a Monotonic Condition
```

Your goal is not to memorize ten separate algorithms.

Your goal is to recognize:

> **"What is my search space, and what information does `mid` give me?"**
