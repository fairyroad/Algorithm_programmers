#4번째 문제_n진수 게임
#자기차례가 돌아오는 건 i % m == p-1번째 일때
#돌아올때마다 k의 값을 1만큼씩 증가시켜서 만약에 t의 값과 같아지면 끝낼수있게함
#convert는 n진수로 바꿔주는 함수
#몇번째까지 구해야되는지를 생각하지 않게 그냥 숫자(i)를 다 진수로 바꿔서 일단 저장해두게 했음
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
      
def solution(n, t, m, p):
    answer = ''
    s = ""
    i = 0
    k = 0
    while k < t:
        s+=convert(i, n)
        if i%m == p-1:
            answer+=s[i]
            k+=1
        i+=1
    return answer
