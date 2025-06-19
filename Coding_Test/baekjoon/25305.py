"""
baekjoon 25305
"""

import collections

n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(arr[k-1])

