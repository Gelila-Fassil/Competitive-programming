test_case = int(input())
for _ in range(test_case):
    n = int(input())
    s = input().strip()

    a = s.find('A')
    b = s.rfind('B')

    if a == -1 or b == -1:
        print(0)
    else:
        print(max(0, b - a))

