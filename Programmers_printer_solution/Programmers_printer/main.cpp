/*programmers level2 printer*/

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    queue<pair<int, int>> que;
    priority_queue<int> pque;
//priority queue, queue를 만들어서 vector값을 push시킴
    for (int i = 0; i < priorities.size(); i++) {
        //처음을 index번호, 두번째를 중요도로 넣음
        que.push(make_pair(i, priorities[i]));
        pque.push(priorities[i]);
    }

    while (!que.empty()) {
        //그냥 queue에서 하나씩 pop시켜서 priorityqueue의 pop시킨 값과 중요도가 같은지 확인
        //중요도가 같더라도 내가 알고싶은 location인지를 check해야하기 때문에 그냥 queue도 이용하는것!!
        if (que.front().second == pque.top()) {
            if (que.front().first == location) {
                return answer + 1;
            }
            else {
                answer++;
                que.pop(); pque.pop();
            }
        }
        else {
            que.push(que.front());
            que.pop();
        }
    }
    return answer;
}