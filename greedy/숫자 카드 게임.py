n, m = map(int, input().split())

result = 0

# 한줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  minCard = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  # 반복문을 돌 때 마다 전 줄의 '가장 작은 수'와 비교해서 더 큰 수가 대입됨
  result = max(result, minCard)

print(result)
