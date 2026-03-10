test_case = int(input())
for _ in range (test_case):
    n = int(input())

    size_of_decoration = list(map(int , input().split()))
    size_of_decoration.sort()
    min_operation = size_of_decoration[2] - size_of_decoration[0]
    for i in range (n-2):
        current_operation = size_of_decoration[i+2] - size_of_decoration[i]
        if current_operation < min_operation:
            min_operation = current_operation
    print(min_operation)



    
   

