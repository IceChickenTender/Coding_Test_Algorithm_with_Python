"""
259 페이지 미래 도시

입력 예시1

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력 예시1
3

입력 예시2
4 2
1 3
2 4
3 4

출력 예시2
-1
"""
import sys

INF = int(1e9)

input = sys.stdin.readline

n, m = map(int, input().split())

result_graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            result_graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    result_graph[a][b] = 1
    result_graph[b][a] = 1

x, k = map(int, input().split())

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            result_graph[a][b] = min(result_graph[a][b], result_graph[a][c] + result_graph[c][b])

result = result_graph[1][k] + result_graph[k][x]

print(result)


