#ZAD 3 - Napisz program w Python, który policzy, ile dni,
# tygodni i miesięcy zostało użytkownikowi do końca życia, zakładając, że
# średnia życia człowieka to 90 lat. Użytkownik podaje swoją
# datę urodzenia + zakładając poniższe (nie uwzględniamy roków przestępnych):
#1 rok = 12 miesięcy = 52 tygodnie = 365 dni

from datetime import date

teraz = date.today()
print(f"Dziesiejsza data: {teraz}")

x = int(input("Podaj datę urodzenia: "))
print(x)

