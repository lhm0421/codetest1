def solution(n):
    sam3 = list()
    answer = 0
    while n >=3:
        sam3.append(n%3)
        n = n//3
    
    sam3.append(n)
    sam3.reverse()
    
    for i in range(len(sam3)):
        
        answer = answer + (sam3[i] * 3**i)
    return answer