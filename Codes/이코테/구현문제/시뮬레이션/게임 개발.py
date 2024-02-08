# 게임판 크기
n, m = map(int, input().split())
# 현재 위치 및 보는 방향
pos_x, pos_y, look = map(int, input().split())

# 동서남북 방향
cardinal_directions = [0, 1, 2, 3]

# 움직임: 북, 동, 남, 서 순으로 1칸 직진, 뒤로 한칸은 그냥 음수 곱하면 됨
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

# Game map 만들기
game_map = []
for i in range(n):
    mini_map = list(map(int, input().split()))
    game_map.append(mini_map)

while True:
    look -= 1
    if look < 0:
        look = 3

    for j in range(len(cardinal_directions)):
        if j == look:
            new_pos_x = pos_x + move_x[j]
            new_pos_y = pos_y + move_y[j]





