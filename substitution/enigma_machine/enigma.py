from string import ascii_uppercase as alpha
from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor


class Enigma:
    def __init__(self, rotors=(Rotor(), Rotor(), Rotor()), reflector=Reflector(), plugboard=Plugboard()):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

        self.reflect = self.reflector.reflect
        self.plug = self.plugboard.process

    def __repr__(self):
        return f'{self.__class__.__name__}{*self.rotors, self.reflector, self.plugboard}'

    def __str__(self):
        r1, r2, r3 = self.rotors
        return f'{r1.rotations:02}-{r2.rotations:02}-{r3.rotations:02}'

    def reset(self):
        for rotor in self.rotors:
            rotor.reset()
        return self

    def revolve(self, c, reverse=False):
        rotors = reversed(self.rotors) if reverse else self.rotors
        for rotor in rotors:
            c = rotor.process(c, reverse=reverse)
        return c

    def rotate_rotors(self, r=1):
        self.rotors[0].rotate(r)
        if self.rotors[0].rotations == 26:
            self.rotors[0].rotations = 0
            self.rotors[1].rotate(r)
            if self.rotors[1].rotations == 26:
                self.rotors[1].rotations = 0
                self.rotors[2].rotate(r)

    def _process(self, c, r=1):
        c = self.plug(self.revolve(self.reflect(self.revolve(self.plug(c), reverse=False)), reverse=True))
        if c.isupper(): self.rotate_rotors(r)
        return c

    def process(self, s):
        return ''.join(map(self._process, s))


machine = Enigma((Rotor('UKW-K', 1),
                  Rotor('II-K', 2),
                  Rotor('ETW-K', 3)),
                 Reflector('EJMZALYXVBWFCRQUONTSPIKHGD'))
print(machine.process('ATTACKATDAWN!'))
print(machine.reset().process('CAQHYL ED JXGL!'))
