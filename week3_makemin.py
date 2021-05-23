#전체배열의 합이 최솟값이 되려면 작은것과 큰것을 곱하면 됨
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer=[A[i]*B[i] for i in range(len(A))]
    return sum(answer)
