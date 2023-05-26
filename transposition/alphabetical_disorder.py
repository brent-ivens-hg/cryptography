from collections.abc import Callable, Generator, Iterable
from itertools import chain
from operator import le
from random import sample
from typing import TypeVar

_T = TypeVar('_T')

shuffled = lambda population: sample(population, k=len(population))
chain = chain.from_iterable


def segment(iterable: Iterable[_T],
            cmp_func: Callable[[_T, _T], bool],
            ord_func: Callable[[Iterable[_T]], Iterable[_T]]
            ) -> Generator[_T, None, None]:
    it = iter(iterable)
    prev = next(it)
    segment_ = [prev]
    for curr in it:
        if cmp_func(prev, curr):
            segment_.append(curr)
        else:
            yield ord_func(segment_)
            segment_ = [curr]
        prev = curr
    yield ord_func(segment_)


class AlphaDis:
    """
    Alphabetical Disorder
    """

    def __init__(self, shuffle: bool = False) -> None:
        self._shuffle = bool(shuffle)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(shuffle={self._shuffle!r})'

    def encode(self, plaintext: str) -> str:
        return ' '.join(map(''.join, segment(
            iterable=filter(str.isalpha, plaintext.upper()),
            cmp_func=le,
            ord_func=shuffled if self._shuffle else reversed
        )))

    @staticmethod
    def decode(ciphertext: str) -> str:
        return ''.join(chain(sorted(filter(str.isalpha, segment_)) for segment_ in ciphertext.split()))


def test_alphadis():
    cipher = AlphaDis()
    print(cipher.encode('ALPHABET'), cipher.decode('PLA H TEBA'))
    print(cipher.encode('ATTACK AT DAWN'), cipher.decode('TTA KCA TA D WA N'))
    print()
    cipher = AlphaDis(shuffle=True)
    encoded = cipher.encode('ALPHABET')
    print(encoded, cipher.decode(encoded))
    encoded = cipher.encode('ATTACK AT DAWN')
    print(encoded, cipher.decode(encoded))
    print(cipher.decode('ATTACKATDAWN'))
