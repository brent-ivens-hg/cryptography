from itertools import count

class Trithemius:
    def __init__(self,
                 init_shift: int = 0,
                 descending: bool = False,
                 alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 ) -> None:

        if not isinstance(init_shift, int) or not isinstance(descending, bool) or not isinstance(alphabet, str):
            raise TypeError
        if len(alphabet) != 26 or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')

        self._init_shift = init_shift
        self._desc = descending
        self._alpha = alphabet.upper()
        self._map = dict(enumerate(self._alpha))
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self):
        return f'{self.__class__.__name__}{self._init_shift, self._alpha}'

    def cipher(self, text: str, init_shift: int, shift: int) -> str:
        shift = count(init_shift, shift)
        return ''.join(self._map[(self._map[c] + next(shift)) % 26] if c.isalpha() else c for c in text.upper())

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, self._init_shift, -1 if self._desc else 1)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, -self._init_shift, 1 if self._desc else -1)

def test_trithemius():
    cipher = Trithemius()
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('AUVDGP GA LJGY'))
    cipher = Trithemius(12, descending=True)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('MEDJKR GY HDYO'))
