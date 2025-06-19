"""
baekjoon 1620
"""

n, m = map(int, input().split())

num_to_pocket = dict()
pocket_to_num = dict()

solve_list = []

for i in range(n+m):
    string = input()
    if i < n:
        num_to_pocket[str(i+1)] = string
        pocket_to_num[string] = str(i+1)
    else:
        solve_list.append(string)

for i in solve_list:
    if i in num_to_pocket:
        print(num_to_pocket.get(i))
    if i in pocket_to_num:
        print(pocket_to_num.get(i))

