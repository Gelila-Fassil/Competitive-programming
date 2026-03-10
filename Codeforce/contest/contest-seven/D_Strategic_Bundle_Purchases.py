import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        
        a.sort(reverse=True)  # descending: most expensive first
        b.sort()  # ascending: use smaller coupons first
        
        saved = 0
        idx = 0  # current position in sorted items
        
        for x in b:
            if idx + x > n:
                # Not enough items left to use this coupon
                continue
            # Use coupon on items [idx : idx+x]
            # Save the cheapest among them, which is at position idx+x-1
            saved += a[idx + x - 1]
            # Move pointer past these x items
            idx += x
        
        total = sum(a)
        print(total - saved)

solve()