"""
DFS 예제

1->2->7->6->8->3->4->5 로 출력되는 그래프를 예제로 함
본 코드에서는 각 노드를 배열의 인덱스에 맞추기 위해 1을 빼준 것이 아닌 노드 번호 그대로를 사용
그렇기 때문에 노드가 8개 임에도 불구하고 사용된 배열들의 크기가 9로 사용
"""

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리하고 출력
    visited[v] = True
    print(v, end = ' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
