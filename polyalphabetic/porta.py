from collections.abc import Sequence
from itertools import cycle

_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

_PAIRS = 'AB CD EF GH IJ KL MN OP QR ST UV WX YZ'.split()

_A1 = ('NOPQRSTUVWXYZABCDEFGHIJKLM', 'ZNOPQRSTUVWXYBCDEFGHIJKLMA', 'YZNOPQRSTUVWXCDEFGHIJKLMAB',
       'XYZNOPQRSTUVWDEFGHIJKLMABC', 'WXYZNOPQRSTUVEFGHIJKLMABCD', 'VWXYZNOPQRSTUFGHIJKLMABCDE',
       'UVWXYZNOPQRSTGHIJKLMABCDEF', 'TUVWXYZNOPQRSHIJKLMABCDEFG', 'STUVWXYZNOPQRIJKLMABCDEFGH',
       'RSTUVWXYZNOPQJKLMABCDEFGHI', 'QRSTUVWXYZNOPKLMABCDEFGHIJ', 'PQRSTUVWXYZNOLMABCDEFGHIJK',
       'OPQRSTUVWXYZNMABCDEFGHIJKL')

_A2 = ('NOPQRSTUVWXYZABCDEFGHIJKLM', 'OPQRSTUVWXYZNMABCDEFGHIJKL', 'PQRSTUVWXYZNOLMABCDEFGHIJK',
       'QRSTUVWXYZNOPKLMABCDEFGHIJ', 'RSTUVWXYZNOPQJKLMABCDEFGHI', 'STUVWXYZNOPQRIJKLMABCDEFGH',
       'TUVWXYZNOPQRSHIJKLMABCDEFG', 'UVWXYZNOPQRSTGHIJKLMABCDEF', 'VWXYZNOPQRSTUFGHIJKLMABCDE',
       'WXYZNOPQRSTUVEFGHIJKLMABCD', 'XYZNOPQRSTUVWDEFGHIJKLMABC', 'YZNOPQRSTUVWXCDEFGHIJKLMAB',
       'ZNOPQRSTUVWXYBCDEFGHIJKLMA')

class Porta:
    def __init__(self, key: str, alphabets: Sequence[str] = _A1) -> None:
        if not isinstance(key, str): raise TypeError('key must be str')
        if not key.isalpha(): raise ValueError('invalid key')
        if len(alphabets) != 13 or not all(
                isinstance(alpha, str) and len(alpha) == 26 and set(alpha.upper()) == set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                for alpha in alphabets): raise ValueError('invalid alphabets')

        self.key = key.upper()
        self.alphabets = tuple(map(str.upper, alphabets))
        self.map = {c: str.maketrans(_ALPHA, alphabets[i // 2]) for i, c in enumerate(_ALPHA)}

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.key!r})'

    def __str__(self):
        return '     ' + ' '.join(_ALPHA) + '\n\n' + '\n'.join(
            map('   '.join, zip(_PAIRS, map(' '.join, self.alphabets))))

    def cipher(self, text: str) -> str:
        k = cycle(map(self.map.get, self.key))
        return ''.join(c.translate(next(k)) if c.isalpha() else c for c in text.upper())

    def encode(self, plaintext: str) -> str: return self.cipher(plaintext)
    def decode(self, ciphertext: str) -> str: return self.cipher(ciphertext)

def test_porta():
    cipher = Porta('Queenly')
    print(cipher)
    print(cipher.encode('attack at dawn'))
    print(cipher.decode('SDIYWS OB TYLG'))
