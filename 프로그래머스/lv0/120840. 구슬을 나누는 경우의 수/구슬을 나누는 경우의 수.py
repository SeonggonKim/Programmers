def solution(balls, share):
    boonmo = 1
    boonja = 1
    
    for _ in range(share):
        boonmo *= balls
        balls -= 1
    
    for _ in range(share):
        boonja *= share
        share -= 1
    
    answer = boonmo / boonja
    
    return answer