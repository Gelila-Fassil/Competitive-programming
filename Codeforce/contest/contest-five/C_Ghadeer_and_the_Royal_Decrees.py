test_case = int(input())

for _ in range(test_case):
   
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])

    numbers = list(map(int, input().split()))
    current_max = max(numbers)
    
    results = []

    for i in range(m):
        op_data = input().split()
        sign = op_data[0]
        lower = int(op_data[1])
        upper = int(op_data[2])
      
        if lower <= current_max <= upper:
            if sign == "+":
                current_max += 1
            else:
                current_max -= 1
        
        results.append(str(current_max))

    print(" ".join(results))