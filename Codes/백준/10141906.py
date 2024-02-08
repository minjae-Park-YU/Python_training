array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
from bisect impoft bisect_left, bisect_right

def my_key(x):
    return x[1]

print(sorted(array, key=my_key, reverse=True))
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))

print(ord('A'))

result = ['A', '1', '2']
print(''.join(result))

print(min(list1))