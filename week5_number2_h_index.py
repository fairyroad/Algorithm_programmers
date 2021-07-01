#week5 2번째 문제 h-index
#문제에서 주어진 대로 h-index의 최댓값을 찾기 위해 범위를 max(citations)까지로 한정지었다. 
#0부터 차례로 citations의 max값까지 하나씩 값을 1씩 증가시키면서 big값을 바꾸게 된다.
#조건에 맞는 big값중에 최댓값을 저장하게 된다.(이미 정렬된 상태이니까)


def solution(citations):
    citations.sort()
    for i in range(0, max(citations) + 1):
        num = 0
        for j in citations:
            if i <= j:
                num=num+1
        if i<= num:
            big = i
    return big
