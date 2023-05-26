from itertools import cycle


class Gronsfeld:
    def __init__(self, key: int, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(key, int): raise ValueError('invalid key')
        if not isinstance(alphabet, str) or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')
        self._alpha = alphabet.upper()
        self._key = tuple(map(int, str(key)))
        self._map = dict(enumerate(self._alpha))
        self._map.update({v: k for k, v in self._map.items()})

    def cipher(self, text: str, mode: int) -> str:
        key = cycle(self._key)
        return ''.join(self._map[(self._map[c] + mode * next(key)) % 26]
                       if c in self._map else c for c in text.upper())

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, 1)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, -1)


def test_gronsfeld():
    cipher = Gronsfeld(12345)
    print(cipher.encode('attack at dawn'))
    print(cipher.decode('BVWEHL CW HFXP'))
