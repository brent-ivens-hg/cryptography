class Disk:
    def __init__(self, alphabet: str) -> None:
        self.alpha = alphabet.upper()
        if set(self.alpha) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.alpha!r})'

    def __str__(self) -> str:
        return self.alpha

    def __getitem__(self, item: int) -> str:
        return self.alpha[item]

    def index(self, *args, **kwargs) -> int:
        return self.alpha.index(*args, **kwargs)

    def rotate(self, count: int) -> None:
        self.alpha = self[count % 26:] + self[:count % 26]
        return self

    def roll(self, start: int, stop: int) -> None:
        self.alpha = self[:start - 1] + self[start:stop] + self[start - 1] + self[stop:]
        return self


class Chao:
    def __init__(self, left_alphabet: str, right_alphabet) -> None:
        self.left = Disk(left_alphabet)
        self.right = Disk(right_alphabet)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.left, self.right}'

    def __str__(self) -> str:
        return f'''\
            +            *
 LEFT (ct): {self.left}
RIGHT (pt): {self.right}
            --------------------------
  Position: 12345678911111111112222222
                     01234567890123456'''

    def permute(self, index) -> None:
        self.left.rotate(index).roll(2, 14)
        self.right.rotate(index + 1).roll(3, 14)

    def _enc(self, char: str) -> str:
        idx = self.right.index(char)
        char = self.left[idx]
        self.permute(idx)
        return char

    def _dec(self, char: str) -> str:
        idx = self.left.index(char)
        char = self.right[idx]
        self.permute(idx)
        return char

    def encode(self, plaintext: str) -> str:
        return ''.join(self._enc(c) if c.isalpha() else c for c in plaintext.upper())

    def decode(self, ciphertext: str) -> str:
        return ''.join(self._dec(c) if c.isalpha() else c for c in ciphertext.upper())


def test_chao():
    cipher = Chao('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(cipher.encode('ATTACK AT DAWN'))
    cipher = Chao('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(cipher.decode('ASRXZS UN ITWC'))
