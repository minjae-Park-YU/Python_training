n, m = map(int, input().split())

ball_box = [i for i in range(int(n))]

for i in range(m):
    start, end = map(int, input().split())

    temp = ball_box[start:end+1]
    temp.reverse()
    print(temp)
    ball_box[start:end+1] = temp

for i in range(len(ball_box)):
    print(ball_box[i]+1, end=" ")
