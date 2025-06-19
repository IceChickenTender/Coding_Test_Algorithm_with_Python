total_price1 = int(input())
total_num = int(input())

total_price2 = 0

for i in range(total_num):
    price, num = map(int, input().split())
    total_price2 += (price * num)

if total_price1 == total_price2:
    print("Yes")
else:
    print("No")


