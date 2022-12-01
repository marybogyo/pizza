#adatbekérés
tipusT = []
meret = []
feltetT = []
arT = []
szel = 20
def pizza_rend():
    print("Add meg a pizza adatait!")
    uj_rendeles = ""
    while uj_rendeles != 'n':
        uj_rendeles = input("Akar új rendelést rögzíteni? i- igen, n - nem " )

        if uj_rendeles != 'n':
            csillag()
            print(f"*1 - sajtos {7* ' '}*")
            print(f"*2 - gombás {7 * ' '}*")
            print(f"*3 - sonkás {7 * ' '}*")
            csillag()
            tip = input(f"Válasszon pizzát:  ")
            csillag()
            print(f"*1 - kicsi {7* ' '}*")
            print(f"*2 - normál {6 * ' '}*")
            print(f"*3 - nagy {8 * ' '}*")
            csillag()
            nagysag = input("Válasszon métretet: ")
            fk = input("Kér extra feltétet? i - igen, n - nem: ")
            ar = arak(tip)
            ar = meret_ar(nagysag, ar) + feltet_ar(fk)
            tipusT.append(tipusf(tip))
            meret.append(merete(nagysag))
            feltetT.append(feltet_kelle(fk))
            arT.append(ar)

    i = 0
    szum = 0
    while i < len(tipusT):
        szum+= arT[i]
        szoveg = (f"A rendelt pizza: tipus: {tipusT[i]}, mérete: {meret[i]}, feltét: {feltetT[i]}\n")

        csillag()
        print(szoveg + "Fizetendő: " + str(arT[i]))
        csillag()
        i += 1
    print(f"Fizetendő összesen: {szum}")


def tipusf(tipus):
    tip = " "
    if tipus == "1":
        tip = "Sajtos"
    elif tipus == "2":
        tip = "Gombás"
    else:
        tip = "Sonkás"
    return tip

def arak(tipus):

    normal_sajtos_ar = 1000
    normal_gombas_ar = 1100
    normal_sonkas_ar = 1200
    ar = 0
    if tipus == "1":
        ar = normal_sajtos_ar
    elif tipus == "2":
        ar = normal_gombas_ar
    else:
        ar = normal_sonkas_ar

    return ar
def merete(merete):
    mer = " "
    if merete == "1":
        mer = "Kicsi"
    elif merete == "3":
        mer = "Nagy"
    else:
        mer = "Normál"
    return mer

def meret_ar(merete, ar):

    if merete == "1":
        ar *= 0.9
    elif merete == "3":
        ar *= 1.1
    return ar


def feltet_kelle(feltet):
    felt = " "
    if feltet == "i":
        felt ="Igen"
    else:
        felt = "nincs"
    return felt

def feltet_ar(feltet):
    f_ar = 0
    if feltet == "i":
        f_ar += 50
    return f_ar

def csillag():
    print("*" * szel)



