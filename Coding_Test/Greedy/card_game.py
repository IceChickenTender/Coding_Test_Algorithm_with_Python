"""
case1

input
3 3
3 1 2
4 1 4
2 2 2

output
2
"""

"""
case2

input
2 4
7 3 1 8
3 3 3 4

output
3
"""

n, m = map(int, input().split())

result_list = []

for i in range(n):
    input_list = list(map(int, input().split()))
    min_value = min(input_list)
    result_list.append(min_value)

print(max(result_list))