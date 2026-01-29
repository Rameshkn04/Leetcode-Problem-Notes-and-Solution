🧠 Key Observation (MOST IMPORTANT)

You are allowed to:

Flip the signs of any two adjacent elements any number of times

This operation has a hidden invariant:

👉 The parity (even/odd) of the number of negative elements never changes.

Why?

Each operation flips exactly 2 elements

Negatives can change by 0 or 2, but never by 1

🎯 Goal

Maximize the sum of the array.

That means:

Ideally, make all numbers positive

But parity constraint may stop us

✅ Strategy
Step 1: Take absolute values

If there were no restrictions, best sum =

sum(|a[i]|)

Step 2: Count negatives

Let neg = number of negative elements

Let min_abs = minimum of |a[i]|

Step 3: Apply parity rule
Case 1: neg is even

✅ We can make all elements positive

Answer = sum(|a[i]|)

Case 2: neg is odd

❌ One element must stay negative

To minimize loss:

Keep the element with smallest absolute value negative

Answer = sum(|a[i]|) - 2 * min_abs

🧪 Why subtract 2 * min_abs?

Because:

Instead of +min_abs, it becomes -min_abs

Loss = min_abs + min_abs = 2 * min_abs

✅ Final Solve() Function (Python)
def Solve():
    n = int(input())
    arr = list(map(int, input().split()))

    total = 0
    neg_count = 0
    min_abs = float('inf')

    for x in arr:
        if x < 0:
            neg_count += 1
        abs_x = abs(x)
        total += abs_x
        min_abs = min(min_abs, abs_x)

    # If number of negatives is odd, one must remain negative
    if neg_count % 2 == 1:
        total -= 2 * min_abs

    print(total)

📌 Example Walkthrough
Example 1
-1 -1 -1


Negatives = 3 (odd)

sum(|a|) = 3

min_abs = 1

👉 Answer = 3 - 2 = 1 ✅

Example 2
1 5 -5 0 2


Negatives = 1 (odd)

sum(|a|) = 13

min_abs = 0

👉 Answer = 13 - 0 = 13 ✅

⏱️ Complexity

Time: O(n)

Space: O(1)
