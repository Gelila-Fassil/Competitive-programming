t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    all_houses = []
    for i in range(n):
        hand = list(map(int, input().split()))
        hand.sort()
        all_houses.append((hand, i + 1))
    all_houses.sort() 
    p = []
    for house in all_houses:
        p.append(house[1])
    possible = True
    for i in range(n):
        hand = all_houses[i][0]
        for j in range(m):
            if hand[j] != i + (j * n):
                possible = False
                break
        if not possible:
            break
    if possible:
        print(*(p))
    else:
        print("-1")