import bisect
def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]
    max_books = 0
    for i in range(n):
        target = pref[i] + t
        j = bisect.bisect_right(pref, target) - 1
        max_books = max(max_books, j - i)
    print(max_books)

solve()