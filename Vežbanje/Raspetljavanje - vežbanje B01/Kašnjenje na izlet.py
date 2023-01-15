n, k = map(int, input().split())
rezultat = []
for i in range(n):
    ulaz = input().split()
    rezultat.append((int(ulaz[0])*60+int(ulaz[1]), ulaz[2]))
rezultat.sort(reverse=True)
for i in range(k):
    print(rezultat[k-i-1][1])
