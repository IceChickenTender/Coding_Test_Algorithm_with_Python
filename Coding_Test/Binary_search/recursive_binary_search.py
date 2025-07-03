"""
10 7
1 3 5 7 9 11 13 15 17 19
4
"""

import sys

#이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)





