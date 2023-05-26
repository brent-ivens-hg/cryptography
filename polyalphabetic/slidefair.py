from itertools import cycle

class Slidefair:
    """Slidefair encryption uses an encryption key (as well as an alphabet) and is performed by bigrams"""

    def __init__(self, key: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(key, str) and key.isalpha(): raise ValueError('invalid key')
        if not isinstance(alphabet, str) or len(alphabet) != 26 or set(alphabet.upper()) != set(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'): raise ValueError('invalid alphabet')

        self._key = key.upper()
        self._alpha = alphabet.upper()
        self._map = dict(enumerate(self._alpha))
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self):
        return f'{self.__class__.__name__}{self._key, self._alpha}'

    def cipher(self, text: str) -> str:
        bigrams = zip(*[iter(filter(str.isalpha, text.upper() + 'X'))] * 2)
        return ''.join(self._map[(self._map[b] - k) % 26] + self._map[(self._map[a] + k) % 26]
                       for (a, b), k in zip(bigrams, cycle(map(self._map.get, self._key))))

    def encode(self, plaintext: str) -> str: return self.cipher(plaintext)
    def decode(self, ciphertext: str) -> str: return self.cipher(ciphertext)

def test_slidefair():
    cipher = Slidefair('QUEENLY')
    print(cipher.encode('attack at dawn'))
    print(cipher.decode('DQ GN GG PE NQ CH'))
