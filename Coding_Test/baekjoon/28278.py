"""
baekjoon 28278
"""
import sys

input = sys.stdin.readline

n = int(input())

stack = []

command_list = []

for i in range(n):
    string = input().rstrip()
    command_list.append(string)


for i in command_list:

    if i.startswith("1"):
        num = int(i.split()[1])
        stack.append(num)
    elif i == "2":
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif i == "3":
        print(len(stack))
    elif i == "4":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif i == "5":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)



