# https://arena.petlja.org/sr-Latn-RS/competition/raspetljavanje-se-test1#tab_134852

arr = [int(input()), int(input()), int(input()), int(input())]
arr.sort()
d = int(input())
pos = 0
x = arr[0]
arr.sort()
print(pos)
c = -1
while pos < len(arr):
  nextPos = pos
  nextX = x
  for i in range(pos + 1, len(arr)):
    if (x + d >= arr[i]):
      nextPos = i
      nextX = arr[i]
  if (nextPos == pos):
    break
  pos = nextPos
  print(pos)
  x = nextX
  c += 1
print(str(c) * (c >= 0) + '-' * (c == -1))
