#https://arena.petlja.org/sr-Latn-RS/competition/raspetljavanje-se-test1#tab_134855

import math
n = int(input())
res = 2**31
for i in range(n):
  broj = int(input())
  stepen = 0
  tmp = 0
  while (2**stepen) <= broj:
    if(broj%(2**stepen)==0):
      tmp = (2**stepen)
    stepen+=1
  res = min(res, tmp)
print(res)
