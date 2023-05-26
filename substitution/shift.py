from itertools import cycle, count

# TODO: (sub)class WordShift: shift every word  /W
# TODO: (sub)class NShift: shift every n characters /NC

class Shift:  # shifts every character /C
    def __init__(self, *shifts: int, increment: int = 0, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self._shifts = shifts or (0,)
        self._inc = increment
        self._map = dict(enumerate(alphabet)); self._map.update({v: k for k, v in self._map.items()})

    def encode(self, plaintext: str) -> str: return self._cipher(plaintext, 1)
    def decode(self, ciphertext: str) -> str: return self._cipher(ciphertext, -1)

    def _cipher(self, text: str, mode: int):
        assert abs(mode) == 1
        res = []
        shift = cycle(self._shifts)
        inc = count(0, self._inc)
        for c in text.upper():  # index [+|-] (shift + increment)
            if c in self._map: res.append(self._map[(self._map[c] + mode * (next(shift) + next(inc))) % 26])
            else: res.append(c)
        return ''.join(res)

def test_shift():
    cipher = Shift(3)
    print('caesar shift (3)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('DWWDFN DW GDZQ'))
    cipher = Shift(1, 2, 3)
    print('\nmulti-shifting (1, 2, 3, 1, 2, 3 ...)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('BVWBEN BV GBYQ'))
    cipher = Shift(increment=1)
    print('\nprogressive shifting (0, 1, 2, 3, 4, 5 ...)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('AUVDGP GA LJGY'))
    print('\nprogressive shifting (1, 2, 3, 4, 5, 6 ...)')
    cipher = Shift(1, increment=1)
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('BVWEHQ HB MKHZ'))
    cipher = Shift(0, 1, 2, increment=1)
    print('\nmulti-progressive shifting (0, 2, 4, 3, 5, 7 ...)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('AVXDHR GB NJHA'))
    cipher = Shift(-1, increment=-1)
    print('\ndegressive shifting (-1, -2, -3, -4, -5, -6 ...)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('ZRQWXE TL UQLB'))
    cipher = Shift(1, -1)
    print('\nalternate shifting (1, -1, 1, -1, 1, -1 ...)')
    print(cipher.encode('ATTACK AT DAWN'), '<>', cipher.decode('BSUZDJ BS EZXM'))

test_shift()