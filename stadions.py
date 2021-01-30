# Nev: Vörös Vivien
# Neptun: J4VDGE
# h: h986160

def legnagyobb_stadion(file_path):
    with open(file_path, "r") as file:
        line1 = file.readline()
        table = file.readlines()
    legnagyobb = 0
    neve = ""
    varos = ""
    for line in table:
        sor_alap = line.replace(" ,", ",")
        sor = sor_alap.split(",")
        kapacitas = int(sor[4])
        if legnagyobb < kapacitas:
            legnagyobb = kapacitas
            neve = sor[3]
            varos = sor[2]

    if legnagyobb == 0:
        var = "Nincs (Nincs)"
    else:
        var = neve + " (" + varos + ")"

    with open("legnagyobb.txt", "w") as file:
        file.write(var)


def osszes_arena(eleresiut):
    nezszam = -1

    with open("arena_park.csv", "w") as file:
        file.write("Stadium,City,Country,Big\n")
    with open(eleresiut, "r") as file:
        elsosor = file.readline()
        tartalom = file.readlines()
        for sor in tartalom:
            nagy = False
            sor2 = sor.replace(" ,", ",")
            darabok = sor2.split(",")
            nev = darabok[2]
            stadium = darabok[3]
            nezok = int(darabok[4])
            orszag = darabok[7]
            orszaga = orszag.replace("\n", "")

            if nezok > 50000:
                nagy = True
            if stadium.endswith("Arena"):

                orszaga = orszag.replace("\n", "")
                with open("arena_park.csv", "a") as file:
                    file.write(stadium + "," + nev + "," + orszaga + "," + str(nagy) + "\n")


def osszes_park(eleresiut):
    nezszam = -1

    with open(eleresiut, "r") as file:
        elsosor = file.readline()
        tartalom = file.readlines()
        for sor in tartalom:
            nagy = False
            sor2 = sor.replace(" ,", ",")
            darabok = sor2.split(",")
            nev = darabok[2]
            stadium = darabok[3]
            nezok = int(darabok[4])
            orszag = darabok[7]
            orszaga = orszag.replace("\n", "")

            if nezok > 20000:
                nagy = True
            if stadium.endswith("Park"):
                with open("arena_park.csv", "a") as file:
                    file.write(stadium + "," + nev + "," + orszaga + "," + str(nagy) + "\n")


def varosok_szama(eleresiut, *orszagok):

    if len(orszagok) == 0:
        raise Exception("Nincs megadva egy orszag sem!")
    with open("varosok.txt", "w") as ide:
        with open(eleresiut, "r") as file:
            elsosor = file.readline()
            tartalom = file.readlines()
            for i in range(0, len(orszagok)):
                res = set()
                for sor in tartalom:
                    sor2 = sor.replace(" ,", ",")
                    darabok = sor2.split(",")
                    orszag = darabok[7]
                    orszaga = orszag.replace("\n", "")
                    varos = darabok[2]

                    if orszagok[i] == orszaga:
                        res.add(varos)

                var = sorted(res)
                ide.write(orszagok[i] + " varosai:\n")
                for i in range(0, len(var)):
                    ide.write("\t")
                    ide.write(var[i] + "\n")
                ide.write("----------\n")




# osszes_arena("stadium.csv")
# legnagyobb_stadion("stadium.csv")
# osszes_park("stadium.csv")
#varosok_szama("stadium.csv", "England")
