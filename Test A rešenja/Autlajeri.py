# https://arena.petlja.org/sr-Latn-RS/competition/raspetljavanje-se-test1#tab_134856

import math
n = int(input())
arr = []
res = 0
for i in range(n):
  arr.append(float(input()))
arr.sort()
if(n/4-n//4!=0.0):
  q1 = arr[math.ceil(n/4)-1]
else:
  q1 = (arr[n//4-1]+arr[n//4])/2
if(3*n/4-3*n//4!=0.0):
  q3 = arr[math.ceil(3*n/4)-1]
else:
  q3 = (arr[3*n//4-1]+arr[3*n//4])/2
iqr = q3-q1
for i in range(n):
  if(arr[i] < (q1 - 1.5*iqr) or arr[i] > (q3 + 1.5*iqr)):
    res += 1
print(res)
