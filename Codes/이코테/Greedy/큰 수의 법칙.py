n, m, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0
idx_count = 0
array.sort(reverse=True)

# 첫 번째 시도: 곧바로 생각나는 대로 품
for _ in range(m):
    if idx_count < k:
        result += array[0]
        idx_count += 1
    else:
        result += array[1]
        idx_count = 0

print(result)

# 두 번째 시도: 패턴화 시켜서 알고리즘 다듬기
pattern_count = m // (k+1)
max_values = (pattern_count + (m % (k+1))) * k * array[0]
submax_values = pattern_count * array[1]

print(max_values + submax_values)






