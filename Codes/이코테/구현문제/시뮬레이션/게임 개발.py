# 게임판 크기
n, m = map(int, input().split())
# 현재 위치 및 보는 방향
pos_x, pos_y, look = map(int, input().split())

# 탐색 횟수 및 방문 횟수 정의
explore_cnt = 0
room_cnt = 0

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

# 현재 위치 방문 처리
game_map[pos_x][pos_y] = 1
room_cnt += 1

while True:
    look -= 1
    if look < 0:
        look = 3

    explore_cnt += 1

    new_pos_x = pos_x + move_x[look]
    new_pos_y = pos_y + move_y[look]
    # 이동 후의 위치가 게임판 안이고, 육지인 경우에만 이동하기 위한 조건
    if min([new_pos_x, new_pos_y]) > -1 and max([new_pos_x, new_pos_y]) < min([n, m]) and game_map[new_pos_x][new_pos_y] == 0:
        pos_x, pos_y = new_pos_x, new_pos_y
        game_map[new_pos_x][new_pos_y] = 1
        explore_cnt = 0
        room_cnt += 1

    # 4방향 모두 탐색했는데 이동 할 수 없을 시
    if explore_cnt == 3:
        new_pos_x = pos_x - move_x[look]
        new_pos_y = pos_y - move_y[look]
        # 뒤로 갈 수 있으면 뒤로 가기
        if min([new_pos_x, new_pos_y]) > -1 and max([new_pos_x, new_pos_y]) < min([n, m]) and game_map[new_pos_x][new_pos_y] == 0:
            pos_x, pos_y = new_pos_x, new_pos_y
            game_map[new_pos_x][new_pos_y] = 1
            explore_cnt = 0
            room_cnt += 1
        # 어떤 곳으로도 갈 수 없으면 끝
        else:
            print(room_cnt)
            break





