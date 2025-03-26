# 삽입 정렬 예제

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 1번째 인덱스 부터 리스트 마지막 인덱스까지 반복

    """
    인덱스 i부터 1까지 하나씩 감소하는 반복문 
    i부터 1까지만 역으로 감소하게 한 이유는 아래 조건문에서 j에 -1을 해주기 때문에 조건문 연산 시 0번째 인덱스도 확인하기 때문
    """
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # j와 j-1 번째의 값을 비교한 후 j 인덱스에 있는 값이 더 작을 경우 바꿔줌
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

