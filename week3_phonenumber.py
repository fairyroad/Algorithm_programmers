#전화번호를 dictionary에 저장
#tmp가 1,19,119이런식으로 되면서 prefix가 일치하는지 check
#일치한다면 false, 일치하지 않으면 true를 return함
def solution(phone_book):
    hash_map={}
    for phone_number in phone_book:
        hash_map[phone_number]=1
    for number in phone_book:
        tmp=""
        for num in number:
            tmp+=num
            if tmp in hash_map and tmp!=number:
                return False
    return True
