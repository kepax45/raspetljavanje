import datetime
import time

n = int(input())
resenja = []

def unix_vreme(resenje):
    vreme = datetime.datetime(resenje[0], resenje[1], resenje[2], resenje[3], resenje[4])
    return time.mktime(vreme.timetuple())
for i in range(n):
    resenja.append(list(map(int, input().split())))
resenja.sort(key=unix_vreme)
resenja[0] = list(map(str, resenja[0]))
resenja[1] = list(map(str, resenja[1]))
resenja[2] = list(map(str, resenja[2]))
print(' '.join(resenja[0]))
print(' '.join(resenja[1]))
print(' '.join(resenja[2]))
