# Nev: Vörös Vivien
# Neptun: J4VDGE
# h: h986160

def is_disarium(szam):
    disatrium = False
    szoveg = str(szam)

    sum = 0
    maradek = 0
    ujszam = szam
    a = szam

    for i in range(1, len(szoveg) + 1):
        sum += int(szoveg[i - 1]) ** i
        print(sum)

    if szam == sum:
        disatrium = True
    return disatrium


def osszeszoroz(elso, masodik):
    visszaad = []
    for i in range(0, len(elso)):
        for j in range(0, len(masodik)):
            visszaad.append(elso[i] + masodik[j])
    return visszaad


def letter_combinations(szoveg):
    tomb = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    # 2 3
    if len(szoveg) == 1:
        t = []
        for i in range(0, len(tomb[int(szoveg[0])])):
            t.append(tomb[int(szoveg[0])][i])

        return t
    d = tomb[int(szoveg[0])]
    for i in range(1, len(szoveg)):
        d = osszeszoroz(d, tomb[int(szoveg[i])])

    return d


class Savanyusag(object):
    def __init__(self, minoseget_megorzi, nyitva, *elemek):
        self.minoseget_megorzi = minoseget_megorzi
        self.nyitva = nyitva
        self.elemek = list(elemek)
        egyelem = elemek[0]
        self._tipus = egyelem
        for i in range(0, len(elemek)):
            if egyelem != elemek[i]:
                self._tipus = "csalamade"

    @property
    def tipus(self):
        return self._tipus

    @tipus.setter
    def tipus(self, ertek):
        if ertek in self.elemek:
            self._tipus = ertek

    def szavatos(self, ev, ho, nap):
        ertek = False
        if self.minoseget_megorzi[0] >= ev and self.minoseget_megorzi[1] >= ho and self.minoseget_megorzi[2] >= nap:
            ertek = True
        return ertek

    def fedel_csavar(self):
        self.nyitva = not self.nyitva

    def __iadd__(self, other):
        if isinstance(other, Savanyusag):
            if self.nyitva == True and other.nyitva == True:
                self.elemek += other.elemek
                self.minoseget_megorzi = min(self.minoseget_megorzi, other.minoseget_megorzi)
                if set(self.elemek) != set(other.elemek):
                    self._tipus = "csalamade"
                else:
                    self._tipus = self.elemek[0]
            elif self.nyitva == False:
                raise Exception("A savanyusag fedele zarva van!")
            elif other.nyitva == False:
                raise Exception("A masik savanyusag fedele zarva van!")

        return self

    def __str__(self):
        ertek = "zarva"
        if self.nyitva:
            ertek = "nyitva"
        return f"Savanyitott " + self._tipus + ", aminek a fedele " + ertek + "."

    def __imul__(self, szam):
        self.elemek = self.elemek * szam
        return self

    def __eq__(self, other):
        if not isinstance(other, Savanyusag):
            return False
        if self.nyitva == other.nyitva and self.minoseget_megorzi == other.minoseget_megorzi and self._tipus == other._tipus and set(self.elemek) == set(other.elemek) and len(self.elemek) == len(other.elemek):
            return True
        return False

# print(letter_combinations("532"))
#a = Savanyusag(20, 20, "korte", "alma")
#b = Savanyusag(20, 20, "alma", "korte")
# a.tipus = "bela"

#print(a == b)
