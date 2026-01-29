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
