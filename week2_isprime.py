from itertools import permutations
#소수판별 코드
#time complexity줄이기 위해서 i*i <=numbers를 사용
def is_prime(numbers):
    i = 2
    if numbers == 1:
        return 0
    if numbers == 2 or numbers == 3:
        return 1
    while i * i <=numbers:
        if numbers % i == 0:
            return 0
        i+=1
    return 1
def solution(numbers):
    answer = 0
    possible_permutations = []
    real_permutations=[]
    #가능한 모든 조합을 만들어내는 코드
    #ex. 011 이라면 길이가 3이니까 1, 2, 3개를 뽑는 모든 순열을 만들어냄
    #map은 ' '형태로 지정된 형태로 바꿔주기 위해서 사용한 건데 '0' '1' '1'형태를 011로 바꿔서 저장하기 위해서 사용함
    #extend를 사용한 이유는 1 dimension형태로 사용하기 위함
    for len_numbers in range(1, len(numbers)+1):
        possible_permutations.extend(list(map(''.join, set(permutations(numbers,len_numbers)))))
    #011을 11처럼 바꿔주기 위해 lstrip을 사용함
    for remove_zero_permutations in possible_permutations:
        real_permutations.append(remove_zero_permutations.lstrip("0"))
    #중복되는거 제거하기 위해서 set 사용
    real_permutations = list(set(real_permutations))
    #''처럼 빈문자열이 아닐때만 소수판정을 할 수 있게 함
    #소수라면 answer값에 1씩 더해줌
    for num in real_permutations:
        if num != '' and is_prime(int(num)) == 1:
            answer+=1
    return answer
