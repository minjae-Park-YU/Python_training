n, m = map(int, input().split())
array = []

# 처음 풀었을 때
# min_value = -99
# min_idx = 0
# for _ in range(n):
#     array.append(list(map(int, input().split())))
#
# for i in range(len(array)):
#     if min(array[i]) > min_value:
#         min_value = min(array[i])
#         min_idx = i
#
# print(min(array[min_idx]))

# min() 함수 이용하여 정제된 코드
# result1 = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value1 = min(data)
#     result1 = max(result1, min_value1)
#
# print(result1)

# 2중 반복문 사용하여 구현
result2 = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value2 = 10001
    for a in data:
        min_value2 = min(min_value2, a)
    result2 = max(result2, min_value2)
print(result2)

