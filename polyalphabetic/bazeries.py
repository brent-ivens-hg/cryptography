from collections.abc import Iterable, Generator
from itertools import cycle, islice

numword = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}


class Bazeries:
    def __init__(self, *keys, grid1: str = 'AFLQVBGMRWCHNSXDIOTYEKPUZ', grid2: str = '') -> None:
        grid2 = grid2 or ''.join(dict.fromkeys(''.join(map(numword.get, keys)) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))

        if not isinstance(grid1, str) or not isinstance(grid2, str): raise TypeError('invalid type')
        if not (set(grid1.upper()) == set(grid2.upper()) == set('ABCDEFGHIKLMNOPQRSTUVWXYZ')):
            raise ValueError('invalid grid')

        self._keys = keys
        self._grid1 = grid1.upper()
        self._grid2 = grid2.upper()
        self._enc = str.maketrans(self._grid1, self._grid2)
        self._dec = str.maketrans(self._grid2, self._grid1)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{*self._keys, self._grid1, self._grid2}'

    def partition(self, iterable: Iterable[str]) -> Generator[str, None, None]:
        keys = cycle(self._keys)
        while 1:
            part = ''.join(islice(iterable, next(keys)))[::-1]
            if not part: break
            yield part

    def encode(self, plaintext: str) -> str:
        plaintext = plaintext.upper()
        encoded = iter(''.join(self.partition(c for c in plaintext if c in self._grid1)).translate(self._enc))
        return ''.join(next(encoded) if c in self._grid1 else c for c in plaintext)

    def decode(self, ciphertext: str) -> str:
        ciphertext = ciphertext.upper()
        decoded = iter(''.join(self.partition(c for c in ciphertext if c in self._grid2)).translate(self._dec))
        return ''.join(next(decoded) if c in self._grid2 else c for c in ciphertext)


def test_bazeries():
    cipher = Bazeries(1, 2, 3)
    print(cipher)
    print(cipher.encode('attack at dawn'), cipher.decode('OQQVDO OL QGCO'))
