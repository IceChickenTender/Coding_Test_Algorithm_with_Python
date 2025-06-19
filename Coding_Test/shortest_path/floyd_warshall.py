"""
플로이드 워셜 알고리즘

입력 예시
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력 예시
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""
import sys

INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())

result_graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            result_graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    result_graph[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            result_graph[a][b] = min(result_graph[a][b], result_graph[a][k] + result_graph[k][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        print(result_graph[a][b], end = " ")
    print()























