niz = []
for i in range(4):
    niz.append(int(input()))
l = int(input())
niz.sort()
brojac = 0
sum = 0
for i in range(4):
    if(sum+niz[i]>l):
        brojac+=1
        sum = 0
    sum += niz[i]
print(brojac+1)
