#못풀어서 좋은 풀이 참고함!!
#week5 4번째 문제 가장 큰 정사각형

#2~5번째줄은 2x2배열에서 오른쪽 아래에 존재하는 값이 1이상일 때 나머지 3칸의 최솟값을 파악해서 (0 또는 1로 나오게 될 것)
#만약 0이라면 그냥 똑같이 1이 될것이고 다 1이라면 2, 다 2라면 3이 될 수 있게 만들어주는 것이다. 
#dynamic programming을 이용해서 반복되는 것의 결과를 미리 저장해두는 방식이다.
#6번째 줄은 2차원배열일때 max값을 구해내는 방법이고 우리는 넓이를 구해야 하기 때문에 제곱을 해주었다.

def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]>=1:
                board[i][j]=min(board[i][j-1],board[i-1][j-1],board[i-1][j])+1
    return max(map(max,board))**2
