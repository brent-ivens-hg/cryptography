from collections.abc import Callable, Sequence
from itertools import cycle


def nsplit(seq: Sequence, n: int) -> list:
    return [seq[i:i + n] for i in range(0, len(seq), n)]


class Phillips:
    def __init__(self,
                 n: int = 5,
                 row_shift: int = 1,
                 col_shift: int = 1,
                 alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'):

        if not (isinstance(n, int) and isinstance(row_shift, int) and isinstance(col_shift, int)):
            raise TypeError
        if not (isinstance(alphabet, str) and len(alphabet) == len(set(alphabet)) == 25):
            raise ValueError('invalid alphabet')

        self.n, self.rshift, self.cshift, self.alpha = n, row_shift, col_shift, alphabet
        # shift functions
        self.shift = lambda r, c: ((r + row_shift) % 5, (c + col_shift) % 5)
        self.unshift = lambda r, c: ((r - row_shift) % 5, (c - col_shift) % 5)
        # polybius squares / mapping
        self.grids = self.generate_grids()
        self.maps = tuple(
            {**{c: divmod(i, 5) for i, c in enumerate(m)}, **{divmod(i, 5): c for i, c in enumerate(m)}}
            for m in map(''.join, self.grids)
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.n, self.rshift, self.cshift, self.alpha}'

    def __str__(self) -> str:
        return '\t' + '\t\t\t'.join('12345678') + '\n' + '\n'.join(map(' '.join, map(' '.join, zip(*self.grids))))

    def generate_grids(self) -> tuple[tuple[str, ...], ...]:
        G = nsplit(self.alpha, 5)
        return ((G[0], G[1], G[2], G[3], G[4]), (G[1], G[0], G[2], G[3], G[4]),
                (G[2], G[1], G[0], G[3], G[4]), (G[3], G[1], G[2], G[0], G[4]),
                (G[4], G[1], G[2], G[3], G[0]), (G[1], G[4], G[2], G[3], G[0]),
                (G[2], G[1], G[4], G[3], G[0]), (G[3], G[1], G[2], G[4], G[0]))

    def cipher(self, text: str, shift_func: Callable[[int, int], tuple[int, int]]) -> str:
        res, map_ = [], cycle(self.maps)
        for block in nsplit(list(filter(self.alpha.__contains__, text.upper())), self.n):
            m = next(map_)
            res += [m[shift_func(*m[c])] for c in block]
        return ''.join(res)

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, self.shift)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, self.unshift)


def test_phillips():
    # print(Phillips(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXY'))
    cipher = Phillips()
    print(cipher)
    print(cipher.encode('attack at dawn'))
    print(cipher.decode('GZZGI AMZPM NI'))
