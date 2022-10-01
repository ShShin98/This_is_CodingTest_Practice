from itertools import combinations

# 도시의 크기와 폐업시키지 않을 치킨집 입력
n, m = map(int, input().split())
data = [] # 도시 정보 저장
chicken = [] # 치킨집 정보 저장
house = [] # 집 정보 저장

# 도시의 정보 입력
for _ in range(n):
  data.append(list(map(int, input().split())))

# 도시의 크기만큼 반복
# 집과 치킨집의 좌표를 각각의 배열에 저장
for i in range(n):
  for j in range(n):
    if data[i][j] == 1:
      house.append((i, j)) 
    elif data[i][j] == 2:
      chicken.append((i, j))

# 치킨집 배열에서 m개를 뽑는 조합을 리스트에 저장
#[((x, y), (x, y), (x, y)), ((x, y), (x, y), (x, y)), ((x, y), (x, y), (x, y))] 형식
chickCom = list(combinations(chicken, m))

result = 10000 # 가장 작은 '도시의 치킨 거리'

# 리스트에 있는 각각의 조합마다 반복
for com in chickCom:
  cityLen = 0 # 도시의 치킨 거리
  # 집마다 반복
  for h in house: 
    chiLen = 10000 # 집의 치킨 거리
    # 조합 안의 치킨집 갯수만큼 반복
    for j in range(m):
      # 치킨집과의 거리를 구해서 기존의 거리보다 작으면 저장 
      chiLen = min(chiLen, abs(h[0] - com[j][0]) + abs(h[1] - com[j][1]))
    cityLen += chiLen # 도시의 치킨 거리에 더함
  # 그렇게 나온 '도시의 치킨 거리'중 작은값 저장
  result = min(result, cityLen)

print(result)