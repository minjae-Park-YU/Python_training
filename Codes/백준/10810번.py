n, m = map(int, input().split())

ball_box = [0 for i in range(int(n))]

for i in range(m):
    first, last, number = map(int, input().split())
    for j in range(first-1, last):
        ball_box[j] = number

for i in range(len(ball_box)):
    print(ball_box[i], end=" ")
