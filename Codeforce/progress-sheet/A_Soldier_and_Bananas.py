k, n, w = map(int, input().split())
total_cost = k * (w * (w + 1) // 2)
borrow = total_cost - n
if borrow < 0:
    print(0)
else:
    print(borrow)