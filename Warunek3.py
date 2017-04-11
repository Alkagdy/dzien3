imie = input("Podaj imie:")

if "a" in imie:
    print("Litera a jest w imieniu")
elif "A" in imie:
    print("Litera A jest w imieniu")
else:
    print("W imieniu nie ma litery A i a")

if imie.endswith("a"):
    print("Chyba jestes kobieta")
else:
    print("Jestes facetem")
