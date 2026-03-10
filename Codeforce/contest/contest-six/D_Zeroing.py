n , k = map(int , input().split())
a = sorted(list(set(map(int , input().split()))))

if a and a[0] == 0 :
    a.pop(0)

total_subtracted = 0
count = 0

for val in a :
    if count < k :
        current_min = val - total_subtracted
        print(current_min)

        total_subtracted += current_min
        count +=1
    else:
        break
while count < k:
    print(0)
    count +=1

