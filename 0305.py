def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor ==0:
            answer.append(i)
    if len(answer) == 0:
            answer.append(-1)
    else:
            answer.sort()
    return answer

#나누어 떨어지는수
