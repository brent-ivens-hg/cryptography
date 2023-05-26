from collections.abc import Callable, Generator, Iterable
from itertools import accumulate, tee
from operator import sub
from typing import TypeVar

_T = TypeVar('_T')


def decumulate(iterable: Iterable[_T], func: Callable[[_T, _T], _T] = sub) -> Generator[_T, None, None]:
    """Return series of differences (or other binary function results)."""
    t1, t2 = tee(iter(iterable))
    yield from (next(t1), *map(func, t1, t2))


class ARA:
    """
    Substitution with alphabetical ranks and basic arithmetic.
    This is a variant of the alphabetical rank cipher A1Z26 (A=1, B=2, C=3 etc.)
    but accumulates the rank values (A=1, B=2+A=3, C=3+B=6 etc.)
    """

    def __init__(self, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        """
        :param alphabet: rank values correspond to index ('ABC' -> A=0, B=1, C=2)
        """
        if not isinstance(alphabet, str) or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')
        self._alpha = alphabet.upper()
        self._map = dict(enumerate(self._alpha));
        self._map.update({v: k for k, v in self._map.items()})

    def __repr__(self) -> str: return f'{self.__class__.__name__}({self._alpha!r})'

    def cipher(self, text: str, func: Callable[[Iterable[int]], Generator[int, None, None]]) -> str:
        return ''.join(self._map[x % 26] for x in func(self._map[c] for c in text.upper() if c in self._map))

    def encode(self, plaintext: str) -> str:
        """
        :param plaintext: unencrypted text
        :return: encrypted text
        """
        return self.cipher(plaintext, accumulate)

    def decode(self, ciphertext: str) -> str:
        """
        :param ciphertext: encrypted text
        :return: unencrypted text
        """
        return self.cipher(ciphertext, decumulate)


def test_ara():
    cipher = ARA()
    print(cipher)
    print(cipher.encode('ATTACK AT DAWN'), cipher.decode('ATMMOY YR UUQD'), '\n')

    cipher = ARA('ZYXWVUTSRQPONMLKJIHGFEDCBA')
    print(cipher)
    print(cipher.encode('ATTACK AT DAWN'), cipher.decode('AUOPSD EY CDAO'), '\n')

    cipher = ARA('JIXFVWKRYMOTUDCZHQNBSPGEAL')
    print(cipher)
    print(cipher.encode('ATTACK AT DAWN'), cipher.decode('AMSNKUOPYKTF'))
