#문제 설명
#두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
#예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
#n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# lcm(a, b)= a * b / gcd(a, b) 사용
from fractions import gcd
def solution(arr):
  #2개이상이 아직 arr에 존재한다면 최소공배수를 계산해야함
    while len(arr)>1:
        a,b=arr.pop(),arr.pop()
        arr.append(a*b//gcd(a,b))
    #마지막 하나남았을 때 while문이 종료되므로
    #제일 첫번쨰 원소가 전체 arr의 lcm이 됨
    return arr[0]
