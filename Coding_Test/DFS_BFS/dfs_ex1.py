from collections import deque


def bfs(visited, start, graph):
    queue = deque([start])

    while queue:
        pop_node = queue.popleft()
        if (visited[pop_node] == False):
            visited[pop_node] = True
            print(pop_node, end = ' ')
            for i in graph[pop_node]:
                queue.append(i)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(visited, 1, graph)


