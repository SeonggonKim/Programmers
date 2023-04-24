def solution(balls, share):
    boonmo = 1
    boonja = 1
    
    for _ in range(share):
        boonja *= balls
        balls -= 1
    
    for _ in range(share):
        boonmo *= share
        share -= 1
    
    answer = boonja / boonmo
    
    return answer