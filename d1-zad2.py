#d1-zad2
plik = open("liczby (1).txt", "r")
lista = []
for i in plik:
    lista.append(i.strip())
print("Lista:",lista)
plik.close()

krotka = tuple(lista)
print("Krotka:",krotka)