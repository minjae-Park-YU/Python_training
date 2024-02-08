# 처음 풀었을 때
n = int(input())
directions = list(input().split())
commands = {'L':[0, -1], 'R':[0, 1], 'U':[-1, 0], 'D':[1, 0]}
pos = [1, 1]
for d in directions:
    new_pos = [i+j for i, j in zip(pos, commands[d])]
    if min(new_pos) > 0 and max(new_pos) < n+1:
        pos = new_pos

for i in range(len(pos)):
    print(pos[i], end=" ")

# dx, dy 이용하여 정제된 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

