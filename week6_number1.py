'''
1번 문제: 더 맵게


1.종료조건은 모든 음식의 스코빌 지수가 K이상!!

-> 스코빌 지수가 가장 작은 값이 K보다 작을 때는 계속 loop를 돌 수 있게 해야 겠다.

2.제일 낮은 값 2개를 찾아야 하는데

->pop을 시켜서 찾자

여기까지 생각했었는데 문제 처음 보고 너무 쉽다고 생각했었다. 
근데 계속 효율성에서 걸려서 뭐가 문제인지 봤는데 heap을 써야지 풀리는 문제라고 한당,,, 
그래서 heapq에 대해 검색을 해봤고 import heapq를 해서 사용하면 된다고 한다. 
처음에 할당하는 걸 몰라서 for문으로 돌렸었는데 시간이 생각보다 많이 걸리는것같아 찾아보니 heapify라는 함수가 있었당.

7번은 종료조건과 관련이 된건데 가장 작은값이 K보다 작으면 계속 loop를 돌 수 있게 하는 것이다.

8번줄은 10번째 줄을 보면 2개를 pop시켜야 되는데 만약 남아있는게 1개라면 더이상 pop시킬 수 없어서 오류가 생기게 되는걸 미리 방지하기 위해 넣었다. 

heap은 pop을 시키면 return값을 돌려주게 된다.

'''
import heapq
 
def solution(scoville, K):
    answer=0
    heap=[]
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<=1:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer+=1
    return answer

'''
위의 python코드를 그냥 c++로 변환한 것 밖에 없당

근데 그냥 vector로 하고 싶어서 처음에 vector그대로 사용했더니 효율성테스트를 통과하지 못해서 min-heap으로 구현하니까 바로 통과됐다. 근데 확실히 c++이 효율성테스트에서는 매우 빠르게 통과하는 것 같당

시간차이가 python이랑 엄청많이 난다

시간이 중요한 문제에서는 c++로 풀어야징~~
'''
  
#include <string>
#include <vector>
#include <queue>
using namespace std;
 
int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> q;
    for(int i=0;i<scoville.size();i++)
    {
        q.push(scoville[i]);
    }
    while(q.top()<K)
    {
        if(q.size()<=1)
        {
            return -1;
        }
        int first=q.top();
        q.pop();
        int second=q.top();
        q.pop();
        q.push(first+second*2);
        answer++;
    }
    return answer;
}
