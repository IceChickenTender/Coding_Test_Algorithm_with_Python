"""
baekjoon 2903
"""

n = int(input())

result = 3

for i in range(1, n):
    result+=(int)(pow(2, i))

print(pow(result, 2))