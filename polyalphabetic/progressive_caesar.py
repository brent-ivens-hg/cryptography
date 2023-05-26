class ProgressiveCaesar:
    def __init__(self, n: int = 1, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(n, int) or not isinstance(alphabet, str):
            raise TypeError
        if len(alphabet) != 26 or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabets')

        self._n = n
        self._alpha = alphabet.upper
        self._map = dict(enumerate(alphabet))
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self):
        return f'{self.__class__.__name__}{self._n, self._alpha}'

    def cipher(self, text: str, mode: int) -> str:
        inc = 1 if mode * self._n > 0 else -1 if mode * self._n < 0 else 0
        i, shift, res = 0, inc, []
        for c in text.upper():
            if c.isalpha():
                c = self._map[(self._map[c] + shift) % 26]
                i += 1
                if i % self._n == 0: shift += inc
            res.append(c)
        return ''.join(res)

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, 1)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, -1)


def test_progressive_caesar():
    cipher = ProgressiveCaesar()
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('BVWEHQ HB MKHZ'))
    cipher = ProgressiveCaesar(3)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('BUUCEM DW GEAR'))
    cipher = ProgressiveCaesar(-3)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('ZSSYAI XQ AWSJ'))
