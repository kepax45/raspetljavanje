import decimal

novac = float(input())
n = int(input())
predmeti = []
def get_decimal(n):
    return decimal.Decimal(n).quantize(decimal.Decimal('0.00'))
for i in range(n):
    ime = input()
    cena = float(input())
    predmeti.append((cena, ime))
predmeti.sort()
pos = len(predmeti)-1
while novac > 0.0 and pos >= 0:
    if(novac-predmeti[pos][0]>=0):
        novac -= predmeti[pos][0]
        print(predmeti[pos][1], get_decimal(predmeti[pos][0]))
    pos -= 1
if(novac>0.0):
    print(get_decimal(novac))
