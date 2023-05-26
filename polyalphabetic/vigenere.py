from itertools import cycle


# noinspection PyUnresolvedReferences,SpellCheckingInspection
class Vigenere:
    """
    >>> cipher = Vigenere('QUEENLY')
    >>> cipher.encode('ATTACK AT DAWN')
    'QNXEPV YJ XEAA'
    >>> cipher.decode('QNXEPV YJ XEAA')
    'ATTACK AT DAWN'
    """

    def __init__(self, key: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(key, str): raise ValueError('invalid key')
        if not isinstance(alphabet, str) or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')
        self._alpha = alphabet.upper()
        self._key = ''.join(c for c in key.upper() if c in self._alpha)
        self._map = dict(enumerate(self._alpha))
        self._map.update({v: k for k, v in self._map.items()})

    def encode(self, plaintext: str) -> str:
        return self.cipher(plaintext, 1)

    def decode(self, ciphertext: str) -> str:
        return self.cipher(ciphertext, -1)

    def cipher(self, text: str, mode: int) -> str:
        key = cycle(self._key)
        return ''.join(self._map[(self._map[c] + mode * self._map[next(key)]) % 26]
                       if c in self._map else c for c in text.upper())
