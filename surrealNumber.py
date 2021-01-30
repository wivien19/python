import typing


def is_happy(number: int, checked: typing.List[int] = []):
    if not isinstance(number, int):
        return None

    txt = str(number)
    while len(txt) != 1:
        sum = 0
        for i in range(0, len(txt)):
            sum += int(txt[i]) ** 2
        txt = str(sum)
        if sum == 1:
            return True

    return False


class SurrealNumber(object):
    def __init__(self, left, right):
        self._left = left
        self._right = right
        if not (isinstance(left, set) or isinstance(right, set)):
            raise TypeError

    @property
    def left(self):
        return tuple(self._left)

    @property
    def right(self):
        return tuple(self._right)

    def __str__(self):
        separator = ","
        eredmeny = ""
        for i in range(0, len(self._left)):
            eredmeny += self.left[i]
            eredmeny += ","
        eredmeny = eredmeny[:-1]
        eredmeny += "|"
        for i in range(0, len(self._right)):
            eredmeny += self.right[i]
            eredmeny += ","
        eredmeny = eredmeny[:-1]
        itemization = separator.join(map(str, self.left)) + "|" + separator.join(map(str, self.right))
        return itemization

    def __le__(a, b):
        if not (isinstance(a, SurrealNumber) or isinstance(b, SurrealNumber)):
            return False
        else:
            if b <= a.left:
                return False
            if b.right <= a.left:
                return False

        return True

    def __lt__(a, b):
        if not b <= a:
            return True
        else:
            return False


b = SurrealNumber({0, 0}, {3, 2})
a = SurrealNumber({1, 3}, {5, 4})

print(a < b)
