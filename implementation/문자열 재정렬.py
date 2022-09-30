s = input()
cArr = []
nSum = 0

for i in s:
  if i.isalpha():
    cArr.append(i)
  else:
    nSum += int(i)

cArr.sort()

if nSum != 0:
  cArr.append(str(nSum))

print(''.join(cArr))