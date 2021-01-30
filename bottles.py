class Palack(object):
    def __init__(self, ital, max_urtartalom, _jelenlegi_urtartalom=1):
        self.ital = ital
        self.max_urtartalom = max_urtartalom
        self._jelenlegi_urtartalom = _jelenlegi_urtartalom

    @property
    def jelenlegi_urtartalom(self):
        return self._jelenlegi_urtartalom

    @jelenlegi_urtartalom.setter
    def jelenlegi_urtartalom(self, ertek):
        if ertek > self.max_urtartalom:
            self._jelenlegi_urtartalom = self.max_urtartalom
        else:
            self._jelenlegi_urtartalom = ertek
        if ertek == 0:
            self.ital = None

    def suly(self):
        suly = (self.max_urtartalom / 35) + self._jelenlegi_urtartalom
        return suly

    def __str__(self):
        return f"Palack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."

    def __eq__(self, other):
        if not isinstance(other, Palack):
            return False

        return self.__dict__ == other.__dict__

    def __iadd__(self, other):
        if isinstance(other, Palack):
            self.jelenlegi_urtartalom = self._jelenlegi_urtartalom + other._jelenlegi_urtartalom
            if self.ital == None:
                self.ital = other.ital
            elif other.ital != self.ital:
                self.ital = "keverek"

        return self


class VisszavalthatoPalack(Palack):
    def __init__(self, ital, max_urtartalom, _jelenlegi_urtartalom=1, palackdij=25):
        super().__init__(ital, max_urtartalom, _jelenlegi_urtartalom)
        self.palackdij = palackdij

    def __str__(self):
        return f"VisszavalthatoPalack, benne levo ital: {self.ital}, jelenleg {self._jelenlegi_urtartalom} ml van benne, maximum {self.max_urtartalom} ml fer bele."


class Rekesz(object):
    def __init__(self, max_teherbiras):
        self.max_teherbiras = max_teherbiras
        self.palackok = []

    def suly(self):
        sum = 0
        if len(self.palackok) == 0:
            return 0
        for i in range(0, len(self.palackok)):
            sum += self.palackok[i].suly()
        return sum

    def uj_palack(self, param):
        if isinstance(param, Palack):
            var = self.suly() + param.suly()
            if var < self.max_teherbiras:
                self.palackok.append(param)

    def osszes_penz(self):
        penz = 0
        for i in range(0, len(self.palackok)):
            if isinstance(self.palackok[i], VisszavalthatoPalack):
                penz += self.palackok[i].palackdij
        return penz

uveg = Palack("gg", 15, 10)
uveg2 = Palack("kk", 20, 15)
pal = VisszavalthatoPalack("ggg", 20, 40, 10)
pal2 = VisszavalthatoPalack("jjj", 50, 60, 20)
rek = Rekesz(2)
rek2 = Rekesz(10)
rek.palackok = [pal, pal2, uveg2]
print(rek.suly())
# uveg.jelenlegi_urtartalom = 0
uveg += uveg2
print(uveg.ital)
print(uveg.max_urtartalom)
print(uveg._jelenlegi_urtartalom)
print(rek.osszes_penz())
print(rek.uj_palack(pal))
