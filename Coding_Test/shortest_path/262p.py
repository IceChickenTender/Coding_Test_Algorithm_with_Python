"""
최장거리 문제

전보

어떤 나라에는 N개의 도시가 이싿. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시 로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X 라는 도시에서 Y 라는 도시로 전보를 보내고자 한다면, 도시 X 에서 Y 로 향하는 통로가 설치되어 있어야 한다. 예를 들어 X 에서 Y 로 향하는 통로는 있지만
Y 에서 X 로 향하는 통로가 없다면 Y 는 X 로 메시지를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

어느날 C 라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다. 메시지는 도시 C 에서 출발하여 각 도시 사이에 설치된 통로를 거쳐,
최대한 많이 퍼져나갈 것이다. 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C 에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이
모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오

입력 조건
- 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
  (1<=N<=30,000, 1<=M<=200,000, 1<=C<=N)
- 둘째 줄부터 (M+1) 번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z 가 주어진다. 이는 특정 도시 X 에서 다른 특정 도시 Y 로 이어지는 통로가 있으며, 메시지가 전달
  되는 시간이 Z 라는 의미이다.
  (1<=X, Y<=N, 1<=Z<=1,000)

출력 조건
첫째 줄에 도시 C 에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.

입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
"""
import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0

max_distance = 0

for i in distance:
    if i == INF:
        continue
    else:
        cnt+=1
        max_distance = max(max_distance, i)

print((cnt-1), max_distance)











