# 🧠 Binary Search on Answer — Complete Notes

## 1. What Is Binary Search on Answer?

In normal Binary Search, we search for an **element/index** in a sorted array.

```text
Normal Binary Search
        ↓
Search for an index/value
```

In **Binary Search on Answer**, we don't search an array.

We search the **range of possible answers**.

```text
Binary Search on Answer
        ↓
Search for the optimal answer
```

Typical answers:

* Minimum speed
* Minimum time
* Minimum capacity
* Minimum possible maximum sum
* Maximum possible minimum distance
* Smallest value satisfying a condition
* Largest value satisfying a condition

---

# 2. The Core Idea

The main idea is:

> **Guess an answer → Check whether it is possible → Use monotonicity to eliminate half the answers.**

Think:

```text
        Answer Space
    ┌───────────────────┐
    │ low ........ high │
    └───────────────────┘
             ↓
          choose mid
             ↓
       check(mid)
             ↓
       possible / impossible
             ↓
       eliminate half
```

---

# 3. The Three Conditions

Do NOT use Binary Search on Answer just because the problem asks for a minimum or maximum.

You should check **three things**.

```text
1. Is it an optimization problem?
2. Can I check a guessed answer?
3. Is that check monotonic?
```

If all three are true:

```text
🚨 Binary Search on Answer
```

---

# 4. Step 1 — Is It an Optimization Problem?

Look for words such as:

* minimum
* maximum
* smallest
* largest
* least
* maximum possible
* minimum possible
* smallest possible
* largest possible

Examples:

```text
Minimum eating speed
Minimum ship capacity
Minimum time
Maximum minimum distance
Minimum possible largest subarray sum
```

### ⚠️ Important

This alone is **NOT enough**.

For example:

> Find the minimum element in an unsorted array.

This doesn't automatically mean Binary Search on Answer.

You still need a **checkable and monotonic condition**.

---

# 5. Step 2 — Can I Check a Guessed Answer?

This is the most important question.

Ask yourself:

> **"If I guess the answer is X, can I determine whether X is possible?"**

This is called a **feasibility check**.

---

## Example 1 — Koko Eating Bananas

Suppose we guess:

```text
speed = 10
```

We can calculate whether Koko can finish all bananas within the given number of hours.

So:

```text
possible(10)
```

returns:

```text
True
```

or:

```text
False
```

---

## Example 2 — Ship Packages

Suppose we guess:

```text
capacity = 50
```

We can check whether all packages can be shipped within `D` days.

```text
possible(50)
```

returns:

```text
True / False
```

---

## Example 3 — Book Allocation

Suppose we guess:

```text
maximum pages = 100
```

Can we distribute the books among students such that no student receives more than `100` pages?

```text
possible(100)
```

returns:

```text
True / False
```

---

## Example 4 — Painter's Partition

Suppose we guess:

```text
maximum time = 50
```

Can all boards be assigned to the painters such that no painter needs more than `50` units of work?

```text
possible(50)
```

returns:

```text
True / False
```

---

# 6. Step 3 — Is the Check Monotonic?

This is the **deciding factor**.

Suppose we have a candidate answer `X`.

Ask:

> If `X` works, will larger values also work?

OR:

> If `X` fails, will smaller values also fail?

If YES, the search space is **monotonic**.

---

# 7. Monotonic Pattern

## Pattern 1 — Find Minimum Valid Answer

```text
False False False False True True True True
                         ↑
                       Answer
```

Here:

```text
If X works,
all X > X also work.
```

So we search for the:

> **First True**

This is common when finding:

* Minimum speed
* Minimum capacity
* Minimum time
* Minimum maximum sum

---

## Pattern 2 — Find Maximum Valid Answer

```text
True True True True False False False False
                   ↑
                 Answer
```

Here:

```text
If X fails,
all X > X also fail.
```

So we search for the:

> **Last True**

This is common for problems such as:

* Maximum possible minimum distance

---

# 8. The Golden Rule

## ⭐ Memorize This

> **Binary Search on Answer is used when the answer space is checkable and monotonic.**

Even better:

