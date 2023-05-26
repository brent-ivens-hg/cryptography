from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import cycle, islice, repeat
from math import lcm
from operator import add, sub, mul, floordiv


class Beaufort:
    def __init__(self, key: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(key, str): raise ValueError('invalid key')
        if not (isinstance(alphabet, str) and len(alphabet) == 26
                and set(alphabet.upper()) == set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')): raise ValueError('invalid alphabet')
        self.key = key.upper()
        self._alpha = alphabet.upper()
        self._map = dict(enumerate(self._alpha))
        self._map.update({v: k for k, v in self._map.items()})

    __repr__ = lambda self: f'{self.__class__.__name__}{self.key, self._alpha}'
    __str__ = lambda self: f'{self.__class__.__name__}({self.key!r})'
    __eq__ = lambda self, other: isinstance(other, Beaufort) and self.key == other.key
    __add__ = __radd__ = lambda self, other: self.arithmetic(other, add)
    __sub__ = __rsub__ = lambda self, other: self.arithmetic(other, sub)
    __mul__ = __rmul__ = lambda self, other: self.arithmetic(other, mul)
    __floordiv__ = __rfloordiv__ = lambda self, other: self.arithmetic(other, floordiv)

    def arithmetic(self, other: Beaufort | int, func: Callable[[int, int], int]) -> Beaufort:
        """
        Calculates new Beaufort object, based on :param other: (int or Beaufort) and :param func: (binary operation)
        """
        return Beaufort(self.key_gen(other, func) if isinstance(other, Beaufort) else
                        self.apply(zip(self.key, repeat(self._map[other])), func))

    def apply(self, iterable: Iterable[tuple[str, str]], func: Callable[[int, int], int]) -> str:
        """
        Applies :param func: to :param iterable:
        """
        return ''.join(self._map[func(self._map[x], self._map[y]) % 26] for x, y in iterable)

    def key_gen(self, other: Beaufort, func: Callable[[int, int], int]) -> str:
        """
        Generates new key                   e.g. SECRET + WORD
        :key-length: lcm(a, b)                   S E C R E T S E C R E T
        :key-values: func(a, b) % 26             W O R D W O R D W O R D
                                                 ----------------------- (+) mod 26
                                                 O S T U A H J H Y F V W
        """
        return self.apply(islice(zip(cycle(self.key), cycle(other.key)), lcm(len(self.key), len(other.key))), func)

    def cipher(self, text: str) -> str:
        return self.apply(zip(cycle(self.key), filter(self._map.__contains__, text.upper())), sub)

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext)


def test_beaufort():
    # cipher
    print(Beaufort('queenly').encode('attack at dawn'))
    print(Beaufort('queenly').decode('qblelb yx reia'))
    # addition
    print(Beaufort('SECRET') + 3, 3 + Beaufort('SECRET'))
    print(Beaufort('SECRET') + Beaufort('WORD'))
    # subtraction
    print(Beaufort('SECRET') - 3, 3 - Beaufort('SECRET'))
    print(Beaufort('SECRET') - Beaufort('WORD'))
    # multiplication
    print(Beaufort('SECRET') * 3, 3 * Beaufort('SECRET'))
    print(Beaufort('SECRET') * Beaufort('WORD'))
    # division
    print(Beaufort('SECRET') // 3, 3 // Beaufort('SECRET'))
    print(Beaufort('SECRET') // Beaufort('WORD'))
