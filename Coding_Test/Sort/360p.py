"""
https://www.acmicpc.net/problem/18310
"""
import sys

input = sys.stdin.readline

n = int(input())

house_position_list = list(map(int, input().split()))

house_position_list.sort()

print(house_position_list[(n-1)//2])