'''
3번문제 : 타겟 넘버

recursion써야하는것도 알고 left,right나누어서 하는것도 생각났는데 막상 코드 적으려고 하니까 아무 생각이 나질 않아서 다른 사람 풀이 2개 찾음

3번째줄의 (x,-x)는 하나는 +값, 하나는 -값으로 바꿔주기 위한 코드이다.

4번째줄의 product는 여러개의 조합들을 모두 구해주는데 map(sum,product(*poss))를 하게 되면 그렇게 나온 조합들의 모든 합들을 구해주는 역할을 해준당

5번째줄의 count는 target값과 일치하는 것들의 개수를 세어주는 역할을 하는 코드이다.
'''

from itertools import product
def solution(numbers, target):
    poss=[(x,-x) for x in numbers]
    possible=list(map(sum,product(*poss)))
    return possible.count(target)
  
'''
3번째줄은 list의 길이를 받아오는 역할을 한당!!

5번째줄부터 11번째줄까지는 recursion인데 아직 더 탐색해야할 게 남아있다면 +값으로 만들어둔걸로 operator를 한번 돌고 -값으로 만들어준걸로 operator를 한번돌게 되는 코드이다. 

13번째줄의 elif부분은 전체 numbers의 합을 구해서 target값과 같게 된다면 우리가 원하는 답이니까 cnt를 1만큼증가시키게 된다. nonlocal을 해준 이유는 위의 2번째줄의 cnt를 가리키기 위해서 이다. 

'''
  def solution(numbers, target):
    cnt = 0
    len_numbers = len(numbers)
 
    def operator(idx=0):
        if idx < len_numbers:
            numbers[idx] *= 1
            operator(idx+1)
 
            numbers[idx] *= -1
            operator(idx+1)
 
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
 
    operator()
 
    return cnt
