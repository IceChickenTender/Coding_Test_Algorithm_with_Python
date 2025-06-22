# 선택 정렬 예제 코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):

    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # i 인덱스 이후의 값 들 중에서 i 보다 작은 것이 있다면 min_index 변경
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 값 변경

print(array)
