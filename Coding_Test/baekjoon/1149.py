"""
baekjoon 1149
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]*3 for _ in range(n)]

input_rgb_list = []

for i in range(n):
    rgb_list = list(map(int, input().split()))
    input_rgb_list.append(rgb_list)

for i in range(0,3):
    dp[0][i] = input_rgb_list[0][i]

for i in range(1, n):
    for j in range(0, 3):

        min_value = 1000*1000

        for k in range(0, 3):
            if j == k:
                continue

            if dp[i-1][k] < min_value:
                min_value = dp[i-1][k]
            dp[i][j] = min_value + input_rgb_list[i][j]

print(min(dp[n-1]))