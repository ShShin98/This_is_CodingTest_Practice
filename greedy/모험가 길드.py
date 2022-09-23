n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도 낮은 순으로 확인
  cnt += 1 # 그룹에 현재 모험가 추가
  if cnt >= i: # 현재 그룹에 포함된 모험가 수가 현재 모험가의 공포도 이상이라면
    group += 1 # 그룹 결성, 그룹의 수 1 증가
    cnt = 0 # 그룹에 포함된 모험가의 수 초기화

print(group)