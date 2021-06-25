#두번째문제_땅따먹기
#동적계획법 사용
#이 문제 풀이의 핵심은 차례로 같은 열을 제외한 것들중의 max값을 미리 저장해두는 방법을 사용한다는 것
#예를 들어 첫번째 row에 [1,2,3,4], 두번째 row에 [5,6,7,8]이 존재하면 두번째 row의 값을 [9,10,11,11] 로 바꿔주는 것이다. 
#그럼 마지막줄의 최댓값이 이 문제의 답이 됨!!

그렇게 하면 맨 마지막 줄의 max값만 찾아내면 바로 답
def solution(land):
    answer = 0
    for i in range(0,len(land)-1):
        for j in range(len(land[0])):
            land[i+1][j]+=max(land[i][:j]+land[i][j+1:])
    return max(land[len(land)-1])
