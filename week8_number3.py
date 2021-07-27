'''
3번문제 : 문자열압축 (카카오)

1.새롭게 알게 된 내용

먼저 python은 //이라는 operator가 있는데 소수점을 버리는 나눗셈 연산자라고 함

그리고 문자열은 배열형태로 되서 parsing을 [ : ]이런식으로 할 수 있음 

당연히 맨끝에 들어가는 것은 포함안됨

따라서 10번째줄에 s[ : cut]은 맨 처음부터 cut-1까지의 문자열만 parsing되어 들어감

2.문제 푸는 방법

[원래 내 생각]
제일 먼저 생각했던 것은 어차피 맨끝까지 할 필요는 없고 전체길이를 반으로 나눈 길이 만큼만 반복해서 가장 짧게 들어가지는 것의 개수를 세면 된다고 생각했음

: 근데 list형태로 만들어서 min쓰면 된다는 것 까지는 생각하지 못함

그리고 range에서 step을 사용할 수 있다고는 들었지만 진짜 step을 사용해 본 적은 없었는데 11번째처럼 해주면 자동으로 cut만큼 다음으로 건너뛰게 됨

=> 문제푸는 방법은 단순하게 parsing할 개수만큼 반복해서 최솟값을 구해내야 하는데 

최솟값을 구해내는 방법은 문자열을 parsing할 개수만큼 반복하고 맨 마지막은 loop를 빠져나오면서 result에 들어가지 못하니까 마지막에 직접 넣어주어야 함

cf) python은 parsing할때 기존의 문자열보다 더 긴 문자열을 불러와도 원래 문자열 길이만큼만 return함

예를 들어, s="abcde"이고 s[3:8]이라고 하면 de만 return함
'''

def solution(s):
    candidate=[]
    result=""
 
    if len(s)==1:
        return 1
 
    for cut in range(1,len(s)//2+1):
        cnt=1
        temp=s[:cut]
        for i in range(cut,len(s),cut):
            if s[i:i+cut]==temp:
                cnt+=1
            else:
                if cnt==1:
                    cnt=""
                result=result+str(cnt)+temp
                cnt=1
                temp=s[i:cut+i]
        if cnt==1:
            cnt=""
        result =result+str(cnt)+temp
        candidate.append(len(result))
        result=""
    return min(candidate)
