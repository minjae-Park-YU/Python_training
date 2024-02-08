n, k = map(int, input().split())
result = 0
cnt = 0

# 처음 생각한 풀이.
while True:
    if k > 1 and n % k == 0:
        n = n//k
    else:
        n -= 1
    cnt += 1
    if n == 1:
        break

print(cnt)

# 빼기 먼저 해서 딱 떨어지게 만든다음 나누기하는 풀이법
n, k = map(int, input().split())
result1 = 0
while True:
    target = (n // k) * k
    result1 += (n - target) # 원래 n에서 딱 맞아떨어지는 target까지 차이를 생각하면 -1씩 이만큼 빼준거랑 같음.
    n = target
    if n < k:
        break
    result1 += 1
    n //= k

result1 += (n-1) # n이 1이라면 0이 더해져서 의미없는 수가 될 것임. 근데 그 이외의 경우에는 다시 -1씩 전부 해줘야 하기 때문에, n과 1까지의 차이를 더해주면 완성
print(result1)


