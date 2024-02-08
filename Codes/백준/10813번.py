n, m = map(int, input().split())

ball_box = [0 for i in range(int(n))]

for i in range(m):
    box1, box2 = map(int, input().split())
    temp = ball_box[box1-1]
    ball_box[box1-1] = ball_box[box2-1]
    ball_box[box2-1] = temp

for i in range(len(ball_box)):
    print(ball_box[i], end=" ")
