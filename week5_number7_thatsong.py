#week5 7번문제 [카카오] 방금그곡
#나중에 값 구하는 부분에서 못풀음 -> 좋은 풀이 참고


#m과 music 부분을 모두 한 문자로 변환(사용하지 않는)
#시간을 구해야지 musicinfo의 4번째 문자열의 길이를 늘일 수 있으니까 시간을 먼저 구함
#시간을 구하기 위해서 ,로 split한 후에 :를 기준으로 나눠서 시간을 구함
#해당 문자열을 dict type으로 key는 노래제목, value는 노래길이가 표현된 문자열로 저장
#현재 value에 있는 값의 길이가 answer[1]의 길이보다 길다면 값을 저장할 수 있음(문자열이 일치하는 게 있을 때는 길이가 더 긴게 우선순위가 크니까 교체가능)
#value값에 일치하는게 존재하면 해당 값을 answer에 저장함

#m과 value의 값이 일치하는게 존재하면 
def solution(m, musicinfos):
    dic = {}
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    for info in musicinfos:
    	#콤마를 기준으로 변수에 저장
        start, end, title, music = info.split(',')
        start = [int(i) for i in start.split(':')]
        end = [int(i) for i in end.split(':')]
        #끝난시각-시작시간을 분단위로 저장
        time = (end[0] - start[0]) *60 + (end[1] - start[1])
        music = music.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        #몫, 나머지를 이용해 실제로 재생된 멜로디 저장
        music = music * (time // len(music)) + music[:time % len(music) + 1]
        dic[title] = music
        
    answer = ["", ""]
    for key, value in dic.items():
        if m in value:
            if len(answer[1]) < len(value):
                answer[0] = key
                answer[1] = value
    
    return "(None)" if len(answer[0])==0 else answer[0]
