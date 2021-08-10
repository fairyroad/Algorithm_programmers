'''
네번째 문제 : 메뉴리뉴얼 ( 다른 풀이 참고)

1.course를 하나씩 꺼내면서 course에 맞는 개수를 orders를 돌면서 전체 경우의 수를 찾아내야겠다.

->근데 전체 경우의 수를 순서대로 찾아내려면 combinations를 이용할까??

->아니면 저번 문제처럼 stack을 이용해서 찾아낼까??

->근데 경우의 수를 다 찾아내도 개수가 가장 높은것들을 모두 넣어야 되는데 그 값이 2보다 크거나 같아야 한다.

여기서 포인트는 경우의 수를 가장 빠르게 찾아내고 개수가 2이상이면서 높은것을 모두 찾아내야 한다.

->중복의 개수를 찾아내는건 counter를 이용하면 된다고 한다. 

2.마지막의 정답은 오름차순으로 정렬되어있어야 한다.

---------------------------------------------------------------------------------------------------

5번째 줄(for num in course부분) course에서 하나씩 뽑아진 2,3,4같은 숫자들을 combination에서 뽑아낼 개수로 넣어줄 때 사용할 loop이다.

8번째줄에서(combination = combinations(sorted))부분은 그냥 order를 쓰지 않고 sorted(order)를 사용하는 이유는 배열의 각 원소가 오름차순이어야 하기 때문이다.

10번째줄의 Counter는 중복되는 개수들을 세주는 역할을 하고 

11번째줄은 counter의 길이가 0이거나 아니면 최댓값이 1면 answer에 담지 말라는 조건이 있기 때문에 넣었다.

12번째줄의 ''.join(result)를 사용한 이유는 값들이 ('W','X'):2 이런식으로 저장이 되어 있어서 WX로 바꿔주기 위해서 넣은 것이다. list comprehension을 사용하면 조금 더 빠르게 돌릴 수 있다. 

12번째줄의 if문 처럼 각각의 for 문에 조건을 줄 수 도 있다. 

써야 되는 것들은 다 똑같았었는데 join을 마지막에 쓰는거랑 sorted하지 않았던 것 때문에 처음에 틀렸었당 ㅠ

'''

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for num in course:
        tmp = []
        for order in orders:
            combination = combinations(sorted(order), num)
            tmp += combination
        counter = Counter(tmp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(result) for result in counter if counter[result] == max(counter.values())]
 
    return sorted(answer)
