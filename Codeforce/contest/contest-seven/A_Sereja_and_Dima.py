length = int(input())
cards = list(map(int , input().split()))

s_score = 0
d_score = 0

left = 0
right = len(cards)-1
turn = 0

while left <= right :
    if cards[left] > cards[right]:
        pick = cards[left]
        left += 1
    else:
        pick = cards[right]
        right -=1
    if turn % 2 == 0:
        s_score += pick
    else:
        d_score +=pick
    turn +=1
print(s_score , d_score)
   

