array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 재귀함수 형태이기 때문에 End flag 만들어주기
    if start >= end:
        return
    pivot = start # Pivot은 처음 원소 선택
    left = start + 1
    right = end
    while left <= right: # 정상 동작 상태
        while left <= end and array[left] <= array[pivot]: # 왼->오 방향으로 피벗보다 큰거 찾음
            left += 1
        while right > start and array[right] >= array[pivot]: # 왼<-오 방향으로 피벗보다 작은거 찾음
            right -= 1
        if left > right: # 위의 조건에 안걸려서 서로 엇갈린 경우 피벗을 해당 위치로 옮김
            array[right], array[pivot] = array[pivot], array[right]
        else: # 정상 동작 상태이고, 안 엇갈린 경우에는 두 데이터의 위치를 서로 변경
            array[left],  array[right] = array[right], array[left]
    quick_sort(array, start, right-1) # 서로 엇갈려서 피벗 옮긴 후에 반 나눠서 다시 진행(왼쪽 부분)
    quick_sort(array, right+1, end) # 서로 엇갈려서 피벗 옮긴 후에 반 나눠서 다시 진행(오른쪽 부분)

quick_sort(array, 0, len(array)-1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort2(array):
    # 파이썬의 장점을 살린 퀵 정렬
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot] # 피벗 기준으로 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 피벗 기준으로 분할된 오른쪽 부분

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))
