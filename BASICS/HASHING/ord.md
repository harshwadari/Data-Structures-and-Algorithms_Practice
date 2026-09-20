````markdown
# Python `ord()` and `chr()` — DSA Cheat Sheet

## 1. What is `ord()`?

`ord()` is a built-in Python function that converts a **single character into its Unicode code point (number)**.

```python
ord('a')   # 97
ord('b')   # 98
ord('c')   # 99
````

For lowercase English letters:

```text
a → 97
b → 98
c → 99
...
z → 122
```

For uppercase letters:

```text
A → 65
B → 66
C → 67
...
Z → 90
```

---

## 2. What is Unicode?

Computers represent characters using numbers.

For example:

```python
ord('A')   # 65
ord('B')   # 66

ord('a')   # 97
ord('b')   # 98

ord('0')   # 48
ord('1')   # 49
```

Each character has a corresponding Unicode code point.

---

# 3. `ord()` and `chr()` are opposites

### Character → Number

```python
ord('a')
```

Output:

```text
97
```

### Number → Character

```python
chr(97)
```

Output:

```text
'a'
```

Think of them as:

```text
ord() → character → number

chr() → number → character
```

---

# 4. Most Important DSA Pattern

## Convert `a-z` into `0-25`

Use:

```python
ord(ch) - ord('a')
```

Example:

```python
ord('a') - ord('a')   # 0
ord('b') - ord('a')   # 1
ord('c') - ord('a')   # 2
ord('d') - ord('a')   # 3
```

Therefore:

```text
a → 0
b → 1
c → 2
d → 3
...
z → 25
```

This is one of the most common uses of `ord()` in DSA.

---

# 5. Convert `a-z` into `1-26`

Use:

```python
ord(ch) - ord('a') + 1
```

Example:

```python
ord('a') - ord('a') + 1   # 1
ord('b') - ord('a') + 1   # 2
ord('c') - ord('a') + 1   # 3
```

Therefore:

```text
a → 1
b → 2
c → 3
...
z → 26
```

---

# 6. Reverse Mapping: `a-z` → `26-1`

If you want:

```text
a → 26
b → 25
c → 24
...
z → 1
```

Use:

```python
ord('z') - ord(ch) + 1
```

Example:

```python
ord('z') - ord('a') + 1
# 122 - 97 + 1
# 26
```

```python
ord('z') - ord('b') + 1
# 122 - 98 + 1
# 25
```

```python
ord('z') - ord('z') + 1
# 122 - 122 + 1
# 1
```

Therefore:

```text
a → 26
b → 25
c → 24
...
z → 1
```

---

# 7. Reverse Mapping Cheat Sheet

| Requirement        | Formula                  |
| ------------------ | ------------------------ |
| `a → 0 ... z → 25` | `ord(ch) - ord('a')`     |
| `a → 1 ... z → 26` | `ord(ch) - ord('a') + 1` |
| `a → 26 ... z → 1` | `ord('z') - ord(ch) + 1` |

### Memorize these three.

---

# 8. Convert Index Back to Character

Suppose you have:

```text
0 → a
1 → b
2 → c
3 → d
...
25 → z
```

Use:

```python
chr(ord('a') + index)
```

Example:

```python
chr(ord('a') + 0)   # 'a'
chr(ord('a') + 1)   # 'b'
chr(ord('a') + 2)   # 'c'
chr(ord('a') + 3)   # 'd'
```

For example:

```python
i = 3

ch = chr(ord('a') + i)

print(ch)
```

Output:

```text
d
```

---

# 9. `ord()` for Frequency Arrays

One of the most common DSA applications is using a fixed array of size `26` instead of a dictionary.

### Dictionary approach

```python
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```

### Using `ord()`

```python
freq = [0] * 26

for ch in s:
    index = ord(ch) - ord('a')
    freq[index] += 1
```

Now:

```text
freq[0]  → frequency of 'a'
freq[1]  → frequency of 'b'
freq[2]  → frequency of 'c'
...
freq[25] → frequency of 'z'
```

This technique is useful for:

* Frequency counting
* Anagrams
* Character counting
* String hashing
* Sliding window
* Two pointers
* Substring problems

---

# 10. Example: Frequency Counting

Given:

```python
s = "banana"
```

We can do:

```python
freq = [0] * 26

for ch in s:
    index = ord(ch) - ord('a')
    freq[index] += 1
```

The important mappings are:

```text
b → 1
a → 0
n → 13
```

So:

```text
freq[0]  = 3   # a
freq[1]  = 1   # b
freq[13] = 2   # n
```

---

# 11. Character Comparison

Characters can be compared because their Unicode code points are ordered.

```python
'a' < 'b'
```

Output:

```text
True
```

Because:

```text
97 < 98
```

You can check whether a character is lowercase using:

```python
if 'a' <= ch <= 'z':
    print("lowercase")
```

You don't necessarily need `ord()` for this.

---

# 12. Checking Character Ranges

### Lowercase letter

```python
if 'a' <= ch <= 'z':
    ...
```

### Uppercase letter

```python
if 'A' <= ch <= 'Z':
    ...
```

### Digit

```python
if '0' <= ch <= '9':
    ...
