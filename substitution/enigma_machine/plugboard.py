class Plugboard:
    def __init__(self, wires=''):
        n = len(wires)
        assert n <= 20 and n % 2 == 0 and n == len(set(wires)), 'incorrect wiring'
        self.wires = wires
        self.pairs = ' '.join(map(''.join, zip(*[iter(wires)] * 2)))
        wires += wires[::-1]
        self.table = str.maketrans(wires[::2], wires[1::2])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.wires!r})'

    def __str__(self):
        return self.pairs

    def process(self, c):
        return c.translate(self.table)
