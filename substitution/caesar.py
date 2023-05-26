class Caesar:
    def __init__(self, shift: int, alpha: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self._enc = str.maketrans(alpha, alpha[shift:] + alpha[:shift])
        self._dec = str.maketrans(alpha[shift:] + alpha[:shift], alpha)

    def encode(self, plaintext: str) -> str:
        return plaintext.upper().translate(self._enc)

    def decode(self, ciphertext: str) -> str:
        return ciphertext.upper().translate(self._dec)


cipher = Caesar(3)
print(cipher.encode('I am a golden God!'))
print(cipher.decode('L DP D JROGHQ JRG!'))
