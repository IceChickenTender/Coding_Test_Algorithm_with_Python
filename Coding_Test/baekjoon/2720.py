"""
baekjoon 2720
"""

quarter = 25
dime = 10
nickel = 5
penny = 1

quarter_cnt = 0
dime_cnt = 0
nickel_cnt = 0
penny_cnt = 0

n = int(input())

arr = []

for i in range(n):
    money = int(input())
    arr.append(money)

for i in range(n):

    money = arr[i]
    quarter_cnt = int(money/quarter)
    money = money % quarter

    dime_cnt = int(money/dime)
    money = money % dime

    nickel_cnt = int(money/nickel)
    money = money % nickel

    penny_cnt = int(money/penny)

    print(quarter_cnt, dime_cnt, nickel_cnt, penny_cnt, end = ' ')
    print()
