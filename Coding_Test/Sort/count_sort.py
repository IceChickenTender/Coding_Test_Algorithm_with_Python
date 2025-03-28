# 계수 정렬 예제

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

array_max = max(array)

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count_array = [0] * (array_max+1)

for i in range(len(array)):
    count_array[array[i]]+=1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count_array)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count_array[i]):
        print(i, end = " ") # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력