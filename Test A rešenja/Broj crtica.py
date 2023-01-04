# https://arena.petlja.org/sr-Latn-RS/competition/raspetljavanje-se-test1#tab_134854

n = int(input())
res = 0
mapa = {'-':1, 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
if(n < 0):
  n = abs(n)
  res += mapa['-']
while n>0:
  res += mapa[n%10]
  n //= 10
print(res)
