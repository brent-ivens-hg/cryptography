from math import gcd
from typing import Any

class Affine:
    """
    Encryption uses a classic alphabet, and two integers, called coefficients (or keys) A and B,
    these are the parameters of the affine function Ax + B.
    """

    def __init__(self, A: int, B: int) -> None:
        """
        :param A: coefficient A (coprime to M=26)
        :param B: coefficient B
        """
        self.A = A % 26
        self.B = B % 26
        self._map = dict(enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.A, self.B}'

    def __setattr__(self, key: str, value: Any) -> None:
        if key in ('A', 'B') and not isinstance(value, int): raise TypeError('coefficient must be integer')
        if key == 'A':
            if gcd(value, 26) != 1: raise ValueError(f'A={value} must be coprime to M=26')
            self._A = pow(value, -1, 26)  # modular inverse
        super().__setattr__(key, value)

    def encode(self, plaintext: str) -> str:
        """ y = Ax + B mod 26 """
        return ''.join(self._map[(self.A * self._map[c] + self.B) % 26] for c in plaintext.upper() if c.isalpha())

    def decode(self, ciphertext: str) -> str:
        """ x = A⁻¹ * (y - B) mod 26 """
        return ''.join(self._map[(self._A * (self._map[c] - self.B)) % 26] for c in ciphertext.upper() if c.isalpha())


def test_affine():
    cipher = Affine(1, 20)
    print('A  B  ENCODED      DECODED')
    for i in range(26):
        if gcd(i, 26) == 1:  # coprime
            cipher.A = i
            encoded = cipher.encode('ATTACK AT DAWN')
            print(f'{cipher.A:<2} {cipher.B} {encoded} {cipher.decode(encoded)}')
