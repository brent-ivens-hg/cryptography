from itertools import count


class Alberti:  # AUTO RESETS AFTER ENCRYPTION / DECRYPTION
    """
    Formula: polyalphabetic substitution with mixed alphabets and variable period, made up of two conentric disks
    Stabilis: the larger, stationary disk
    Mobilils: the smaller, movable disk
    """

    def __init__(
            self,
            disk1: str = 'ABCDEFGILMNOPQRSTVXZ1234',
            disk2: str = 'gklnprtvz&xysomqihfdbace',  # OR 'c&bmdgpfznxyvtoskerlhaiq'
            shift: int = 0,
            increment: int = 1,
            period: int = 4
    ) -> None:
        """
        :param disk1: outer ring: uppercase alphabet for plaintext, and numbers 1-4
        :param disk2: inner ring: lowercase mixed alphabet for ciphertext
        :param shift: initial shift
        :param increment: periodic increment
        :param period: period length
        """
        if len(disk1) != len(disk2): raise ValueError('the disks must have equal length')
        self._disk1 = disk1
        self._disk2 = disk2
        self._map1 = dict(enumerate(disk1)); self._map1.update({v: k for k, v in self._map1.items()})
        self._map2 = dict(enumerate(disk2)); self._map2.update({v: k for k, v in self._map2.items()})
        self._shift = shift
        self._inc = increment
        self._period = period

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._disk1!r}, {self._disk2!r},' \
               f' shift={self._shift!r}, increment={self._inc!r}, period={self._period!r})'

    def encode(self, plaintext: str) -> str:
        shift = count()
        return ''.join(self._map2[(self._map1[c] + self._shift + next(shift) // self._period * self._inc) % 26]
                       for c in plaintext.upper() if c in self._map1).upper()

    def decode(self, ciphertext: str) -> str:
        shift = count()
        return ''.join(self._map1[(self._map2[c] - self._shift - next(shift) // self._period * self._inc) % 26]
                       for c in ciphertext.lower() if c in self._map2).upper()

def test_alberti():
    cipher = Alberti()
    print(cipher)
    print(cipher.encode('ALBERTI'))
    print(cipher.decode('GZKPQHZ'))

    cipher = Alberti('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', 1, 2, 3)
    print(cipher)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('BUUDFN FY IHDU'))
