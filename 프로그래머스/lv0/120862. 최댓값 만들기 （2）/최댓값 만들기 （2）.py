def solution(numbers):
    minus = []
    plus = []
    for i in numbers:
        if i < 0:
            minus.append(i)
        else:
            plus.append(i)
    minus.sort()
    plus.sort()
    if len(minus) == 1 and len(plus) == 1:
        answer = minus[-1] * plus[-1]
    elif len(minus) < 2:
        answer = plus[-1] * plus[-2]
    elif len(plus) < 2:
        answer = minus[-1] * minus[-2]
    elif len(minus) >=2 and len(plus) >=2:
        answer = max(minus[-1]*minus[-2], plus[-1]*plus[-2])
    return answer