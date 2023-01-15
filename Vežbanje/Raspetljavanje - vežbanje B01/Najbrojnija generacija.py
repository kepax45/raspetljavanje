n = int(input())
podaci = list(map(int, input().split()))
def najbrojnija(l):
    l.sort(reverse=True)
    pod = l
    res = 0
    godina = podaci[0]
    c = 0
    for i in range(len(pod)-1):
        c += 1
        if(pod[i]!=pod[i+1]):
            if(res < c):
                res = c
                godina = pod[i]
            c = 0
    if(res < c+1):
        res = c+1
        godina = pod[len(pod)-1]
    print(godina)
najbrojnija(podaci)
