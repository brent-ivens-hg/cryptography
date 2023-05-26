class KeyboardSub:
    """
    SUBSTITUTION CIPHER USING THE ALPHABET/QWERTY/ALPHABET LAYOUTS AS MAPS

    alphabet <> azerty:  2 keys in common ( 4% identical) -> PARTIAL SUBSTITUTION
    alphabet <> qwerty:  0 keys in common ( 0% identical) -> FULL SUBSTITUTION
    azerty   <> qwerty: 32 keys in common (62% identical) -> PARTIAL SUBSTITUTION

    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    azerty = 'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn'
    qwerty = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

    def __init__(self):
        self.alpha2azerty = lambda s: s.translate(str.maketrans(self.alphabet, self.azerty))
        self.alpha2qwerty = lambda s: s.translate(str.maketrans(self.alphabet, self.qwerty))
        self.azerty2alpha = lambda s: s.translate(str.maketrans(self.azerty, self.alphabet))
        self.azerty2qwerty = lambda s: s.translate(str.maketrans(self.azerty, self.qwerty))
        self.qwerty2alpha = lambda s: s.translate(str.maketrans(self.qwerty, self.alphabet))
        self.qwerty2azerty = lambda s: s.translate(str.maketrans(self.qwerty, self.azerty))

    def test(self, test_string='abcdefghijklmnopqrstuvwxyz'):
        print(f'test string: {test_string}')
        print(f'alpha2azerty: {self.alpha2azerty(test_string)}')
        print(f'alpha2qwerty: {self.alpha2qwerty(test_string)}')
        print(f'azerty2alpha: {self.azerty2alpha(test_string)}')
        print(f'azerty2qwerty: {self.azerty2qwerty(test_string)}')
        print(f'qwerty2alpha: {self.qwerty2alpha(test_string)}')
        print(f'qwerty2azerty: {self.qwerty2azerty(test_string)}')


class RotSub:
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        # rotate cipher
        self.rot = lambda s, i: s.upper().translate(str.maketrans(self.ABC, self.ABC[i % 26:] + self.ABC[:i % 26]))
        # inverted rotate cipher
        self.irot = lambda s, i: s.upper().translate(
            str.maketrans(self.ABC, self.ABC[i % 26::-1] + self.ABC[:i % 26:-1]))

    def test(self, test_string=ABC):
        print(f'TEST STRING: {test_string!r}\n')
        for i in range(26):
            print(f'ROT-{i:<3}: {self.rot(test_string, i)}')
        print()
        for i in range(26):
            print(f'IROT-{i:<2}: {self.irot(test_string, i)}')


class ValueSub:
    @staticmethod
    def basal(string, base):
        assert 2 <= base <= 10, 'unsupported'
        from Personal.Math.Base import to_base
        # ASCII VALUE <base 10> => ASCII VALUE <base x>
        return ''.join([chr(to_base(ord(x), base)) for x in string])

    @staticmethod
    def debasal(string, base):
        assert 2 <= base <= 10, 'unsupported'
        # ASCII VALUE <base x> => ASCII VALUE <base 10>
        return ''.join([chr(int(str(ord(x)), base)) for x in string])

    def test(self, test_string='abcdefghijklmnopqrstuvwxyz'):
        print(f'TEST STRING: {test_string!r}\n')
        for i in range(2, 11):
            print(f'Base {i}:', a := self.basal(test_string, i))
            # print('Original:', self.debasal(a, i))


# KeyboardSub().test()
# RotSub().test()
# ValueSub().test()


class ShuffleSub:
    @staticmethod
    def encode(string, n):
        string = string.upper() + 'X' * ((n - (len(string) % n)) % n)
        return string


print(ShuffleSub.encode("xxxxx", 4))
