def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] += arr1[i][j]
            answer[i][j] += arr2[i][j]
            
    return answer