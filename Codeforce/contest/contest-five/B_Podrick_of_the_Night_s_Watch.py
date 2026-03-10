n = int(input())
raven_tracker = {}

for i in range(n):
    m = int(input())
    for j in range(m):
        message = input().split()
        name = message[0]
        hour = message[1]

        key = (name, hour)
        
        if key in raven_tracker:
            raven_tracker[key] += 1
        else:
            raven_tracker[key] = 1
goal = n * 0.8
is_suspicious = False

for count in raven_tracker.values():
    if count >= goal:
        is_suspicious = True
        break
if is_suspicious:
    print("YES")
else:
    print("NO")