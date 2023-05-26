from itertools import cycle
from random import choice
from string import digits

class VIC:
    def __init__(self,
                 digit1: int,
                 digit2: int,
                 alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ./',
                 key: str = None
                 ) -> None:

        if not isinstance(digit1, int) or not isinstance(digit2, int): raise TypeError
        if not isinstance(alphabet, str) or (key is not None and not isinstance(key, str)): raise TypeError
        if digit1 == digit2 or not (0 <= digit1 <= 9) or not (0 <= digit2 <= 9): raise ValueError('invalid digit(s)')
        if len(alphabet) != 28 or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ./'):
            raise ValueError('invalid alphabet')
        if key is not None and not key.isdigit(): raise ValueError('invalid key')

        self.dig1, self.dig2 = (digit1, digit2) if digit1 < digit2 else (digit2, digit1)
        self.alpha = alphabet.upper()
        self.key = key

        self.board = tuple(zip(*[iter(
            self.alpha[:self.dig1] + ' ' + self.alpha[self.dig1:self.dig2 - 1] + ' ' + self.alpha[self.dig2 - 1:]
        )] * 10))
        self.map = {col: str(idx if dig is None else dig * 10 + idx)
                    for dig, row in zip((None, self.dig1, self.dig2), self.board)
                    for idx, col in enumerate(row) if not col.isspace()}
        self.map.update({v: k for k, v in self.map.items()})

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.dig1!r}, {self.dig2!r}, {self.alpha!r}, {self.key})'

    def __str__(self) -> str:
        return '\n'.join(' '.join((prefix, *row)) for prefix, row in
                         zip(f'  {self.dig1}{self.dig2}', (tuple(digits), *self.board)))

    def keyshift(self, digits: str, mode: int) -> str:
        return ''.join(str((int(d) + mode * k) % 10) for d, k in zip(digits, cycle(map(int, self.key))))

    def cipher(self, text: str) -> str:
        res = []
        while text:
            i = 2 if text[:2] in self.map else 1
            res.append(self.map.get(text[:i], text[:i]))
            text = text[i:]
        return ''.join(res)

    def encode(self, plaintext: str, output_letters: bool = False) -> str:
        encoded = ''.join(self.map[c] for c in plaintext if c in self.map)
        if self.key: encoded = self.keyshift(encoded, 1)
        if output_letters and int(encoded[-1:]) in {self.dig1, self.dig2}: encoded += choice(digits)
        return self.cipher(''.join(encoded)) if output_letters else ''.join(encoded)

    def decode(self, ciphertext: str) -> str:
        decoded = ciphertext if ciphertext.isdigit() else ''.join(map(self.map.get, ciphertext))
        return self.cipher(self.keyshift(decoded, -1) if self.key else decoded)

def test_vic():
    cipher = VIC(2, 6, './ZYXWVUTSRQPONMLKJIHGFEDCBA')
    print(cipher.encode('VICTOR'))
    print(cipher.decode('86167202522'))

    cipher = VIC(2, 6, './ZYXWVUTSRQPONMLKJIHGFEDCBA', '0248')
    print(cipher.encode('VICTOR'))
    print(cipher.decode('885474405460'))
    print(cipher.encode('VICTOR', output_letters=True))
    print(cipher.decode('VVXYWYY.XYJ'))

    cipher = VIC(4, 8)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('081810242081308445'))

    cipher = VIC(4, 8, key='162044131124')
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('143854373105460489'))
    print(cipher.encode('ATTACK AT DAWN', output_letters=True))
    print(cipher.decode('BLXLGDBAEOAQH'))
