from math import sqrt
a = int(input('podaj wartosc wspolczynniku a:'))
b = int(input( 'podaj wartosc wspolczynniku b:'))
c = int(input( 'podaj wartosc wspolczynniku c:'))
if a == 0:
    print('funkcja kwadratowa nie istnieje')

delta = b*b - 4*a*c

if delta < 0:
    print("brak")
elif delta == 0:
    print(-b/(2*a))
else:
    delta = sqrt(delta)
    x1 = (-b + delta)/2*a
    x2 = (-b - delta)/2*a
    print('miejsca zerowe to:', x1, x2)
