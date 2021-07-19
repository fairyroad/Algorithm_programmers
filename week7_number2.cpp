/*
(winter 코딩)스킬트리문제
- answer은 몇개인지 결과를 알려주는 변수
- skill을 vector에 담기위해서 하나씩 push함
- test부분의 함수는 0, 1, 2로 구분을 했는데 0은 순서가 틀렸을때를 의미함
1은 순서가 맞았을 때, 2는 예외사항(0일때 아니면 2나올일 없음)
-vector check부분은 중간에 erase하는 부분이 있어서 pop시킬때 data가 손실이 발생할 수 있어서 복제해두는 변수
-test부분에서 0이 나오면 바로 break를 하고(어차피 답에 포함이 안되니까 더이상 볼 필요없음), 1이 나오면
vector에 있는 걸 하나 pop시킴(순서가 어차피 맞으니까 제일 앞에 있는 걸 pop시키면 됨)
-이렇게 반복하다가 skill_trees의 length랑 num이 같아졌을 때 answer를 return해주면 됨
*/
#include <string>
#include <vector>

using namespace std;

int test(vector<char>a, int i, int j,vector<string>skill_trees)
    {
            for(int z=0;z<a.size();z++)
            {
                if(a[z]==skill_trees[i][j])
                {
                    if(z!=0)
                        return 0;
                    return 1;
                }
            }
        return 2;
    }

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    vector<char> check;
    for(int i=0;i<skill.length();i++)
        check.push_back(skill[i]);
    for(int i=0;i<skill_trees.size();i++)
    {
        vector<char> a=check;
        int num=0;
        for(int j=0;j<skill_trees[i].length();j++)
        {
            int b=test(a,i,j,skill_trees);
            if(b==0)
            {
                break;
            }
            else if(b==1)
            {
                a.erase(a.begin()+0);
            }
            num++;
        }
        if(num==skill_trees[i].length())
            answer++;
    }
    return answer;
}
