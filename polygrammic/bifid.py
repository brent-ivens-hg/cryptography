from collections.abc import Iterable, Generator
from itertools import chain

chain = chain.from_iterable


class Bifid:
    def __init__(self, key: str = '') -> None:
        key = self._format_key(key) + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._key = ''.join(dict.fromkeys(key.replace('J', 'I')))[:25]
        self._map = {c: divmod(i, 5) for i, c in enumerate(self._key)}  # char -> coord
        self._map.update({v: k for k, v in self._map.items()}, J=self._map['I'])  # coord -> char

    def __repr__(self) -> str: return f'{self.__class__.__name__}({self._key!r})'

    def __str__(self) -> str: return '\n'.join(map(' '.join, zip(*[iter(self._key)] * 5)))

    @staticmethod
    def _format_key(key: str) -> str: return ''.join(filter(str.isalpha, key)).upper()

    @staticmethod
    def _defractionate(iterable: Iterable) -> zip:
        t = tuple(chain(iterable))
        return zip(*[iter(t)] * (len(t) // 2))

    @staticmethod
    def _fractionate(iterable: Iterable) -> zip: return zip(*[iter(chain(iterable))] * 2)

    @staticmethod
    def _transpose(iterable: Iterable) -> zip: return zip(*iterable)

    def _substitute(self, iterable: Iterable) -> Generator: return (self._map[x] for x in iterable if x in self._map)

    def encode(self, plaintext: str) -> str:
        chars = plaintext.upper()
        encoded = self._substitute(self._fractionate(self._transpose(self._substitute(chars))))
        return ''.join(encoded)

    def decode(self, ciphertext: str) -> str:
        chars = ciphertext.upper()
        decoded = self._substitute(self._transpose(self._defractionate(self._substitute(chars))))
        return ''.join(decoded)


def test_bifid():
    Bifid()
    cipher = Bifid('CRYPTOGRAPHY')
    print(repr(cipher))
    print(cipher)
    print(cipher.encode('FELIX DELASTELLE'))
    print(cipher.encode('FELJX DELASTELLE'))
    print(cipher.decode('FNWJH YQFOQRYZOR'))
    print(cipher.decode('FNWIH YQFOQRYZOR'))
