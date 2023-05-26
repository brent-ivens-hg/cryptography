from collections.abc import Iterable, Sequence
from itertools import chain, zip_longest
from typing import Any

chain = chain.from_iterable


def TRS(iterable: Iterable) -> tuple[tuple]:
    return tuple(zip(*iterable))


def zipper(iterable: Iterable, n: int) -> zip:
    return zip(*[iter(iterable)] * n)


def grouper(iterable: Iterable, n: int, fillvalue: Any = None) -> tuple[tuple]:
    return tuple(zip_longest(*[iter(iterable)] * n, fillvalue=fillvalue))


def inverse(permutation: Sequence[int]) -> list[int]:
    res = [0] * len(permutation)
    for i, p in enumerate(permutation): res[p] = i
    return res


class ADFGVX:
    def __init__(self, key: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') -> None:
        self._key = ''.join(dict.fromkeys(key.upper()))
        self._n = len(self._key)
        self._pkey = sorted(range(self._n), key=self._key.__getitem__)
        self._ikey = inverse(self._pkey)

        self._alpha = alphabet.upper()
        self._map = {c: tuple(map('ADFGVX'.__getitem__, divmod(i, 6))) for i, c in enumerate(self._alpha)}
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self._key, self._alpha}'

    def __str__(self) -> str:
        return '\n'.join(map('  '.join, zipper(self._alpha, 6)))

    def encode(self, plaintext: str) -> str:
        grid = TRS(grouper(chain(self._map[c] for c in plaintext.upper() if c in self._map), self._n, 'X'))
        return ''.join(chain(map(grid.__getitem__, self._pkey)))

    def decode(self, ciphertext: str) -> str:
        q, r = divmod(len(ciphertext), self._n)
        q += bool(r)
        grid = TRS(zipper(chain(map(grouper(ciphertext.upper(), q, 'X').__getitem__, self._ikey)), q))
        return ''.join(map(self._map.get, zipper(chain(grid), 2)))


def test_adfgvx():
    cipher = ADFGVX('key', 'AZERTYUIOPQSDFGHJKLMWXCVBN0123456789')
    print(cipher.encode('DCODE'), cipher.decode('ADAXFVFFGFAX'))
    cipher = ADFGVX('queenly')
    print(cipher.encode('attack at dawn'), cipher.decode('GAGGGDAFDFDVAAAAAAAADVGD'))
