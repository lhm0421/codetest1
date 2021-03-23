def solution(n):
    import math 
    jaecob = math.sqrt(n)
    if jaecob == int(jaecob):
        return pow(jaecob+1,2)
    return -1
