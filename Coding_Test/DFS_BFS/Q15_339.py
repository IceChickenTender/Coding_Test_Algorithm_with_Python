"""
어떤 나라에는 1 ~ N 번까지의 도시와 M 개의 단방향 도로가 존재합니다. 모든 도로의 거리는 1입니다. 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시
중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요. 또한 출발 도시 X 에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정합니다.
예를 들어 N = 4, K = 2, X = 1 일 때 다음과 같이 그래프가 구성되어 있다고 합시다.

1 2
1 3
2 3
2 4

이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시뿐입니다. 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않습니다.

입력 예시1
4 4 2 1
1 2
1 3
2 3
2 4

"""
from collections import deque

n, m, k, x = map(int, input().split())

graph = []
visited = [False] * (n+1)
count_list = [0] * (n+1)

for i in range(n+1):
    graph.append([])

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    cnt = 1
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                count_list[i] = cnt
                queue.append(i)
                visited[i] = True
        cnt+=1

bfs(graph, x, visited)

print(graph)

for i in range(len(count_list)):
    if count_list[i] == k:
        print(i)