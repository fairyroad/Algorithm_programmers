def solution(n):
    first=0;second=1;num=2;answer=0
    while num<=n:
        answer=first+second
        first=second
        second=answer
        num+=1
    if n==2:
        return 1
    return answer%1234567