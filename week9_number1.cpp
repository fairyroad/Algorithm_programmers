/*
첫번째 문제 : 단체사진 찍기

1.처음에는 factorial, combination다 구현하고 공식같은걸 만들어서 수학처럼 풀어보려고 했는데 너무 막막했당,,,

2.모든 종류들(순열)을 만들어낼 수 있는 next_permutation을 이용해서 조건에 맞는 것만 찾아서 count하쟈!!

9번째줄~20번째줄 위치를 계산하는 코드이다. 어차피 8개의 알파벳만 있다는 것을 알고있고 그럼 일치하는 알파벳의 위치를 알게되면 둘 사이의 거리를 계산할 수 있게 되기 때문이다. 1을 빼서 return하는 이유는 예를들어 2,3번째에 위치하게 되면 거리가 1이 아니라 0이기 때문이다.

23번째는 default로 세팅할 문자들을 적어 놓은 것이다. 나중에 next_permutation할 때 모든 경우의 수를 만들어낼 때 사용된다.

29번째의 distance는 check함수를 이용해서 거리를 계산했던 것을 말한다.

30번째줄은 =,>,<중에 어떤 기호를 사용했는지를 알 수 있는 코드이다.

31번째줄은 조건으로 주어진 거리가 얼마인지를 사용하는 것이고 char형으로 불려와지는데 우리는 int형으로 비교하길 원하기 때문에 -'0'을 이용해서 int값으로 저장한 것이다.

48번째의 result는 조건을 모두 통과하면 data.size()의 개수만큼이 더해지게 될 것이니까

51번째줄처럼 그 때만 answer를 1만큼 증가시켜서 결과에 포함되게 만들어주는 코드이다. 

*/

#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<char> name;
int check(char start, char end)
{
    int a,b;
    for(int i=0;i<8;i++)
    {
        if(name[i]==start)
            a=i;
        if(name[i]==end)
            b=i;
    }
    return abs(a-b)-1;
}
int solution(int n, vector<string> data) {
    int answer = 0;
    name={'A','C','F','J','M','N','R','T'};
    do
    {
        int result=0;
        for(int i=0;i<data.size();i++)
        {
            int distance=check(data[i].at(0),data[i].at(2));
            char condition=data[i].at(3);
            int num=data[i].at(4)-'0';
            
            if(condition=='=')
            {
                if(distance!=num)
                    break;
            }
            if(condition=='>')
            {
                if(distance<=num)
                    break;
            }
            if(condition=='<')
            {
                if(distance>=num)
                    break;
            }
            result++;
        }
        if(result==data.size())
            answer++;
    }while(next_permutation(name.begin(),name.end()));
    return answer;
}
