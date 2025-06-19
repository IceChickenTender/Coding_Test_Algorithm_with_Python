# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# time_list = []
# result_list = []
#
# for i in range(n):
#     start, end = map(int, input().split())
#     time_list.append((start, end))
#
# print(time_list)
#
# #time_list.sort(key=lambda x:(x[1],x[0]))
# sorted(time_list, key=lambda x:(x[1],x[0]))
#
# print(time_list)