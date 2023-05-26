with open('morse.txt', 'r', encoding='utf-8') as f:
    morse_dict = dict(map(str.split, f.read().splitlines()))
    '''
    to_bin = str.maketrans('.-', '01')
    print('char\tcode\tbin')
    for char, code in morse_dict.items(): print('\t'.join(s.ljust(4) for s in (char, code, code.translate(to_bin))))
    '''
    morse_dict.update({v: k for k, v in morse_dict.items()})


def to_morse(text: str) -> str:
    return ' '.join(' '.join(morse_dict.get(c, '') for c in w) for w in text.upper().split())


def from_morse(code: str) -> str:
    return ''.join(map(morse_dict.get, code.split()))


def morse_to_ternary(text: str, dot='0', dash='1', pause='2') -> str:
    return text.translate(str.maketrans('.- ', dot + dash + pause))


def ternary_to_morse(text: str, dot='0', dash='1', pause='2') -> str:
    return text.translate(str.maketrans(dot + dash + pause, '.- '))


print(text := 'this is a hidden message')
print(morse := to_morse(text))
print(tern := morse_to_ternary(morse))
print(morse := ternary_to_morse(tern))
print(from_morse(ternary_to_morse(tern)))
