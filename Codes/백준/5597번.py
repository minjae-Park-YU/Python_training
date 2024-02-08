student_id_list = [0 for i in range(30)]
not_submit = []

for i in range(28):
    student_id = int(input())
    student_id_list[student_id-1] = 1

for i in range(30):
    if student_id_list[i] == 0:
        not_submit.append(i+1)

for i in range(2):
    print(not_submit[i])
