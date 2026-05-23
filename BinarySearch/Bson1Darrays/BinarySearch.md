🧠 How to KNOW you must use Binary Search on ARRAYS
🔑 Core Idea

You are searching for a position / index / element
inside a sorted or conditionally sorted array.

✅ Step-by-Step Thinking Process (EXACT)
1️⃣ Is the array SORTED or PARTIALLY SORTED?

Ask:

Does the array have order?

Sorted patterns include:

Fully sorted

Rotated sorted

Bitonic (mountain)

Nearly sorted

Sorted by condition (0s then 1s, false then true)

👉 If YES → 🚨 Think Binary Search

2️⃣ Can one comparison DISCARD HALF the array?

Ask:

After checking mid, can I say left half or right half is useless?

If a single if decides direction → Binary Search.

3️⃣ Am I asked for an INDEX or POSITION?

Keywords:

“find index”

“first occurrence”

“last occurrence”

“peak element”

“minimum in rotated array”

👉 If YES + sorted → Binary Search

4️⃣ Is the condition MONOTONIC over indices?

Think:

Does the condition switch only once?

Examples:

False False False True True

smaller → larger

increasing → decreasing

👉 Single switch = Binary Search

🧩 The Golden Rule (WRITE THIS)

Binary Search on arrays works when the array order allows discarding one half after checking mid.