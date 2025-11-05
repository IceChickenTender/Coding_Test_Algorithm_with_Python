"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력1
3 16

예제 출력1
3
5
7
11
13

문제 해결 방법

해당 문제는 소수를 빨리 구하는 문제이므로 소수를 판별하는데 있어 가장 빠른 방법인 Miller-Rabin 소수판별법을 사용함

"""

import random

def is_prime(n, k=5) :

    # n 이 1보다 작거나 같으면 소수가 아니므로 False return
    if n <= 1:
        return False
    if n <= 3: # n 이 3보다 작거나 같으면 2와 3 밖에 없으니 소수이므로 True return
        return True
    if n % 2 == 0: # 3보다 큰 n 이 2로 나누어 떨어지면 소수가 아니므로 False return
        return False


    r, d = 0, n-1

    # 조건 검사를 위한 r와 d 를 구함
    while d % 2 == 0:
        d //= 2
        r += 1

    # 높은 신뢰도를 위해 k 번 실행 k의 값이 커질 수록 오류율이 1/4^k 만큼 줄어듦
    for _ in range(k):
        a = random.randrange(2, n-1) # 2~n-1 값 사이에 있는 랜덤 숫자를 선택
        x= pow(a, d, n) # a^d 를 구하고 그 값을 mod n 을 진행

        # x 가 1 이거나 n-1 이면 소수라고 보고 continue
        if x == 1 or x == n-1:
            continue

        # 위 조건에서 소수 판별이 되지 않으면 두 번째 조건 판별을 진행
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break

        else: # 위 두 조건 모두 만족하지 못하면 False return
            return False

    # k 번 반복하는 동안 return 하지 않으면 소수라고 판단하고 True return
    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if is_prime(i, 5):
        print(i)