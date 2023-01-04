# https://arena.petlja.org/sr-Latn-RS/competition/raspetljavanje-se-test1#tab_134853

rec = input()
samoglasnici = list('aeiou')
c = 0
for i in range(1, len(rec)-1):
  if(rec[i] in samoglasnici):
    c += 1
  if(rec[i]=='r' and rec[i-1] not in samoglasnici and rec[i+1] not in samoglasnici):
    c += 1
if(rec[0] in samoglasnici):
  c += 1
if(len(rec) > 1 and rec[len(rec)-1] in samoglasnici):
  c += 1
if(rec[0]=='r' and rec[1] not in samoglasnici):
  c += 1
if(rec[len(rec)-1]=='r' and rec[len(rec)-2] not in samoglasnici):
  c += 1
print(c)
