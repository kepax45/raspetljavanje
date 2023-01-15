n, x, y = list(map(int, input().split()))
ucenici = []
for i in range(n):
    ulaz = input().split()
    ucenici.append((float(ulaz[0]), ulaz[2]+" "+ulaz[1]))
ucenici.sort(reverse=True)
for i in range(x, y+x):
    print(ucenici[i][1])
