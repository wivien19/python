# Voros Vivien
# J4VDGE
# h986160

def dict_kiegeszit(parameter):
    lista = []
    if len(parameter) == 0:
        return parameter
    for i in parameter:
        lista.append(i)
    for i in range(1, max(lista)):
        if i not in lista:
            parameter[i] = 0

    return parameter


class Film:
    def __init__(self, _cim, hossz=60):
        self._cim = _cim
        self.hossz = hossz
        self.ertekelesek = []

    @property
    def cim(self):
        return self._cim

    @cim.setter
    def cim(self, ertek):
        if isinstance(ertek, str):
            self._cim = ertek

    def ertekelest_felvesz(self, ertekeles):
        if not isinstance(ertekeles, float):
            raise Exception("Hibas ertekeles")
        else:
            if (ertekeles >= 1.0 and ertekeles <= 10.0):
                self.ertekelesek.append(ertekeles)
            else:
                raise Exception("Hibas ertekeles")

    def __lt__(self, other):
        if not isinstance(other, Film):
            return False
        if self.hossz < other.hossz:
            return True
        else:
            return False

    def __str__(self):
        return self._cim + ", " + str(self.hossz) + " perc hosszu film, " + str(
            len(self.ertekelesek)) + " darab ertekelessel."

    def __eq__(self, other):
        if not isinstance(other, Film):
            return False
        return self.__dict__ == other.__dict__

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# res = { 4: 8, 6: 1, 3: 10 }
# print(dict_kiegeszit(res))

szoveg = "Micimackó szereti a mézet."
print(szoveg[:])

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):

   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


