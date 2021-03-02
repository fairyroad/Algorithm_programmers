def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer=[A[i]*B[i] for i in range(len(A))]
    return sum(answer)

print(solution([1,2,4],[4,4,5]))