class Reflector:
    def __init__(self, reflection='ZYXWVUTSRQPONMLKJIHGFEDCBA'):
        self.reflection = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', reflection))
        assert all(k == self.reflection[v] for k, v in self.reflection.items()), f'invalid reflector'

    def reflect(self, c):
        return self.reflection.get(c, c)


def test():
    #
    print(Reflector('ZYXWVUTSRQPONMLKJIHGFEDCBA').reflect('A'))
    # Reflector A
    print(Reflector('EJMZALYXVBWFCRQUONTSPIKHGD').reflect('A'))
    # Reflector B
    print(Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT').reflect('A'))
    # Reflector C
    print(Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL').reflect('A'))
    # Reflector A Thin
    print(Reflector('ENKQAUYWJICOPBLMDXZVFTHRGS').reflect('A'))
    # Reflector B Thin
    print(Reflector('RDOBJNTKVEHMLFCWZAXGYIPSUQ').reflect('A'))
