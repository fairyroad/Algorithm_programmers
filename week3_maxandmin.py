#s.split으로 공백을 구분하고
#최솟값과 최댓값을 저장함
def solution(s):
    no_space=[int(num) for num in s.split(' ')]
    answer=str(min(no_space))+' '+str(max(no_space))
    return answer