```text
Guess
  ↓
Check
  ↓
Monotonic
  ↓
Binary Search
```

### Final mental rule:

> **If I can guess the answer, check it, and the check is monotonic → Binary Search on Answer.**

---

# 9. How to Find the Answer Space

Once you identify Binary Search on Answer, determine:

```text
low
high
```

These represent the smallest and largest possible answers.

---

## Example — Koko

If:

```text
piles = [3, 6, 7, 11]
```

Minimum possible speed:

```text
1
```

Maximum useful speed:

```text
max(piles) = 11
```

Therefore:

```text
low = 1
high = 11
```

---

## Example — Ship Packages

```text
weights = [1, 2, 3, 4, 5]
```

Minimum capacity:

```text
max(weights) = 5
```

Maximum capacity:

```text
sum(weights) = 15
```

Therefore:

```text
low = max(weights)
high = sum(weights)
```

---

## Example — Split Array Largest Sum

```text
nums = [7, 2, 5, 10, 8]
```

Minimum possible maximum subarray sum:

```text
max(nums) = 10
```

Maximum possible maximum subarray sum:

```text
sum(nums) = 32
```

Therefore:

```text
low = max(nums)
high = sum(nums)
```

---

# 10. Generic Template — Minimum Answer

For most "minimum possible" problems:

```python
low = smallest_possible_answer
high = largest_possible_answer

while low < high:

    mid = (low + high) // 2

    if possible(mid):
        high = mid
    else:
        low = mid + 1

return low
```

### Why?

If `mid` works:

```text
mid might be the answer
```

So:

```python
high = mid
```

We try to find an even smaller valid answer.

If `mid` doesn't work:

```text
mid is too small
```

So:

```python
low = mid + 1
```

---

# 11. Generic Template — Maximum Answer

For problems where we want the **maximum valid answer**:

```python
low = smallest_possible_answer
high = largest_possible_answer

while low <= high:

    mid = (low + high) // 2

    if possible(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

return answer
```

If `mid` works:

```text
Try something larger.
```

Therefore:

```python
low = mid + 1
```

---

# 12. The `possible(mid)` Function

This is usually where the **greedy logic** comes in.

For example:

```python
def possible(mid):
    parts = 1
    current = 0

    for x in nums:

        if current + x <= mid:
            current += x

        else:
            parts += 1
            current = x

    return parts <= k
```

This pattern appears in:

* Book Allocation
* Painter's Partition
* Split Array Largest Sum

The Binary Search is the same.

Only the **story** changes.

---

# 13. Three Important Problems That Are Basically the Same

## 📚 Book Allocation

Goal:

```text
Minimize the maximum number of pages
assigned to any student.
```

Example:

```text
books = [10, 20, 30, 40]
students = 2
```

We are searching:

```text
maximum pages per student
```

Answer space:

```text
max(books) → sum(books)
```

Check:

```text
Can I allocate books to at most k students
such that each student gets <= mid pages?
```

---

# 14. 🎨 Painter's Partition

Goal:

```text
Minimize the maximum time/work assigned
to any painter.
```

We are searching:

```text
maximum work/time per painter
```

Answer space:

```text
max(boards) → sum(boards)
```

Check:

```text
Can I divide the boards into at most k
contiguous groups where each group's sum <= mid?
```

---

# 15. 📦 Split Array Largest Sum

Goal:

```text
Split the array into k contiguous subarrays
such that the largest subarray sum is minimized.
```

We are searching:

```text
minimum possible largest subarray sum
```

Answer space:

```text
max(nums) → sum(nums)
```

Check:

```text
Can I split nums into at most k subarrays
where every subarray has sum <= mid?
```

---

# 16. 🔥 Recognize the Pattern

These three:

```text
Book Allocation
Painter's Partition
Split Array Largest Sum
```

are essentially the same algorithm:

```text
                 Binary Search
                      ↓
               Search answer
                      ↓
                Guess mid
                      ↓
              Greedy feasibility
                      ↓
             How many partitions?
                      ↓
                 <= k ?
                /      \
              YES       NO
               ↓         ↓
           decrease    increase
```

