'''
카카오 순위검색문제

처음 작성했던 코드인데 정확성만 모두 통과하고 효율성은 하나도 통과하지 못했당,,,,,
----------------------------------------------------------------------------------------------------------

이 문제를 푸는 핵심은 hashmap을 이용하는 것과 lower bound를 사용하는 것이다.

먼저 7번째 줄 부터 10번째줄은 hashmap에 넣기 위한 준비를 하는 과정인데 전체 문장들중에 맨마지막 부분에 score이 있고 우리는 해당 score보다 크거나 같은 값을 기준으로 찾아낼 것이기 때문에 분리를 시켜주어야 한다. 일반 문장 vs score 값으로 따라서 info_key는 [:-1]이고 info_value는 [-1]이 된다.

이렇게 나눠진 값을 combination을 사용해서 모든 조합들을 만들어낼 건데 나중에 '-'가 포함된게 나왔을 때를 대비해서 만드는 것이다. 그걸 위한 코드가 12번째줄부터 14번째줄 까지이다.

그렇게 dictionary를 만들어서 저장을 했으면 16~17번째줄에서는 score값에 따라 정렬을 한다. 나중에 lower bound알고리즘을 사용해서 구할때 정렬이 되어있어야 구할 수 있기 때문이다. 

19번째 부터 21번째도 7~10번째줄과 같은 맥락인데 score와 나머지로 분리를 한다.

해당 query에는 -, and 와 같은 필요없는 단어들이 포함이 되어있으므로 제거시켜주는 코드가 바로 24~27번째 문장이다. 28번째는 만들어진 해당 단어들을 합쳐서 하나의 문장으로 만들어내는 역할을 한다.

이제 query와 조건이 맞는 아이들을 찾아내는 코드들이 나오는데 이 때 사용하는게 lower bound알고리즘이다. 일반적인 binary search과정과 거의 비슷하다고 생각하면 된다. 만약 36번째줄처럼 query_score보다 크거나 같은 게 등장하게 된다면 answer에서 조건에 맞는 애들만 가져오면 된다.  

30~42번째줄까지 읽어보면 lower bound가 뭘 의미하는지 바로 이해할 수 있을 것이다. 

'''
def solution(info, query):
    answer = []
    new_query=[q.replace(" and "," ").split(" ") for q in query]
    new_info=[i.split(" ") for i in info]
    for nq in new_query:
        cnt=0
        for ni in new_info:
            j=0
            for i in range(5):
                if nq[i]=="-" or nq[i]==ni[i] or (i==4 and int(nq[i])<=int(ni[i])):
                    j+=1                   
            if j==5:
                cnt+=1
        answer.append(cnt)
    return answer
  
#-----------------------------------------------------------------
  
from itertools import combinations
from collections import defaultdict
 
def solution(infos,queries):
    answer=[]
    info_dict=defaultdict(list)
    for info in infos:
        info=info.split()
        info_key=info[:-1]
        info_val=int(info[-1])
        for i in range(5):
            for c in combinations(info,i):
                tmp_key=''.join(c)
                info_dict[tmp_key].append(info_val)
 
    for key in info_dict.keys():
        info_dict[key].sort()
 
    for query in queries:
        query=query.split(' ')
        query_score=int(query[-1])
        query=query[:-1]
 
        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q=''.join(query)
 
        if tmp_q in info_dict:
            scores=info_dict[tmp_q]
            if len(scores)>0:
                start,end=0,len(scores)
                while end>start:
                    mid=(start+end)//2
                    if scores[mid]>=query_score:
                        end=mid
                    else:
                        start=mid+1
                answer.append(len(scores)-start)
        else:
            answer.append(0)
    return answer

  
