cala_tresc = []
with open("działania.txt") as plik:
    for wiersz in plik:
        cala_tresc.append([wiersz])

czysta_tresc = []
for wiersz in cala_tresc:
    x = wiersz[0].rstrip("\n")
    x = x.replace(" ", "")
    czysta_tresc.append([x])

print(czysta_tresc)

# Zad 1

cyfry = "0123456789"
operatory = "\+-*"

ile_jest_poprawnych = 0
ile_jest_blednych = 0
dzialania_poprawne = []

for wiersz in czysta_tresc:
    licznik_liczb = 0
    for element in wiersz[0]:
        if element in cyfry:
            licznik_liczb = licznik_liczb + 1
        if element in operatory:
            if licznik_liczb < 2:
                print("NIE")
                ile_jest_blednych = ile_jest_blednych + 1
                break
            else:
                licznik_liczb = licznik_liczb - 1
    if licznik_liczb != 1:
        print("NIE")
        ile_jest_blednych = ile_jest_blednych + 1
    else:
        print("TAK")
        ile_jest_poprawnych = ile_jest_poprawnych + 1
        dzialania_poprawne.append(wiersz)

print(f"Poprawne: {ile_jest_poprawnych}") # f-string - {zmienna}
print(f"Bledne: {ile_jest_blednych}")
print(dzialania_poprawne)










#
# licznik ← 0 # przypisz wartość do zmiennej
# dla i = 1, 2, ..., n wykonuj:
#  jeżeli X[i] jest cyfrą wykonaj:
#  licznik ← licznik + 1
#
#  jeżeli X[i] należy do zbioru {+, –, *} wykonaj:
#  jeżeli licznik < 2 wykonaj:
#  zwróć "Nie" i zakończ działanie
#  w przeciwnym razie wykonaj:
#  licznik ← licznik – 1
#
# jeżeli licznik != 1 wykonaj:
#  zwróć "Nie"
# w przeciwnym razie wykonaj:
#  zwróć "Tak"

