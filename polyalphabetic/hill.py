from collections.abc import Iterable
from itertools import chain
from math import gcd
from sympy import Matrix

chain = chain.from_iterable

def grouper(iterable: Iterable, n: int) -> tuple:
    return tuple(zip(*[iter(iterable)] * n))

class Hill:
    def __init__(self, matrix: list, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if set(alphabet) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')
        if not all(len(matrix) == len(row) and all(isinstance(col, int) for col in row) for row in matrix):
            raise ValueError('invalid matrix')

        self._alpha = alphabet.upper()
        self._n = len(matrix)
        self._map = dict(enumerate(self._alpha)); self._map.update({c: i for i, c in self._map.items()})
        self._mat = Matrix(matrix)

        if gcd(self._mat.det(), 26) != 1:
            raise ValueError('matrix determinant has to be coprime with 26')

        self._inv = Matrix(matrix).inv_mod(26)

    def cipher(self, text: str, matrix: list) -> str:
        text = text.upper() + 'Z' * (self._n - 1)
        ngrams = grouper((self._map[c] for c in text if c in self._map), self._n)
        return ''.join(chain(
            [self._map[i % 26] for i in chain((matrix * Matrix(grouper(ngram, 1))).tolist())]
            for ngram in ngrams
        ))

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, self._mat)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, self._inv)

def test_hill():
    cipher = Hill([[9, 0, 1], [3, 2, 0], [1, 5, 1]])
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('TMKKEU DM UNST'))
