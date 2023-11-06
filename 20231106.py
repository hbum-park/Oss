def solution(n):
    hap = 0
    if(n%2==1):
        for i in range(1,n+1,2):
            hap+=i
    else:
        for i in range(2,n+1,2):
            hap+=i**2
    return hap
