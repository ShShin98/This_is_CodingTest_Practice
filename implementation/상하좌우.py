from shutil import move


n = int(input())
x, y = 1, 1 # 초기 좌표
plans = input().split()

# 이동할 계획에 따른 좌표 변화
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      # 이동한 좌표를 임시로 저장
      nx = x + dx[i]
      ny = y + dy[i]
    # 범위를 벗어난 경우 무시 
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    # 현재 위치를 이동
    x = nx
    y = ny

print(x, y)