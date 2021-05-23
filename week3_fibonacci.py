#while문을 돌면서 피보나치수를 계산하고
#123456789의 나머지를 구함
def solution(n):
    first=0;second=1;num=2;answer=0
    while num<=n:
        answer=first+second
        first=second
        second=answer
        num+=1
    return answer%1234567
