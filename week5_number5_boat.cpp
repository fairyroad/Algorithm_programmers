//week5 5번째문제 구명보트

//처음에는 그냥 정렬해놓고 양옆에 있는 것만 확인하려고 했는데 testcase에서 실패,,,,
//생각해보니까 제일작은거랑 제일 큰거 비교해야함!! 

//무게를 작은 것부터 큰 사람까지 정렬해놓고 
//만약 limit보다 작아서 두명 모두를 한 보트에 태울 수 있다면 i도 이동해주고 j도 한칸앞으로 이동해주게 되는것이다.
//만약 limit보다 크다면 j만 하나 줄이게 된다. 즉, j만 보트에 태우게 되는 것!!


#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());
    int i=0,j=people.size()-1;
    while(i<=j)
    {
        answer++;
        if(people[i]+people[j]<=limit)
        {
            i++;
        }
        j--;
    }
    return answer;
}
