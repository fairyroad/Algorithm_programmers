#week5 3번째 문제 올바른 괄호
#올바른 괄호는 왼쪽과 오른쪽부분의 개수가 같아야하는 것에서 아이디어.....
#기본값을 false로 하고 문자열에서 하나씩 가져오면서 왼쪽 괄호면 1만큼 증가시켜주고 오른쪽 괄호면 1만큼 감소시켜서 전체를
#다 봤을 때 0이 나오면 true를 return하고 나머지는 다 false를 return하게 만들어주는 코드

def solution(s):
    answer = False
    left=0;
    for con in s:
        if con=='(':
            left+=1
        else:
            left-=1
        if left<0:
            return False
    if left==0:
        return True
    return False