```

You can also use Python's built-in methods:

```python
ch.islower()
ch.isupper()
ch.isdigit()
```

---

# 13. `ord()` in LC 3498 — Reverse Degree of a String

For reverse alphabet values:

```text
a → 26
b → 25
c → 24
...
z → 1
```

The formula is:

```python
ord('z') - ord(ch) + 1
```

Then multiply by the **1-based position**.

For example:

```text
s = "abc"
```

Positions:

```text
a → position 1
b → position 2
c → position 3
```

Reverse values:

```text
a → 26
b → 25
c → 24
```

So the contributions are:

```text
26 × 1
25 × 2
24 × 3
```

The code is:

```python
total += (ord('z') - ord(s[i]) + 1) * (i + 1)
```

### Important

Use:

```python
i + 1
```

because the problem uses **1-based positions**.

---

# 14. Why `i + 1` Instead of `i`?

Python indexing starts at `0`:

```text
index:     0   1   2   3
character: a   b   c   d
```

But if a problem defines positions starting from `1`:

```text
position:  1   2   3   4
character: a   b   c   d
```

Therefore:

```python
position = i + 1
```

Not:

```python
position = i
```

---

# 15. Doing the Same Thing Without `ord()`

Yes, you can do these mappings without `ord()`.

One approach is using the alphabet string:

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

### `a → 1 ... z → 26`

```python
value = alphabet.index(ch) + 1
```

### `a → 26 ... z → 1`

```python
value = 26 - alphabet.index(ch)
```

For example:

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"

ch = 'd'

value = 26 - alphabet.index(ch)

print(value)
```

Output:

```text
23
```

Because:

```text
alphabet.index('d') = 3

26 - 3 = 23
```

However, `ord()` is usually cleaner and more direct for character-to-index conversions in DSA.

---

# 16. Why Does `ord()` Work for Alphabet Mapping?

The important thing is that lowercase English letters have consecutive Unicode values:

```text
a = 97
b = 98
c = 99
d = 100
...
z = 122
```

Therefore:

```python
ord('d') - ord('a')
```

becomes:

```text
100 - 97 = 3
```

So `'d'` has index `3` relative to `'a'`.

This is why:

```python
ord(ch) - ord('a')
```

works.

---

# 17. `ord()` Is Not Only for `a-z`

You can use `ord()` with any single Unicode character.

Examples:

```python
ord('A')   # 65
ord('Z')   # 90

ord('0')   # 48
ord('9')   # 57
```

It also works with Unicode characters:

```python
ord('₹')
ord('é')
ord('中')
```

The returned value is their Unicode code point.

---

# 18. `chr()` Can Work With the Result

You can convert the number back:

```python
number = ord('d')

character = chr(number)

print(character)
```

Output:

```text
d
```

So:

```text
'd'
   ↓
ord()
   ↓
100
   ↓
chr()
   ↓
'd'
```

---

# 19. `ord()` + `chr()` Together

You can convert:

```text
character → index → character
```

Example:

```python
ch = 'd'

index = ord(ch) - ord('a')

new_ch = chr(ord('a') + index)

print(index)    # 3
print(new_ch)   # d
```

Conceptually:

```text
'd'
 ↓
3
 ↓
'd'
```

---

# 20. Important DSA Patterns

## Pattern 1 — Character → 0-based index

```python
index = ord(ch) - ord('a')
```

Result:

```text
a → 0
b → 1
...
z → 25
```

---

## Pattern 2 — Character → 1-based value

```python
value = ord(ch) - ord('a') + 1
```

Result:

```text
a → 1
b → 2
...
z → 26
```

---

## Pattern 3 — Reverse alphabet value

```python
value = ord('z') - ord(ch) + 1
```

Result:

```text
a → 26
b → 25
...
z → 1
```

---

## Pattern 4 — Index → Character

```python
ch = chr(ord('a') + index)
```

Result:

```text
0 → a
1 → b
...
25 → z
```

---

# 21. Quick Mental Model

Think of the alphabet as an array:

```text
Index:     0   1   2   3   4   ... 25
           ↓   ↓   ↓   ↓   ↓       ↓
Letter:    a   b   c   d   e   ... z
```

Then:

```python
ord(ch) - ord('a')
```

finds the **index** of the character.

And:

```python
chr(ord('a') + index)
```

converts the **index back into a character**.

---

# 22. Final Cheat Sheet

```python
# Character → Unicode number
ord('a')                    # 97

# Unicode number → Character
chr(97)                     # 'a'


# a → 0, b → 1, ..., z → 25
ord(ch) - ord('a')


# a → 1, b → 2, ..., z → 26
ord(ch) - ord('a') + 1


# a → 26, b → 25, ..., z → 1
ord('z') - ord(ch) + 1


# 0 → a, 1 → b, ..., 25 → z
chr(ord('a') + i)
```

---

# ⭐ What You Actually Need to Memorize

For DSA, memorize these four:

```python
# a → 0 ... z → 25
ord(ch) - ord('a')
```

```python
# a → 1 ... z → 26
ord(ch) - ord('a') + 1
```

```python
# a → 26 ... z → 1
ord('z') - ord(ch) + 1
```

```python
# 0 → a ... 25 → z
chr(ord('a') + i)
```

Everything else follows from understanding these four patterns.

```
```
