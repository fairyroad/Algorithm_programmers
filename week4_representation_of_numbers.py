#첫번째 문제 _ 숫자의 표현
#연속이 된 자연수들로 n을 표현하는 방법 찾는 문제
#bruteforce로 찾음
#6이 들어오면 1 + 2 + 3으로 표현할 수 있는 모든 방법을 찾는 건데 
#i를 기준으로 하나씩 숫자를 올려가면서 연속해서 6이 되는게 있는 것을 모두 찾는 방법을 이용
def solution(n):
    answer = 0
    num=1
    for j in range(1,n+1):
        nsum=0
        for i in range(num,n+1):
            if i+nsum<=n:
                nsum+=i
                if nsum==n:
                    answer+=1
                    break; 
            else:
                break;
        num+=1
    return answer
