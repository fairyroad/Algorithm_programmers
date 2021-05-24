#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
int find_max(queue<int> priority)
{
    int max = priority.front();
    while(priority.size())
    {
        priority.pop();
        if(max < priority.front())
            max = priority.front();
    }
    return max;
}
int solution(vector<int> priorities, int location) 
{
    int answer = 0;
    queue<int> q;
    queue<int> priority;
    int num,loc;
    //q에 priority넣음
    for(int i=0;i<priorities.size();i++)
    {
        priority.push(priorities[i]);
        q.push(i);
    }
    while(priority.size())
    {
        num = priority.front();
        priority.pop();
        loc = q.front();
        q.pop();
        if(num < find_max(priority))
        {
            priority.push(num);
            q.push(loc);
        }
        else
        {
            answer++;
            if(loc == location)
                return answer;
        }
    }
    return answer;
}
