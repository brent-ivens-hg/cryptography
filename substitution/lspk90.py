from random import choice

CW_GLYPH = {'A': ('<C', '<(', '<[', '<{', '<|'),
            'B': ('-^', '/\\/\\', 'AA', '^^'),
            'C': ('L!', 'LJ', 'L|', 'U', '|_|'),
            'D': ('/\\', '¯¯U', '¯¯V'),
            'E': ('LL|', 'UU', 'VV', 'W', '\\|/'),
            'F': ('LL', 'L|_'),
            'G': ('L9', 'LD'),
            'H': (']=[', ']['),
            'I': ("'--", "'=="),
            'J': ("'¯7", '¯¯)', '¯¯7', '¯¯]'),
            'K': ('_V_',),
            'L': ('_]', '_|'),
            'M': ('E',),
            'N': ('Z',),
            'O': ('()', '[]'),
            'P': ('/\\_', 'A_', '^-'),
            'Q': ("O'", 'O+', 'v¯¯'),
            'R': ('A<', '^<'),
            'S': ('(/)', 'V\\', '[/]', 'v^'),
            'T': ('[--', '|--'),
            'U': (']',),
            'V': ('>',),
            'W': ('3',),
            'X': ('><', 'X'),
            'Y': (')--', '>-'),
            'Z': ('N', '|\\|')}

CW_DEGLYPH = {v: k for k, vs in CW_GLYPH.items() for v in vs}


class LSPK90CW:
    @staticmethod
    def encode(plaintext: str) -> str:
        return ' '.join(choice(CW_GLYPH[c]) for c in plaintext.upper() if c in CW_GLYPH)

    @staticmethod
    def decode(ciphertext: str) -> str:
        return ''.join(CW_DEGLYPH[c] for c in ciphertext.upper().split() if c in CW_DEGLYPH)


def test_lspk90cw():
    cipher = LSPK90CW()
    print(cipher.encode('attack at dawn'))
    print(cipher.decode('<C [-- [-- <C L! _V_ <C [-- /\\ <C 3 Z'))
