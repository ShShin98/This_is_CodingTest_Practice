n, m = map(int, input().split()) # 맵의 크기 입력
x, y, direction = map(int, input().split()) # 현재 캐릭터의 좌표, 방향 입력

# 방문한 위치를 저장하기 위한 맵 생성
d = [[0] * m for _ in range(n)]
d[x][y] = 1 # 현재 위치에 1 저장 (방문처리)

# 전체 맵 정보 입력 
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
# 북:0 동:1 남:2 서:3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1 # 방문한 칸의 수
turn_time = 0 # 회전한 횟수

while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 후 정면에 가보지 않은 칸이 존재하는 경우
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1 # 해당 칸을 방문 처리
    # 현재 좌표 변경
    x = nx 
    y = ny
    count += 1
    turn_time = 0
    continue
  # 이미 갔던 칸이거나 바다인 경우
  else:
    turn_time += 1 # 이동은 하지 않고 회전 횟수만 +1
  
  # 회전 횟수가 4일때 -> 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    # dx, dy를 빼면 뒤로 가는 효과
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 (뒤가 육지인 경우)
    if array[nx][ny] == 0:
      # 현재 좌표 변경
      x = nx
      y = ny
    else: # 뒤가 바다인 경우
      break
    turn_time = 0

print(count)
  