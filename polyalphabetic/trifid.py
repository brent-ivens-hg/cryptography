# https://www.dcode.fr/trifid-delastelle-cipher

from collections.abc import Iterable, Generator
from itertools import chain, islice
from math import gcd

chain = chain.from_iterable


def TRS(it: Iterable) -> zip: return zip(*it)  # transpose


def frac(iterable: Iterable, n: int) -> iter:  # split iterable in n-sized slices
    it = iter(iterable)
    yield from iter(lambda: tuple(islice(it, n)), ())


class Trifid:
    def __init__(self, key: str = '', groupsize: int = 5):
        assert gcd(groupsize, 3), 'group size should be coprime with 3'
        self._size = groupsize
        self._key = ''.join(dict.fromkeys(self._format_key(key) + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ+'))
        self._map = {c: (i // 9, i // 3 % 3, i % 3) for i, c in enumerate(self._key)}
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self): return f'{self.__class__.__name__}({self._key!r})'

    def __str__(self):
        return '{0} {1} {2}   {9} {10} {11}   {18} {19} {20}\n' \
               '{3} {4} {5}   {12} {13} {14}   {21} {22} {23}\n' \
               '{6} {7} {8}   {15} {16} {17}   {24} {25} {26}'.format(*self._key)

    @staticmethod
    def _format_key(key: str) -> str: return ''.join(filter(str.isalpha, key)).upper()

    def _fractionate(self, iterable: Iterable) -> Iterable:
        return chain(frac(chain(col), 3) for col in TRS(frac(row, self._size) for row in iterable))

    def _defractionate(self, iterable: Iterable) -> zip:
        raise NotImplementedError

    def _substitute(self, iterable: Iterable) -> Generator: return (self._map[x] for x in iterable if x in self._map)

    def encode(self, plaintext: str) -> str:
        chars = plaintext.upper()
        return ''.join(self._substitute(self._fractionate(TRS(self._substitute(chars)))))

    def decode(self, ciphertext: str) -> str:  # FixMe
        chars = ciphertext.upper()
        return ''.join(self._substitute(self._defractionate(self._substitute(chars))))


'''
cipher = Trifid('CRYPTOGRAPHY')
print(cipher)
print(cipher.encode('FELIX DELASTELLE'))
print(cipher.decode('ILASFIGHOJTIHOJ'))

cipher = Trifid('FELIX MARIE DELASTELLE', 5)
print(cipher)
print(cipher.encode('AIDE TOI LE CIEL T AIDERA'))
print(cipher.decode('FMJFV OISSU FTFPU FEQQC'))
'''
cipher = Trifid(groupsize=5)
# print(cipher)
print(*cipher._substitute('SECRETS'))
print(*TRS(cipher._substitute('SECRETS')))
print(*cipher._fractionate(TRS(cipher._substitute('SECRETS'))))
print(*cipher._substitute(cipher._fractionate(TRS(cipher._substitute('SECRETS')))))

print('\n>', *TRS(frac(row, 5) for row in TRS(cipher._substitute('SECRETS'))), '\n')

print(*cipher._substitute('SJLKZYD'))
print(*cipher._defractionate(cipher._substitute('SJLKZYD+++')))

'''
print(cipher.encode('SECRETS'))
print(cipher.decode('SJLKZYD'))
'''
# print(cipher.decode('SJLKZT'))
