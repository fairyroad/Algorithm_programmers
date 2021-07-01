#프로그래머스 풀이 참고함!!

#주어진 조건에 1000이하이므로 3번 반복하는 함수를 사용
#2번째 줄은 각각의 numbers를 str로 바꿔주는 역할을 함
#3번째줄은 예를들어 1,10,8이 있으면 111,101010,888처럼 같은문자를 3번 반복하게 만들어주는 역할을 함 
#reverse=True로 한 이유는 내림차순으로 정렬하기 위해서이고 문자열은 ascii코드값으로 바꿔서 인덱스를 비교하게 됨!!
#4번째줄에 int로 바꾸고 str한 이유는 0000처럼 나왔을 때 0으로 바꿔주고 다시 문자열로 출력해주기 위해서임

def solution(numbers):
    number = list(map(str, numbers)) 
    number.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(number)))
