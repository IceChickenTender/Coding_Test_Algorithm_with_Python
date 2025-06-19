"""
baekjoon 10815
"""

n = int(input())
num_set = set(map(int, input().split()))

m = int(input())
find_num_list = list(map(int, input().split()))

for i in find_num_list:
    if i in num_set:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
