n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True) # 입력받은 수 내림차순으로 정렬
first = data[0] # 가장 큰 수
second = data[1] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (int(m / (k + 1)) * k) + (m % (k + 1))

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result)