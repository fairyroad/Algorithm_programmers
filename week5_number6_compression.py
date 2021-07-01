#week5 6번문제 [카카오] 압축문제
#----------------------------다른 사람 풀이-----------------------
#규칙성 존재 
#1)현재글자 + 다음글자가 사전에 없다면 w = c , c = c + 1
#2)현재글자 + 다음글자가 사전에 있다면 w는 변화없음, c = c + 1
#KAKAO
#현재 다음 -> w c
#K    A  -> 0 1
#A    K  -> 1 2
#K    A  -> 2 3
#KA   O  -> 2 4
#O       -> 4 5

#c가 마지막 인덱스 번호라면, while문을 빠져나가게!!

#w, c의 규칙 -> index를 append함
def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer
