remaining_list = [0 for i in range(42)]
count = 0
for i in range(10):
    number = int(input())
    remaining_list[number % 42] += 1

for i in range(len(remaining_list)):
    if remaining_list[i] > 0:
        count += 1
print(count)
