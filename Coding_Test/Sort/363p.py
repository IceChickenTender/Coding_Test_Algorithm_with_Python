"""
https://www.acmicpc.net/problem/1715
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:

    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    sum_value = first+second
    result+=sum_value
    heapq.heappush(heap, sum_value)

print(result)