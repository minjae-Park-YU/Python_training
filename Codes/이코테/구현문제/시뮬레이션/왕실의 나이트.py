# 처음 풀었을 때, 핵심적인 부분은 문자열도 인덱싱이 된다는거임
pos = input()
new_pos_y = int(pos[1])
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
movable_cnt = 0

for i in range(len(alphabet)):
    if pos[0] == alphabet[i]:
        new_pos_x = i+1

move_1 = [1, 1, -1, -1]
move_2 = [1, 1, -1, -1]
move_3 = [1, -1, 1, -1]

for j in range(len(move_1)):
    new_pos = [new_pos_x + move_1[j] + move_2[j], new_pos_y + move_3[j]]
    if 0 < min(new_pos) and max(new_pos) < 9:
        movable_cnt += 1

for k in range(len(move_1)):
    new_pos = [new_pos_x + move_3[k], new_pos_y + move_1[k] + move_2[k]]
    if 0 < min(new_pos) and max(new_pos) < 9:
        movable_cnt += 1

print(movable_cnt)

# 정제된 풀이
move_1 = [2, 2, -2, -2]
move_2 = [1, -1, 1, -1]
# 이런식으로 표현하면 메모리 및 소요시간 아낄 수 있음