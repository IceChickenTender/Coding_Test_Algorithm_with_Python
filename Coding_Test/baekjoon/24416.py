"""
baekjoon 24416
"""
import sys

def get_re_fino_cnt(dp):
    dp[5], dp[6] = 5, 8

    for i in range(7, 41):
        dp[i] = dp[i-1]+dp[i-2]


input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(41)]

get_re_fino_cnt(dp)

print(dp[n], n-2)