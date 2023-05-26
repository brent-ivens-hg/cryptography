from collections.abc import Sequence
from itertools import chain, cycle, accumulate
from typing import TypeVar

_T = TypeVar('_T')

chain = chain.from_iterable


# FIXME: Duplicated code
def inverse(permutation: Sequence[int]) -> list[int]:
    res = [0] * len(permutation)
    for i, p in enumerate(permutation): res[p] = i
    return res


class AMSCO:  # TODO: FIX encode, IMPLEMENT decode
    def __init__(self, key: str, *sequence: int) -> None:
        self.key = ''.join(dict.fromkeys(key.upper()))
        self.n = len(self.key)
        self.pkey = sorted(range(self.n), key=self.key.__getitem__)
        self.ikey = inverse(self.pkey)
        self.seq = sequence or (1,)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.key, *self.seq}'

    def sequentialize(self, text: str):
        res, n = [], len(text)
        for _, i in zip(text, cycle(self.seq)):
            if n < i:
                if n > 0: res.append(n)
                break
            n -= i
            res.append(i)
        return res

    def encode(self, plaintext: str) -> str:
        plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
        idxs = list(accumulate(self.sequentialize(plaintext), initial=0))
        cuts = [plaintext[start:end] for start, end in zip(idxs, idxs[1:])]
        print(cuts)
        print([cuts[i:i + self.n] for i in range(0, len(cuts), self.n)])
        grid = [cuts[i::self.n] for i in range(self.n)]
        print(grid)
        return ''.join(chain(map(grid.__getitem__, self.pkey)))

    def decode(self, ciphertext: str) -> str:
        ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
        idxs = list(accumulate(self.sequentialize(ciphertext), initial=0))
        return idxs


# cipher = AMSCO('KEY', 1, 2)
# print(cipher.encode('dcodeamsco'))
# print(cipher.decode('COMDEAODSC'))
cipher = AMSCO('KEY', 2, 1)
print(cipher.encode('dcodeamsco'))
