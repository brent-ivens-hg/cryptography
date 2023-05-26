from collections.abc import Hashable, Iterable, Sequence
from itertools import cycle
from operator import add
from typing import TypeVar

_T = TypeVar('_T')


def TRS(seq: Sequence[_T], columns: int) -> tuple[Sequence[_T], ...]:
    """ Equivalent w/ splitting sequence in groups of length <columns> and transposing """
    return tuple(seq[i::columns] for i in range(columns))


class Bellaso:
    def __init__(self,
                 cip_key: str = 'CHIAVE',
                 alphabet: str = 'ABCDEFGHILMNOPQRSTVX',
                 n: int = 5,
                 shift: int = 1,
                 gen_key: str = 'IOVE'):
        if not (type(cip_key) == type(gen_key) == type(alphabet) == str and type(n) == type(n) == int):
            raise TypeError
        if len(alphabet) != len(set(alphabet.upper())): raise ValueError('invalid alphabet')
        if n < 1 or shift < 1: raise ValueError('value cannot be less than 1')

        key, alphabet, gen_key = map(str.upper, (cip_key, alphabet, gen_key))

        self._alphabet = alphabet
        self._cip_key = cip_key  # cipher key
        self._gen_key = gen_key  # alphabet generating key
        self._n = n  # number of alphabets to generate
        self._shift = shift  # shift between each alphabet

        self._alphabets = self.generate_alphabets(n, shift, gen_key, alphabet)
        self._rows = TRS(''.join(self._alphabets[0]), n)
        self._map = self.generate_map(self._rows, self._alphabets)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self._cip_key, self._alphabet, self._n, self._shift, self._gen_key}'

    def __str__(self) -> str:
        return '\n'.join(' '.join(row) + ' > ' + '/'.join(alpha) for row, alpha in zip(self._rows, self._alphabets))

    @staticmethod
    def generate_alphabets(n: int, shift: int, key: str, alphabet: str) -> list[tuple[str, str]]:
        """ Generates n semi-caesar-shifted alphabets """

        def split_half(seq: str, left: bool = False) -> tuple[str, str]:
            """ Splits sequence in half and remainder to left/right-side """
            n = len(seq) // 2 + len(seq) % 2 * bool(left)
            return seq[:n], seq[n:]

        def rotate(seq: str, n: int) -> str:
            """ Rotates sequence n times """
            m = len(seq)
            return seq[n % m:] + seq[:n % m]

        key = ''.join(dict.fromkeys(key.upper()))
        a, b = map(add, split_half(key, left=len(key) % 2 == 1), split_half(''.join(c for c in alphabet if c not in key)))
        c = a[-1] * (len(a) - len(b))
        return [(a, rotate(b, i) + c) for i in range(0, n * shift, shift)]

    @staticmethod
    def generate_map(keys: Iterable[Iterable[Hashable]], alphabets: Iterable[tuple[str, str]]) -> dict:
        """ Maps each key to its corresponding table """
        tables = (str.maketrans(a + b, b + a) for a, b in alphabets)
        return {key: table for keys, table in zip(keys, tables) for key in keys}

    def cipher(self, text: str) -> str:
        k = cycle(self._cip_key)
        return ' '.join(s.translate(self._map[next(k)]) for s in text.upper().split())

    def encode(self, plaintext: str) -> str: return self.cipher(plaintext)
    def decode(self, ciphertext: str) -> str: return self.cipher(ciphertext)


def test_bellaso():
    cipher = Bellaso()
    print(cipher.encode('DCODE ME'), 'XTQXG LH')

    cipher = Bellaso('CHIAVE', 'ABCDEFGHILMNOPQRSTVX', 5, 1, 'CHIAVEALPHABET')
    print(cipher.encode('DCODE ME'), 'OEDOC XN')

    cipher = Bellaso('CHIAVE', 'ABCDEFGHILMNOPQRSTVX', 5, 5, 'CHIAVEALPHABET')
    print(cipher.encode('DCODE ME'), 'OEDOC BD')

    cipher = Bellaso('QUEENLY', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5, 1, 'QUEENLYALPHABET')
    print(cipher.encode('attack at dawn'), 'BVVBEED TCC ONHO')
