/*
1번 : 멀쩡한 사각형

규칙이 있는 것 같아서 일일이 세보다가 아래와 같은 규칙을 발견함
그래서 썼는데 단위에 따라서 답이 오류가 나는게 존재해서 일부러 long long 이런걸 붙여줌... 원래는 안붙였음
그림을 보면 10.5처럼 정수로 걸친건 빼버림 따라서 그래프에서 정수로 떨어지는 아이만 더해주면 됨
일차함수 이용한 공식!!
그랬더니 통과가 됨!!
*/

#include <iostream>
#include <cmath>
using namespace std;

long long solution(int w,int h) {
    long long answer = 0;
    for(int i=1;i<w;i++)
        answer+=(long long)((long double)(-h/(long double)w)*i+h);
    return answer*2;
}
