'''
4번문제: 오픈채팅방

이번문제는 엄청 쉬웠음
하라는 대로 하면됨
처음에 Enter들어오면 dict type으로 user id랑 닉네임을 함께 저장해둠
dict type을 사용하면 값이 변경될 때 알아서 변경해주고 추가해야될때 알아서 추가해줘서 이걸 사용함
update가 다 되면 이번에는 출력을 위해서 다시 한번 돌아서
Enter이면 uid의 data의 value를 찾아서 ~님이 들어왔습니다!!!
해주고, Leave면 나갔습니다~~!!해주면 됨!!
'''
def solution(record):
    answer = []
    data = {}
    for rec in record:
        rec = rec.split(' ')
        if rec[0] == 'Enter' or rec[0] == 'Change':
            data[rec[1]] = rec[2]
    for rec in record:
        rec = rec.split(' ')
        if rec[0] == 'Enter':
            answer.append(data[rec[1]]+"님이 "+"들어왔습니다.")
        elif rec[0] == 'Leave':
            answer.append(data[rec[1]]+"님이 "+"나갔습니다.")
    return answer
  
  '''
  좋은 풀이
  
  다 똑같은데 미리 Enter, Leave값을 dict type으로 두고 불러오는게 좀 신기한 풀이인것 같음
  '''
  def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
