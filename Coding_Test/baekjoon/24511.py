"""
baekjoon 24511
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue_stack_list = list(map(int, input().split()))

init_list = list(map(int, input().split()))

m = int(input())

insert_list = list(map(int, input().split()))

queue_list = []

for i in range((n-1), -1, -1):
    if queue_stack_list[i] == 0:
        queue_list.append(init_list[i])

result_queue = deque(queue_list)

for i in insert_list:

    if len(result_queue) > 0:
        print(result_queue.popleft(), end = " ")
        result_queue.append(i)
    else:
        print(i, end = " ")