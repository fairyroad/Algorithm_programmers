'''
tank → kick → know → wheel → land → dream → mother → robot → tank
flag부분은 [0,0]을 판별하기 위한 변수인데 break가 되서 나간건지 아니면 그냥 iterate할 words가 남아있지 않아서 나간건지를 구별하기 위한 변수!! 
num은 차례를 계산하기 위한 변수 -> answer[0], answer[1]에 사용될 것!
dictionary는 이미 말했던 걸 다시 말하지 않는지를 체크하기 위한 list
0부터 len(words)-1까지 돌면서 num값을 1만큼 먼저 증가시켜 준다. 그리고 끝말잇기할때 이전의 나왔던거의 마지막 글자가 지금 말할 거의 첫번째 글자여야 되니까 그걸 확인하는게 16번째 줄!!
틀리다면 flag=1로 두고 break를 함
그리고 그 다음은 내가 지금 말할께 dictionary(이전 사람들이 말했던게 저장되어 있는 곳)에 담겨있는지를 보고 있었다면 탈락이니까 flag=1, break를 함
그런다음 answer[0], answer[1]이 있음
'''

import math
def solution(n, words):
    answer = [0,0]
    dictionary = []
    num=0
    flag=0
    for i in range(len(words)):
        num+=1
        if i != 0:
            if words[i-1][-1]!=words[i][0]:
                flag=1
                break;
        if words[i] in dictionary:
            flag=1
            break;
        dictionary.append(words[i])
    if flag==1:
        if num%n==0:
            answer[0]=n
        else:
            answer[0]=num%n
        answer[1]=math.ceil(num/n)
    return answer
