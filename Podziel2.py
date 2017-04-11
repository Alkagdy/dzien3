
#input
liczba = input("Podaj liczbe:")
podzielnik = input("Podaj podzielnik:")
#czy tylko cyfry
if liczba.isdigit() and podzielnik.isdigit():

    wynik = int(liczba)/int(podzielnik)
    print(wynik)
    #zaokraglenie do 2 miejsca po przecinku i dlatego float
    if float(round(wynik,2)).is_integer():
        print("Liczba {0} jest podzielna przez {1}".format(liczba, podzielnik))
    else:
        print("Liczba {} nie jest podzielna przez {}".format(liczba, podzielnik))
        #wynik dzielenia zaokraglony do dwoch miejsc po przecinku
        print("Wynik dzielenia: {:2f}".format(wynik))
else:
    print("Podaj liczbe!!")