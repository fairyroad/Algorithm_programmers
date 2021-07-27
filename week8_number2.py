'''
2번문제 : 점프와 순간이동

처음에 여러시도 해보다가 규칙을 찾음
2로 나누어떨어지지 않을 때까지 계속 2로 나눠주고 
만약 2로 나누어떨어지지 않는 부분이 존재하면 ans값을 1올리고 n값을 1만큼 낮추면서 
다시 반복해서 n이 0이 될때까지 반복하는 방법으로 문제를 풀었음
예를 들어서 5면 5는 나누어 떨어지지 않으니까 ans = 1, n=4가 된다음에 2로 계속 나누면 n이 1이 됨!!
이때 다시 나누어 떨어지지 않는 수가 나왔으니까 ans = 2, n = 0이 되면서 while 문을 빠져나오게 되고 2를 return하게 되는 방법으로 문제를 풀었음
'''

def make_prior(num):
    while num % 2 == 0:
        num = num // 2
    return num
def solution(n):
    ans = 0
    num = n
    while num > 0:
        num = make_prior(num)
        if num %2 != 0:
            ans += 1
            num -=1 
    return ans
