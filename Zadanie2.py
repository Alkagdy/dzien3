#czy liczba jest podzielna przez 3, 5 lub 7

#input
liczba = input("Podaj liczbe:")
#spr czy tylko cyfry
if liczba.isdigit():
#jesli podzielna przez 3
    if int(liczba) %3==0:
        print("Podzielna przez 3")

# w przeciwnym wypadku czy podzielna przez 5
    elif int(liczba) %5==0:
        print("Podzielna przez 5")
    #napisz podzielna przez 5
#Czy podzielna przez 7
    elif int(liczba) %7==0:
        print("Liczba podzielna przez 7")
else:
    print("Podaj liczbe!!")