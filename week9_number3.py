'''
세번째 문제 : 배달 

다익스트라 알고리즘으로 대부분 풀었음!! 

2가지 수정사항을 제외하고 다익스트라 알고리즘을 그대로 활용해 풀이했습니다. 

(1) 하나의 도로에서 양방향으로 이동 가능하므로, graph를 만들 때 양방향 정보를 모두 저장했습니다

(2) 마지막에 답을 구할 때 주어진 K 이하의 시간이 걸리는 마을의 개수를 세서 반환했습니다. 

https://mattlee.tistory.com/50

일반적인 다익스트라 알고리즘을 그대로 적용해서 풀면 됨

Dijkstra의 최단 경로 알고리즘은 네트워크에서 하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로를 찾는 알고리즘이다. 
최단 경로는 경로의 길이순으로 정해진다. Dijkstra의 알고리즘에서는 시작 정점에서 집합 S에 있는 정점만을 거쳐서 다른 정점으로 가는 최단 거리를 기록하는 배열이 반드시 있어야 한다. 
// 집합 S에는 최단 거리에 해당하는 정점이 하나씩 추가될 예정이다.

 최단 거리를 기록하는 1차원 배열을 하나 설정하고 이름을 distance로 한다. 
 시작 정점을 v라고 했을 때, distance[v] = 0 이고 다른 정점에 대한 distance 값은 시작 정점과 해당 정점 간의 가중치가 된다. 
 가중치는 인접 행렬에 저장되므로 가중치 인접 행렬을 weight라 했을 때 distacne[w] = weight[v][w] 과 같이 사용할 수 있다.

 단, 정점 v에서 정점 w로의 직접 간선이 없을 경우에는 무한대의 값을 저장한다. 시작 단계에서는 아직 최단 경로를 발견하지 못했으므로 S = { v } 와 같을 것이다. 
 즉 처음에는 시작 정점 v를 제외하고는 최단거리가 알려진 정점이 없다. 알고리즘이 진행되면서 최단 거리가 발견되는 정점들이 S에 하나씩 추가될 것이다.

 알고리즘의 매 단계에서 집합 S 안에 있지 않은 정점 중에서 가장 distance 값이 작은 정점을 S에 추가한다. 
 새로운 정점 u가 S에 추가되면, S에 있지 않은 다른 정점들의 distance 값을 수정한다. 
 시작 기준점이 u로 바뀌었기 때문에, 새로 추가된 정점 u를 거쳐서 정점까지 가는 거리와 기존의 거리를 비교한다. 
 그 후 더 작은 거리값을 기준으로 distance값을 수정한다. 아래와 같은 수식을 이용하면 될 것이다.

 distance[w] = min(distance[w], distance[u] + weight[u][w]) // min은 stdlib.h에 선언되어 있는 매크로다. 매개 변수로 들어온 두 값중 더 작은 값을 리턴한다.

  아래의 예제 그래프를 통해 Dijkstra 알고리즘이 어떻게 진행되는지, 그리고 집합 S와 distance 배열은 어떻게 값이 바뀌어가는지 그 과정을 살펴보자. 
  시작 정점을 0으로 잡았다고 생각하고 흐름을 따라가 보자.

'''
import heapq

def solution(N, road, K):
    INF = int(1e9)
    #그래프 2차원 배열 만들기 위해서...
    graph = [[] for _ in range(N+1)]
    #쓰레기값으로 채우기(가장 클 수 있는 값)
    distance = [INF] * (N+1)
    
    # 간선 정보 저장하기
    # (1,4,1)이런 느낌으로 r 이 들어가니까
    for r in road:
        a, b, c = r
        # 양방향
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    # 다익스트라 알고리즘 
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        
        while q:
            # 최단거리 노드
            dist, now = heapq.heappop(q)
            # 이미 방문했거나 최솟값이 아닌 경우 
            if distance[now] < dist:
                continue 
            # 연결된 노드들에 대해 
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 정보보다 더 적은 시간이 필요한 경우 갱신
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    dijkstra(start=1)
    
    # K 이하의 시간에 배달이 가능한 마을의 개수 
    return len([d for d in distance if d <= K])
