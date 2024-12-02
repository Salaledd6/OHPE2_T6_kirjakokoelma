kirjat = [
    ("978-0-306", "Introduction to Algorithms", "Thomas H. Cormen", 5),
    ("978-0-672", "Python Crash Course", "Eric Matthes", 8),
    ("978-0-07", "Clean Code", "Robert C. Martin", 3),
    ("978-1-491", "Deep Learning", "Ian Goodfellow", 2),
    ("978-0-321", "The Pragmatic Programmer", "Andrew Hunt", 6),
]

def tulosta_kirjat(tulostettavat: list):
    print("Kirjaston kirjalista:")
    for kirja in tulostettavat:
        (isbn, nimi, tekija, kpl) = kirja
        tuloste = f"ISBN: {isbn:20s} Nimi:{nimi:20s} Tekijä: {tekija:20s} kpl:{kpl:20d}"
        print(tuloste)

def lisaa_kirja(kirjalista: list):
    print("Syötä lisättävän kirjan tiedot: ")
    isbn = input("ISBN > ")
    nimi = input("Nimi > ")
    tekija = input("Tekija > ")
    kpl = int(input("Kappalemäärä > "))
    kirjatuple = (isbn, nimi, tekija, kpl)
    kirjalista.append(kirjatuple)

def poista_kirja(kirjalista: list):
    isbn = input("Syötä poistettavan kirjan ISBN >")
    for kirja in kirjalista:
        if isbn == kirja[0]:
            kirjalista.remove(kirja)
            break

def kirjoja_yhteensa(kirjalista: list):
    yhteensa = 0
    for kirja in kirjalista:
        yhteensa += kirja[3]
    return yhteensa

'''Ohjelman suoritus alkaa tästä'''
while True:
    print("Valitse toiminto:")
    print("\t1 = Tulosta kirjat")
    print("\t2 = Lisää kirja")
    print("\t3 = Poista kirja")
    print("\t4 = Kirjoja yhteensä")
    print("\t5 = Lopeta")

    valinta = input("> ")

    if valinta == "1":
        tulosta_kirjat(kirjat)
    elif valinta == "2":
        lisaa_kirja(kirjat)
    elif valinta == "3":
        poista_kirja(kirjat)
    elif valinta == "4":
        print(f"Kirjoja yhteensä: {kirjoja_yhteensa(kirjat)}")
    elif valinta == "5":
        break
