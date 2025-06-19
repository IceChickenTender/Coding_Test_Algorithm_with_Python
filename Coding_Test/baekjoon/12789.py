"""
baekjoon 12789
"""
import sys

input = sys.stdin.readline

n = int(input())

wait_list = list(map(int, input().split()))

judge = True

stack = []

out = []

current_order = 1

for i in wait_list:
    if i == current_order:
        out.append(i)
        current_order+=1
    else:
        if len(stack) > 0:
            while stack:
                if stack[-1] == current_order:
                    out.append(stack[-1])
                    stack.pop()
                    current_order+=1
                else:
                    break
            stack.append(i)
        else:
            stack.append(i)

while stack:
    out.append(stack[-1])
    stack.pop()

sorted_out = list(out)
sorted_out.sort()

for i in range(len(out)):
    if out[i] != sorted_out[i]:
        judge = False
        break

if judge:
    print("Nice")
else:
    print("Sad")

