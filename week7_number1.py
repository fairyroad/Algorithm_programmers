'''
1.모든 경우의 수를 찾아내야 하는데 순서가 바뀌면 안됨

->combinations를 사용

->근데 모든 combinations수를 찾아내기에는 시간이 많이 걸림

->len(number)-k만큼중에 가장 큰 수를 찾아내서 index를 저장하고 그 이후부터만 찾는걸로 함

->이렇게 해서 돌렸더니 코드실행에서는 통과가 되는데 결과에서는 시간초과가 뜸

->TEAM EDA분이 푸신 코드를 참고해서 정리해봄

-------------------------------------------------------------------------------------------------------------------------------------

1.stack을 이용해서 풀어야 하는데 기존 number로 구성된 list의 첫값과 stack에 포함된 것들 중 top값을 비교해서 list의 첫값이 더 크면 pop을 시키면서 k값을 하나씩 줄임 

2.근데 이것만 하게 되면 나중에 54321처럼 값이 나왔을 때 pop되는 k값이 없어서 문제가 생기므로 맨 마지막에 짤려야 하는 숫자만큼 없애는 코드도 만들어주어야 함
'''

from itertools import combinations
def solution(number, k):
    answer = ''
    result=[]
    a=number[:len(number)-k]
    i=number.find(max(a))
    mid=combinations(number[i:],len(number)-k)
    for num in mid:
        result.append(int(''.join(num)))  
    result=list(set(result))
    answer=str(max(result))
    return answer
#--------------------------------------------------------------------------------
  def solution(number, k):
    answer = ''
    stack=[number[0]]
    for num in number[1:]:
        while k>0 and len(stack)>0 and stack[-1]<num:
            k=k-1
            stack.pop()
        stack.append(num)
    if k!=0:
        stack=stack[:-k]
    return ''.join(stack)
  
