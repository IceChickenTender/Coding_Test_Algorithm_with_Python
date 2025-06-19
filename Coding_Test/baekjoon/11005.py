"""
baekjoon 1105
"""

n, m = map(int, input().split())

result = []

while n>=m:
    a = n % m
    if 10<=a<=35:
        result.append(chr(a+55))
    else:
        result.append(a)
    n = (int)(n/m)

if 10<= n <= 35:
    result.append(chr(n+55))
else:
    result.append(n)

for i in range(len(result)-1, -1, -1):
    print(result[i], end='')



