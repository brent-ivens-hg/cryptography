from itertools import cycle

class JeffersonWheel:
    def __init__(self, rank: int = 1) -> None:
        if not isinstance(rank, int): raise TypeError('rank must be an integer')
        self._rank = rank % 26
        self._wheels = (
            'ABCEIGDJFVUYMHTQKZOLRXSPWN', 'ACDEHFIJKTLMOUVYGZNPQXRWSB', 'ADKOMJUBGEPHSCZINXFYQRTVWL',
            'AEDCBIFGJHLKMRUOQVPTNWYXZS', 'AFNQUKDOPITJBRHCYSLWEMZVXG', 'AGPOCIXLURNDYZHWBJSQFKVMET',
            'AHXJEZBNIKPVROGSYDULCFMQTW', 'AIHPJOBWKCVFZLQERYNSUMGTDX', 'AJDSKQOIVTZEFHGYUNLPMBXWCR',
            'AKELBDFJGHONMTPRQSVZUXYWIC', 'ALTMSXVQPNOHUWDIZYCGKRFBEJ', 'AMNFLHQGCUJTBYPZKXISRDVEWO',
            'ANCJILDHBMKGXUZTSWQYVORPFE', 'AODWPKJVIUQHZCTXBLEGNYRSMF', 'APBVHIYKSGUENTCXOWFQDRLJZM',
            'AQJNUBTGIMWZRVLXCSHDEOKFPY', 'ARMYOFTHEUSZJXDPCWGQIBKLNV', 'ASDMCNEQBOZPLGVJRKYTFUIWXH',
            'ATOJYLFXNGWHVCMIRBSEKUPDZQ', 'AUTRZXQLYIOVBPESNHJWMDGFCK', 'AVNKHRGOXEYBFSJMUDQCLZWTIP',
            'AWVSFDLIEBHKNRJQZGMXPUCOTY', 'AXKWREVDTUFOYHMLSIQNJCPGBZ', 'AYJPXMVKBQWUGLOSTECHNZFRID',
            'AZDNBUHYFWJLVGRCQMPSOEXTKI'
        )
        self._maps = tuple(
            {**{c: i for i, c in enumerate(cyl)}, **{i: c for i, c in enumerate(cyl)}} for cyl in self._wheels
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._rank!r})'

    def __str__(self) -> str:
        return '\n'.join(map(' | '.join, zip(*self._wheels)))

    def cipher(self, text: str, mode: int) -> str:
        res, map = [], cycle(self._maps)
        for c in text.upper():
            if c.isalpha():
                m = next(map)
                c = m[(m[c] + mode * self._rank) % 26]
            res.append(c)
        return ''.join(res)

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, 1)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, -1)

def test_jefferson_wheel():
    cipher = JeffersonWheel()
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('BLVEYV HD SKDF'))
    cipher = JeffersonWheel(13)
    print(cipher.encode('ATTACK AT DAWN'))
    print(cipher.decode('HRERNU OV YTAZ'))
