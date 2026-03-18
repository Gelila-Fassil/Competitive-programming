# Read n and k
line1 = input().split()
if line1:
    n, k = map(int, line1)
    num = list(map(int, input().split()))
    num.sort()
    if k == 0:
        if num[0] > 1:
            print(1)
        else:
            print(-1)
    else:
        ans = num[k-1]
        if k < n and num[k-1] == num[k]:
            print(-1)
        else:
            print(ans)