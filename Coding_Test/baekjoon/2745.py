import math

def str_reverse(str):
    return str[::-1]

str, n = input().split()

n = int(n)

reverse_str = str_reverse(str)
print(reverse_str)

cnt = 0
result = 0
for i in reverse_str:
    if 65<=ord(i)<=90:
        temp = (ord(i) - 55)
        result+=(int)(temp * math.pow(n, cnt))
    else:
        result+=(int)(int(i) * math.pow(n, cnt))
    cnt+=1

print(result)