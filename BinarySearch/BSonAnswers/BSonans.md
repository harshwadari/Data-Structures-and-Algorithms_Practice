🧠 How to KNOW you must use Binary Search on ANSWERS (Answer Space BS)
🔑 Core Idea

You are not searching an index,
you are searching the minimum / maximum valid answer.

✅ Step-by-Step Thinking Process (EXACT)
1️⃣ Does the problem ask for:

Minimum possible value, or

Maximum possible value

Keywords:

“minimum time”

“minimum speed”

“maximum distance”

“least capacity”

“smallest number such that…”

👉 If YES → 🚨 Answer Space Binary Search

2️⃣ Can I CHECK a given answer?

Ask yourself:

“If I guess an answer X, can I tell whether it works or not?”

This is the most important test.

Examples:

Can Koko eat bananas at speed X?

Can ships be shipped in X days?

Can painters paint in X time?

👉 If YES → Binary Search is possible

3️⃣ Is the check MONOTONIC?

This is the deciding factor.

Ask:

If X works, will all bigger X also work?
OR
If X fails, will all smaller X also fail?

This creates a pattern like:

False False False True True True


or

True True True False False


👉 This monotonic behavior = Binary Search

🧩 The Golden Rule (WRITE THIS)

Binary Search on answer is used when the answer space is monotonic and checkable.

🧠 Mental Template (Very Important)

Whenever you see such a problem, think:

Answer range = low to high

mid = guessed answer

if possible(mid):

save mid

try smaller / larger

else:

move opposite side

📌 Very Common Signals (Instant Recognition)
Problem says	Think
minimum speed	BS on speed
minimum time	BS on time
smallest capacity	BS on capacity
maximum minimum	BS on answer
least number	BS
🔁 Real Examples (Just Names)

Koko Eating Bananas

Ship Packages in D Days

Allocate Books

Aggressive Cows

Painters Partition

(All are Binary Search on Answer)

🧠 One-line Interview Explanation

“The answer space is monotonic, and I can validate any mid, so I apply binary search on answers.”

🔥 Final Notebook Line (MEMORIZE)

If I can guess the answer and check it, and the check is monotonic → Binary Search on Answer.