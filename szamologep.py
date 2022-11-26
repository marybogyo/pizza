nev = "Béla"
def osszeadas():
    global nev
    szam1 = adatbekeres("Kérek egy számot! ")
    szam2 = adatbekeres("Kérek még egy számot! ")
    osszes = (szam1 +szam2)
    print("=" * 10)
    print("A számolásom eredménye: ")
    print(f"{szam1} + {szam2} {osszes:.2f}")
    print("-" * 10)
    kiiras(szam1, szam2, osszes, "+")
    nev2 = "Szia" + nev
    print(nev)

def kivonas():
    
    szam1 = adatbekeres("Kérek egy számot! ")
    szam2 = adatbekeres("Kérek még egy számot! ")
    osszes = (szam1 - szam2)
    print("=" * 10)
    print("A számolásom eredménye: ")
    print(f"{szam1} - {szam2} = {osszes:.2f}")
    print("-" * 10)
    kiiras(szam1, szam2, osszes,"-")


def kiiras(szam1, szam2, osszes, muv):
    print("=" * 10)
    print("A számolásom eredménye: ")
    print(f"{szam1} {muv} {szam2} = {osszes:.2f}")
    print("-" * 10)

def adatbekeres(uzenet):
    print("=" * 10)
    szam = float(input(uzenet))
    print("-" * 10)

    return szam