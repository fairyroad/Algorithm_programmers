#week5 8번문제 [카카오] 캐쉬


#LRU방식 -> queue처럼 FIFO느낌으로 구현
#hit이랑 miss일때로 구분함
#hit이라는 의미는 해당 city가 cache에 존재한다는 거니까 answer값을 1만큼만 증가시키고 이미 존재하는 index에서 pop을 시킨후 다시 맨뒤에 넣어줌
#miss일때는 cache가 full일때와 cache에 자리가 남아있을때로 구분할 수 있는데 먼저 두가지 경우 모두 answer값은 5만큼 증가시키고
#full이라면 기존에 있는 것중에 제일 처음것(index가 0인것)을 pop시키고 해당 도시를 push해주고
#자리가 남아있다면 그냥 바로 push해주는 방식으로 구현함

#----------------------------내가 구현한 방법--------------------------------
def solution(cacheSize, cities):
    answer = 0
    queue = []
    num = 0
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city not in queue:
            answer+=5
            if num < cacheSize:
                queue.append(city)
                num+=1
            else:
                if len(queue) > 0:
                    queue.pop(0)
                else:
                    num+=1
                queue.append(city)
        else:
            answer+=1
            queue.pop(queue.index(city))
            queue.append(city)      
    return answer

#--------------------------좋은 풀이------------------------------
#collections.deque()는 순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템 유지하고 싶을 때 사용한다고 함 -> 우리문제에 적합함
#deque를 이용하는데 maxlen을 설정할 수 있음!!
#만약 cache에 존재하면 우선순위를 바꿔줘야하니까 지우고 다시 append시켜주고(내가 한 방법이랑 같음)
#만약 cache에 존재하지 않는다면 바로 append시켜주면 됨
#기존에 내 방식을 이용하면 크기에 따라 4가지 경우로 분리해야한다는 단점이 있었는데 collections.dequeue를 이용하게 되면 자동으로 최신것만 maxlen만큼 유지해주니까 삭제하지 않아도 된다는 장점이 있음
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
