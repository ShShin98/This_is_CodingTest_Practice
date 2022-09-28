input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 (row, column) 순
steps = [(2,1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
cnt = 0
# 8가지 방향에 대해서
for step in steps:
  # 이동한 임시 좌표
  nrow = row + step[0]
  ncolumn = column + step[1]
  # 임시 좌표가 범위 안에 있으면 카운트 증가
  if nrow >= 1 and nrow <= 8 and ncolumn >= 1 and ncolumn <= 8:
    cnt += 1

print(cnt)
