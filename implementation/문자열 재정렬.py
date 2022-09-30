s = input()
cArr = []
nSum = 0

for i in s:
  if i.isalpha(): # 알파벳인 경우
    cArr.append(i)
  else: # 숫자인 경우
    nSum += int(i)

cArr.sort()

# 숫자가 있을때만 뒤에 삽입
if nSum != 0:
  cArr.append(str(nSum))

# join 사용하면 리스트를 문자열로 변환 가능
print(''.join(cArr))