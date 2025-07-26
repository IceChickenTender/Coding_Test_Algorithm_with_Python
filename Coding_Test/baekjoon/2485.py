"""
문제
직선으로 되어있는 도로의 한 편에 가로수가 임의의 간격으로 심어져있다. KOI 시에서는 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진하고 있다. KOI 시에서는 예산문제로 가능한 한 가장 적은 수의 나무를 심고 싶다.

편의상 가로수의 위치는 기준점으로 부터 떨어져 있는 거리로 표현되며, 가로수의 위치는 모두 양의 정수이다.

예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다. 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하라. 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.

입력
첫째 줄에는 이미 심어져 있는 가로수의 수를 나타내는 하나의 정수 N이 주어진다(3 ≤ N ≤ 100,000). 둘째 줄부터 N개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수로 주어지며, 가로수의 위치를 나타내는 정수는 1,000,000,000 이하이다. 가로수의 위치를 나타내는 정수는 모두 다르고, N개의 가로수는 기준점으로부터 떨어진 거리가 가까운 순서대로 주어진다.

출력
모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 첫 번째 줄에 출력한다.

예제 입력 1
4
1
3
7
13

예제 출력 1
3

문제 풀이 방법

1. 가로수 사이의 거리들 값에 대한 최대 공약수를 구한다.
2. 가로수 사이의 거리들 값에 구한 최대 공약수로 나누어주고 그 몫에 -1 을 한 값을 모두 더해준다
-1을 해주는 이유는 예를 들어 구한 최대공약수의 값이 2라면 가로수 사이의 거리가 2가 되어야 함 이럴 경우 `4`, `8` 위치에 심어져 있는 가로수 사이에는 `6` 이라는 위치에
가로수가 하나 심어져야 함 즉 4와 8 의 거리는 4 이고 이를 최대공약수인 2로 나누어 주면 2가 되게 됨 우리가 구해야 하는 것은 이 사이에 심어져야 할 가로수의 수 이므로 -1을 해줌

"""
import sys
import math

def multiple_gcd(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
    return result

n = int(input())

trees_position_list = []

trees_gap_list = []

for _ in range(n):
    tree_position = int(sys.stdin.readline().rstrip())
    trees_position_list.append(tree_position)

for i in range(len(trees_position_list)-1):
    gap = trees_position_list[i+1] - trees_position_list[i]
    trees_gap_list.append(gap)

gcd = multiple_gcd(trees_gap_list)

cnt = 0

for i in trees_gap_list:
    cnt += i // gcd - 1

print(cnt)