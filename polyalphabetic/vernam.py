class Vernam:
    def __init__(self, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> None:
        self.alpha = alphabet.upper()
        self.map = dict(enumerate(self.alpha))
        self.map.update({v: k for k, v in self.map.items()})

    def __repr__(self) -> str: return f'{self.__class__.__name__}()'

    def cipher(self, text: str, otp: str, mode: int) -> str:
        text, otp = (list(filter(str.isalpha, x.upper())) for x in (text, otp))
        if len(otp) < len(text): raise ValueError('One-time pad has to be at least as long as the text')
        return ''.join(self.map[(self.map[a] + mode * self.map[b]) % 26] for a, b in zip(text, otp))

    def encode(self, plaintext: str, otp: str) -> str: return self.cipher(plaintext, otp, 1)
    def decode(self, ciphertext: str, otp: str) -> str: return self.cipher(ciphertext, otp, -1)

def test_vernam():
    cipher = Vernam()
    print(cipher.encode('DCODE VERNAM', 'ENCRYPTIONS'))
    print(cipher.encode('ATTACK AT DAWN', 'QUEENLY MOVES'))
