#czy liczba jest podzielna przez 3, 5 lub 7

#input
liczba = input("Podaj liczbe:")
podzielnik = input("Podaj podzielnik:")
#czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():

    if int(liczba) % int(podzielnik) ==0:
        print("Liczba jest podzielna przez:", podzielnik)
    else:
        print("Liczba nie jest podzielna przez:", podzielnik)
else:
    print("Podaj liczbe!!")
