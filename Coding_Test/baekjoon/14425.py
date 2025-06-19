"""
baekjoon 14425
"""

n, m = map(int, input().split())

str_set = set()

for i in range(n):
    string = input()
    str_set.add(string)

cnt = 0
for i in range(m):
    string = input()
    if string in str_set:
        cnt+=1

print(cnt)
