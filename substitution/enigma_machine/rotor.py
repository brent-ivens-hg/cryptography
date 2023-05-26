from csv import reader
from string import ascii_uppercase as alpha

with open('tables.csv', 'r', encoding='utf-8') as f:
    data = reader(f)
    next(data)  # skip header
    TABLES = {row[0]: row[1] for row in data}


class Rotor:
    def __init__(self, setting=alpha, offset=0):
        setting = TABLES.get(setting, setting)
        assert len(setting) == 26 and set(setting) == set(alpha), 'invalid rotor'
        self.alpha = alpha[offset:] + alpha[:offset]
        self.init_offset = self.rotations = offset
        self.setting = setting

    def __repr__(self):
        return f'{self.__class__.__name__}{self.mapping, self.rotations}'

    def __str__(self):
        return self.alpha

    def process(self, c, reverse=False):
        args = (self.setting, self.alpha) if reverse else (self.alpha, self.setting)
        return c.translate(str.maketrans(*args))

    def reset(self):
        self.alpha = alpha[self.init_offset:] + alpha[:self.init_offset]
        self.rotations = self.init_offset
        return self

    def rotate(self, r=1):
        self.alpha = self.alpha[r:] + self.alpha[:r]
        self.rotations += r
        return self
