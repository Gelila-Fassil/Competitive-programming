test_case = int(input())
for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    max_val = max(a)
    count = a.count(max_val)
    if count % 2 != 0:
        print("YES")
    else:
        print("NO")