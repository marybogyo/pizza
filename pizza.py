#adatbekérés
tipusT = []
meret = []
feltetT = []
ar = []

def adatbekeres():
    tip = input("Válasszon pizzát: 1 - sajtos, 2 - gombás, 3 - sonkás: ")
    nagysag = input("mekkora méretben? k - kicsi, n - normál, na - nagy: ")
    fk = input("Kér plusz feltétet: i - igen, n - nem: ")
    uj_rendeles = input("Akar új rendelést rögzíteni: i- igen, n - nem")
    i = 0

    tipusT.append(tipusf(tip))
    meret.append(merete(nagysag))
    feltetT.append(feltet_kelle(fk))

def tipusf(tipus):
    tip = " "
    if tipus == 1:
        tip = "Sajtos"
    elif tipus == 2:
        tip = "Gombás"
    else:
        tip = "Sonkás"
    return tip

def merete(merete):
    mer = " "
    if merete == "k":
        mer = "Kicsi"
    elif merete == "n":
        mer = "Normál"
    else:
        mer = "Nagy"
    return mer

def feltet_kelle(feltet):
    felt = " "
    if feltet == "i":
        felt ="Igen"
    else:
        felt = "Nem"
    return felt

def arak():

    plusz_feltet = 50
    normal_sajtos_ar = 1000
    normal_gombas_ar = 1100
    normal_sonkas_ar = 1200



