"""
baekjoon 7785
"""

n = int(input())

enter_set = set()

for i in range(n):
    name, judge = input().split()
    if judge == "enter":
        enter_set.add(name)
    elif judge == "leave":
        enter_set.remove(name)

result_list = list(enter_set)
result_list.sort(reverse=True)

for i in result_list:
    print(i)

