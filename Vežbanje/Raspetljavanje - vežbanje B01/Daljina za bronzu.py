n = int(input())
niz = list(map(int, input().split()))
niz.sort(reverse=True)
if(2==len(niz)-1):
    print(0)
    exit()
if(niz[2]<niz[-1]):
    exit()
print(niz[2]+1)
