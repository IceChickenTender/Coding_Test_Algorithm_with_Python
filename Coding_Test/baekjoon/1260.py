"""
baekjoon 1260 문제 DFS 와 BFS

문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력1
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력1
1 2 4 3
1 2 3 4

예제 입력2
5 5 3
5 4
5 2
1 2
3 4
3 1

예제 출력2
3 1 2 5 4
3 1 4 2 5

예제 입력3
1000 1 1000
999 1000

예제 출력3
1000 999
1000 999
"""

import sys
from collections import deque


def solution(graph, start, vertex_num):
    """
    :param graph: 연결된 정점들을 모아 놓은 리스트
    :param start: 시작 정점
    :param vertex_num: 정점의 개수
    :return:
    """

    # DFS 함수
    def DFS(graph, visited, start):

        """

        :param graph: 인접한 정점들을 모아놓은 리스트
        :param visited: 방문한 정점을 체크하기 위한 리스트
        :param start: 시작 정점
        :return:
        """

        print(start, end=" ") # 우선 파라미터에 있는 start 를 바로 출력
        visited[start] = True # 방문한 정점을 체크하는 리스트에서 start 위치에 있는 정점을 방문 체크

        graph[start].sort() # 문제에서 크기가 작은 정점부터 가라고 했으니 정렬 진행

        for i in graph[start]: # start 정점과 인접한 정점들을 하나씩 가져옴
            if not visited[i]: # 인접한 정점들이 방문 체크가 되어 있지 않으면
                DFS(graph, visited, i) # DFS 함수 재귀 호출

    def BFS(graph, visited, start):

        """

        :param graph: 인접한 정점들을 모아놓은 리스트
        :param visited: 방문한 정점을 체크하기 위한 리스트
        :param start: 시작위치
        :return:
        """
        queue = deque([start]) # 시작위치 정점을 우선 큐에 넣어준다
        visited[start] = True # 그리고 방문 리스트의 시작 위치에 방문 체크를 해준다

        while queue:

            v = queue.popleft() # 큐에서 popleft 를 해준다
            print(v, end = " ") # 출력

            graph[v].sort() # 작은 정점들부터 방문해야 하므로 정렬 진행
            for i in graph[v]: # start 정점과 인접한 정점들을 하나씩 가져옴
                if not visited[i]: # 인접한 정점들 중에서 방문 체크가 되어 있지 않은 정점이 있다면
                    queue.append(i) # 큐에 넣어줌
                    visited[i] = True # 방문 체크 진행

    visited = [False] * (vertex_num+1) # 방문 체크 리스트 정의
    DFS(graph, visited, start)
    print()
    visited = [False] * (vertex_num+1) # 방문 체크 리스트 정의 재정의
    BFS(graph, visited, start)

input = sys.stdin.readline

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):

    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

solution(graph, start, n)