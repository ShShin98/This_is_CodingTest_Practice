from collections import deque
from csv import DictReader

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

# 사과의 갯수 입력
k = int(input())
# 사과가 위치한 곳을 2로 설정
for i in range(k):
  a, b = map(int, input().split())
  board[a][b] = 2

# 방향 전환 횟수 입력
l = int(input())
dirDic = dict()
# 방향 전환 정보 딕셔너리에 저장
for i in range(l):
  x, c = input().split()
  dirDic[int(x)] = c

# 뱀의 몸을 저장할 큐 (꼬리 자르는데 사용, FIFO)
queue = deque()
queue.append((1, 1)) # 초기 위치를 큐에 삽입

#     동  남  서  북 (0, 1, 2, 3)   
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0 # 처음에는 동쪽을 바라봄

cnt = 0 # 시간 
x, y = 1, 1 # 초기 좌표
board[x][y] = 1 # 초기 좌표를 1로 설정

# 방향 전환하는 함수
def turn(alpha):
  global direction
  if alpha == "L": # L이면 시계 반대방향으로 회전
    direction -= 1
    if direction == -1:
      direction = 3
  else: # D이면 시계 방향으로 회전
    direction += 1
    if direction == 4:
      direction = 0

while True:
  cnt += 1 # 1초 증가

  # 현재 방향으로 좌표 이동
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 벽과 부딪힌 경우
  if nx < 1 or ny < 1 or nx > n or ny > n:
    break

  # 이동할 위치에 사과가 있는 경우
  if board[nx][ny] == 2:
    queue.append((nx, ny)) # 이동할 위치(머리)를 큐에 삽입
    board[nx][ny] = 1 # 값을 1로 변경
    # 현재 위치 변경
    x = nx 
    y = ny
    # 현재 초가 방향 전환할 시간이라면
    if cnt in dirDic:
      turn(dirDic[cnt]) # cnt초에 맞는 방향으로 회전
  
  # 이동할 위치에 사과가 없는 경우
  elif board[nx][ny] == 0:
    tx, ty = queue.popleft() # 큐에서 pop(가장 초기에 삽입된 값)
    board[tx][ty] = 0 # pop된 위치를 0으로 변경
    queue.append((nx, ny)) # 이동할 위치를 큐에 삽입
    board[nx][ny] = 1 # 값을 1로 변경
    # 현재 위치 변경
    x = nx
    y = ny
    if cnt in dirDic:
      turn(dirDic[cnt])

  # 자기 자신의 몸과 부딪힌 경우 
  else:
    break

print(cnt)

# https://hongcoding.tistory.com/127