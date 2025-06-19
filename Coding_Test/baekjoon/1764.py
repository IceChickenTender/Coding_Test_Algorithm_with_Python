"""
baekjoon 1764
"""

n, m = map(int, input().split())

see_set = set()
hear_list = []

for i in range(n+m):
    string = input()
    if i < n:
        see_set.add(string)
    else:
        hear_list.append(string)


hear_list.sort()

cnt = 0
result_list = []
for i in hear_list:
    if i in see_set:
        cnt+=1
        result_list.append(i)

print(cnt)
for i in range(cnt):
    print(result_list[i])