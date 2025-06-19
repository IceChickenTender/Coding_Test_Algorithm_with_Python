"""
baekjoon 9184
"""
import sys

# 동적 프로그래밍으로 계산하는 함수
def run(dp):
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):

                if i < j and j < k: # 첫 번재 인자가 두 번째 인자 보다 작고, 두 번째 인자가 세 번째 인자보다 작을 때 아래 계산을 수행
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else: # 그 외의 케이스는 아래 계산을 수행
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]


# 값을 저장할 3차원 리스트로 dp 리스트 생성
dp = [[[0 for col in range(21)] for row in range(21)] for depth in range(21)]

# dp 리스트에서 0이 들어간 원소들은 모두 1의 값을 가지므로 0이 있는 모든 곳에는 1로 업데이트 즉 초기값 업데이트
for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i == 0 or j == 0 or k == 0:
                dp[i][j][k] = 1

dp[1][1][1] = 0

# 함수 실행
run(dp)

# 입력을 받아올 리스트
input_list = []

# 입력을 받아옴
while True:
    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    # a, b, c 값이 모두 -1 이면 조건문 종료
    if a == -1 and b == -1 and c == -1:
        break

    # input_list 에 세 가지 값을 튜플로 하여 저장
    input_list.append((a, b, c))

for i in input_list:
    a, b, c = i[0], i[1], i[2]

    # a, b, c 세 가지 값 중 하나라도 0이면 1을 출력하도록 함
    if a <= 0 or b <= 0 or c <= 0:
        print("w(%d, %d, %d) = %d" % (i[0], i[1], i[2], 1))
        continue

    # a, b, c 값 중 하나라도 20보다 크면 dp[20][20][20] 을 출력하도록 함
    if a > 20 or b > 20 or c > 20:
        print("w(%d, %d, %d) = %d" % ( i[0], i[1], i[2], dp[20][20][20]))
        continue

    # 위 두 조건에 해당하지 않으면 그대로 출력
    print("w(%d, %d, %d) = %d" % (i[0], i[1], i[2], dp[a][b][c]))
