# 해답 보고 푼 문제
n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)

# 핵심은, 리스트가 아니라 하나의 문자열이라도 '3' in str의 형태로 수행해도 찾을 수 있다는 점임.
