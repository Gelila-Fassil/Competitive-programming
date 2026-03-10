test_case = int(input())
for _ in range (test_case):
    n = int(input())
    energy = list(map(int , input().split()))
    target = int(input())
    min_val = min(energy)
    max_val = max(energy)
    if min_val <= target <= max_val:
        print("YES")
    else:
        print("NO")