The story changes.

The pattern doesn't.

---

# 17. Common Problems

| Problem                 | Search On            | Typical Check           |
| ----------------------- | -------------------- | ----------------------- |
| Koko Eating Bananas     | Speed                | Hours required          |
| Ship Packages in D Days | Capacity             | Days required           |
| Allocate Books          | Maximum pages        | Students required       |
| Painter's Partition     | Maximum work         | Painters required       |
| Split Array Largest Sum | Maximum subarray sum | Partitions required     |
| Aggressive Cows         | Minimum distance     | Cows that can be placed |

---

# 18. Quick Recognition Table

| Problem asks for...                 | Think...     |
| ----------------------------------- | ------------ |
| Minimum speed                       | BS on Answer |
| Minimum capacity                    | BS on Answer |
| Minimum time                        | BS on Answer |
| Minimum maximum sum                 | BS on Answer |
| Maximum minimum distance            | BS on Answer |
| Smallest value satisfying condition | BS on Answer |
| Largest value satisfying condition  | BS on Answer |

But always verify:

```text
Optimization
     +
Checkable
     +
Monotonic
```

---

# 19. Common Mistakes

## ❌ Mistake 1

> "The problem says minimum, so I'll use Binary Search."

Wrong.

Minimum/maximum is only a **signal**.

You still need:

```text
checkable + monotonic
```

---

## ❌ Mistake 2

Searching the array instead of the answer.

For example:

```text
Split Array Largest Sum
```

You are NOT searching for an element.

You are searching:

```text
10, 11, 12, 13, ... 32
```

These are possible answers.

---

## ❌ Mistake 3

Choosing the wrong `low`.

For partition/sum problems:

```python
low = max(nums)
```

because no partition can have a sum smaller than the largest individual element.

---

## ❌ Mistake 4

Choosing the wrong `high`.

Usually:

```python
high = sum(nums)
```

because putting everything into one partition is always the maximum possible total.

---

# 20. Interview Thinking Process

When you encounter a new problem:

### Ask 1

```text
What am I optimizing?
```

Example:

```text
minimum maximum sum
```

### Ask 2

```text
What can be my smallest answer?
```

### Ask 3

```text
What can be my largest answer?
```

### Ask 4

```text
If I guess mid, can I check it?
```

### Ask 5

```text
Does possible(mid) behave monotonically?
```

If yes:

```text
🚨 Binary Search on Answer
```

---

# 21. Full Mental Template

```text
                 Problem
                    ↓
          Is it optimization?
                    ↓
                  YES
                    ↓
       What is the answer range?
                    ↓
              low → high
                    ↓
              Guess mid
                    ↓
       Can I check mid?
             /          \
           NO            YES
           ↓              ↓
       Maybe not       Is it monotonic?
                         ↓
                        YES
                         ↓
             Binary Search on Answer
```

---

# 22. Interview Explanation

If the interviewer asks:

> Why are you using Binary Search?

Say:

> **"I'm not searching for an element. I'm searching the answer space. For every candidate answer `mid`, I can check whether it is feasible, and feasibility is monotonic. Therefore, I can use Binary Search on Answer to find the optimal value."**

---

# 🧠 Final Cheat Sheet

```text
BINARY SEARCH ON ANSWER

1. Optimization problem?
       ↓
2. Define possible answer range
       ↓
3. Guess mid
       ↓
4. Can I check mid?
       ↓
5. Is the check monotonic?
       ↓
6. YES → Binary Search
```

## ⭐ MEMORIZE

> **GUESS → CHECK → MONOTONIC → BINARY SEARCH**

And for partition problems:

```text
low  = max(array)
high = sum(array)

mid = (low + high) // 2

possible(mid)
    ↓
How many groups/parts are needed?
    ↓
parts <= k ?
```

### 🔥 The biggest pattern to remember

```text
Allocate Books
Painter's Partition
Split Array Largest Sum
```

All follow:

```text
MINIMIZE
    ↓
maximum load
    ↓
Binary Search on Answer
    ↓
Greedy feasibility check
    ↓
partition into <= k groups
```
