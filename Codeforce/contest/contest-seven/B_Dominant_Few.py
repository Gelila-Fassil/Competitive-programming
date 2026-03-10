test_case = int(input())
for _ in range (test_case):
    num_players = int(input())
    skills = list(map(int , input().split()))

    skills.sort(reverse=True)
    e_sum = skills[0]
    c_sum = skills[1] + skills[2]

    solution = False
    if e_sum > c_sum :
        solution = True
    else:
        e_index = 1
        c_index = 3

        while c_index < num_players:
            e_sum += skills[e_index]
            c_sum += skills[c_index]

            if e_sum > c_sum:
                solution = True
                break
            e_index +=1
            c_index +=1
    if solution:
        print("YES")
    else:
        print("NO")
        





