"""
baekjoon 18870
"""

n = int(input())

arr = list(map(int, input().split()))

remove_dup_set = set(arr)

sorted_arr = list(remove_dup_set)

sorted_arr.sort()

result_dic = dict()

for i in range(len(sorted_arr)):
    result_dic[sorted_arr[i]] = i

for i in arr:
    print(result_dic.get(i), end=' ')