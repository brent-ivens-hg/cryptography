from warnings import warn
from vigenere import Vigenere


class AutoclaveWarning(UserWarning): pass


# noinspection SpellCheckingInspection
class Autoclave:
    """
    >>> cipher1 = Vigenere('queenly')
    >>> cipher1.encode('attack at dawn')
    'QNXEPV YJ XEAA'
    >>> cipher1.decode('QNXEPV YJ XEAA')
    'ATTACK AT DAWN'

    >>> cipher2 = Autoclave(Vigenere, 'queenly')
    >>> cipher2.encode('attack at dawn')
    'QNXEPV YT WTWP'
    >>> cipher2.decode('QNXEPV YT WTWP')
    'ATTACK AT DAWN'
    >>> cipher2.encode('attack')  # warns
    'QNXEPV'
    >>> cipher2.decode('QNXEPV')  # warns
    'ATTACK'
    """

    def __init__(self, cipher: type, key: str = '', alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        if not isinstance(key, str): raise ValueError('invalid key')
        if not isinstance(alphabet, str) or set(alphabet.upper()) != set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            raise ValueError('invalid alphabet')
        self._cipher = cipher
        self._alpha = alphabet.upper()
        self._key = self.filter(key.upper())

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._cipher.__name__}, {self._key!r}, {self._alpha!r})'

    def filter(self, text: str) -> str:
        return ''.join(filter(self._alpha.__contains__, text))

    def encode(self, plaintext: str) -> str:
        plaintext = plaintext.upper()
        decoded = self.filter(plaintext)
        if len(self._key) >= len(decoded):
            warn('text size should be smaller than key size for the autoclave encryption to work properly',
                 category=AutoclaveWarning)
        return self._cipher(self._key + decoded, self._alpha).encode(plaintext)

    def decode(self, ciphertext: str) -> str:
        ciphertext = ciphertext.upper()
        encoded = self.filter(ciphertext)
        k, c = len(self._key), len(encoded)
        if k >= c: warn('text size should be smaller than key size for the autoclave decryption to work properly',
                        category=AutoclaveWarning)
        decoded = [self._key]
        for i in range(0, c, k):  # decodes using previous decoded chunk as key
            decoded.append(self._cipher(decoded[-1], self._alpha).decode(encoded[i:i + k]))
        decoded = iter(''.join(decoded[1:]))  # skip key and join chunks
        return ''.join(next(decoded) if c in self._alpha else c for c in ciphertext)
