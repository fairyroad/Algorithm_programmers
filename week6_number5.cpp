/*
5번문제 : [카카오] 컬러링북

이 문제는 BFS를 사용해서 풀어야 하는 문제이다.

 

1.west, east, north,south 순서로 배열을 지정하는데 나중에 주변에 있는 곳으로 옮겨가며 탐색하기 위한 배열이다. 

int ax[4]={-1,1,0,0};

int ay[4]={0,0,-1,1};

 
2.이 문제를 풀때 헷갈렸던게 m,n이 가로인지 세로인지, for문을 돌릴때 뭘 먼저 해야 하는거지?? 이런 의문점이 있었다.

m이 세로이고 n이 가로인데 우리는 x값,y값을 생각해줄꺼니까 m이 y값들, n이 x값들의 후보라고 생각하면 편하다.

for문을 돌릴때 m을 먼저하고 n을 해도 되고 반대로 해도 되는데 나중에 pictures[i][j]를 할 때 i가 y값이고 j가 x값이라는 것은 꼬옥 기억해 두어야 한다.


3.BFS는 queue를 사용하게 되는데 visited를 꼭 써서 방문한 곳을 체크 할 필요가 있다. 나는 queue를 pair형태로 묶어서 x,y값을 모두 하나의 queue에 저장하려고 한다.
*/

#include <vector>
#include <queue>
using namespace std;
 
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int ax[4] = { -1,1,0,0 };
int ay[4] = { 0,0,-1,1 };
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;//영역의 개수
    int max_size_of_one_area = 0;//영역의 최대 넓이
    bool visited[101][101] = { 0, };//방문했던 곳을 표시하기 위한 variable
    queue<pair<int, int>> q;
 
    for (int j = 0; j < picture.size(); j++)//m이 세로의 길이
    {
        for (int i = 0; i < picture[j].size(); i++)//n이 가로의 길이
        {
            int area = 0;//영역의 넓이를 계산할 variable
            if (picture[j][i] != 0 && !visited[i][j])
            {
                q.push({ i,j });
                number_of_area++;
                area++;
                visited[i][j] = true;
            }
            while (!q.empty())
            {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();
 
                for (int z = 0; z < 4; z++)
                {
                    int xx = x + ax[z];
                    int yy = y + ay[z];
                    if (xx < 0 || xx >= n || yy < 0 || yy >= m)
                        continue;
                    if (picture[yy][xx] == picture[y][x] && !visited[xx][yy])
                    {
                        area++;
                        q.push({ xx,yy });
                        visited[xx][yy] = true;
                    }
                }
            }
            if (area > max_size_of_one_area)
                max_size_of_one_area = area;
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
