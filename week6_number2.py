'''
2번문제 : 위장

고등학교때 경우의 수 문제를 이용해서 풀었는데 해쉬문제라고 해서 일단 dict type을 이용해서  나온 수를 세서 풀었다.
예를 들어, "face"가 3번, "headwear"가 2번, "eyewear"가 4번나왔다고 가정하면 (3번,2번,4번 나온건 직접 dict type을 이용하거나 
Counter를 이용해서 세어야 한다)선택하지 않는 경우를 0이라고 했을 때 (3+1)*(2+1)*(4+1)-1로 풀 수 있다. 
-1을 하는 이유는 선택하지 않는 경우는 제외한다고 문제에 나와있기 때문이다.

2번째줄의 answer을 1로 한 이유는 나중에 곱셈을 할 때 0으로 두면 무조건 답이 0으로 나오기 때문에 초기화시킨 값이다.

4번에 name,kind in clothes는 clothes에서 값을 받아와서 이미 kinds(dict type)에 존재하는 값이 아니면 1로, 기존에 존재하는 값이라면 기존값+1로 할 수 있게 처리한 것이다. 

이건 아래의 소스코드에 counter를 이용해서 더 간단하게 계산할 수도 있다.

9번~10번째줄은 kinds에서 cloth값을 하나씩 받아오면 (3+1)*(4+1)*(2+1)처럼 계산해 주기 위한 코드이닷

11번째줄은 공집합을 빼주기 위해 answer-1을 했당
'''
def solution(clothes):
    answer = 1
    kinds={}
    for name,kind in clothes:
        if kind in kinds:
            kinds[kind]+=1
        else:
            kinds[kind]=1
    for cloth in kinds:
        answer*=kinds[cloth]+1
    return answer-1
  
  
  #---------------------------------------[좋은 풀이]---------------------------------------
 '''
5번째줄 코드에서 collections.Counter([x[1] for x in c])부분은 원래 x에는 yellowhat, headgear 형태로 들어가져 있는데 이중에 headgear부분만 뽑아내어 중복되는 수를 계산하겠다는 의미가 된다. 

[a+1 for a in collections.Counter([x[1] for x in c]).values()는 그렇게 계산된 값은 "face"가 3번, "headwear"가 2번, "eyewear"가 4번형태로 들어가지는데 그 중에 3,2,4라는 숫자만 하나씩 뽑아내서 

y값으로 (3+1),(2+1),(4+1)형태로 하나씩 들어가진다는 의미가 된다. 

reduce는 factorial계산하는 것과 같이 누적된 값이 x로 들어가지는 함수를 의미한다.

전체 계산된 경우의 수에서 공집합경우를 제외해야 하므로 return 전체-1을 하는 코드이다.

이 코드는 프로그래머스에서 봐서 정리하려고 기록했는데 이게 더 좋은 코드인것같당!!
 '''
  
import collections
from functools import reduce
 
def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1

  
  
