"""
baekjoon 2587
"""

arr = []

average = 0
sum = 0

for i in range(5):
    num = int(input())
    sum+=num
    arr.append(num)
arr.sort()

average = (int)(sum/5)
print(average)
print(arr[2])