Youssef_status = input().split()
Youssef_wins = int(Youssef_status[0])
Youssef_time = int(Youssef_status[1])

n = int(input())
for i in range (n):
    warrior_data = input().split()
    warrior_wins = int (warrior_data[0])
    warrior_time = int (warrior_data[1])

    if warrior_wins > Youssef_wins or (warrior_wins == Youssef_wins and warrior_time < Youssef_time):
        print ("The Fallen Champion")
        break
    
else :
    print ("The Champion Saves the Accused")

        
    

