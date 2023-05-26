from itertools import zip_longest


class Scytale:
    def __init__(self, turns: int, isalpha: bool = False) -> None:
        self._turns = turns
        self._isalpha = isalpha

    def encode(self, plaintext: str) -> str:
        plaintext = plaintext.upper()
        plaintext = (c if c.isalpha() else '_' for c in plaintext) if self._isalpha else filter(str.isalpha, plaintext)
        return ''.join(map(''.join, zip(*zip_longest(*[plaintext] * self._turns, fillvalue='_'))))

    def decode(self, ciphertext: str) -> str:
        return ''.join(map(''.join, zip(*zip(*[iter(ciphertext.upper())] * (len(ciphertext) // self._turns)))))


def test_scytale():
    cipher = Scytale(3)
    print(cipher.encode('attack at dawn'), cipher.decode('AAAATCTWTKDN'))
    cipher = Scytale(4)
    print(cipher.encode('attack at dawn'), cipher.decode('ACDTKATAWATN'))
    cipher = Scytale(5)
    print(cipher.encode('attack at dawn'), cipher.decode('AKWTANTT_AD_CA_'))
    cipher = Scytale(5, isalpha=True)
    print(cipher.encode('attack at dawn'), cipher.decode('AKDT_ATAWATNC__'))
    cipher = Scytale(6)
    print(cipher.encode('attack at dawn'), cipher.decode('AATTTDAACWKN'))
