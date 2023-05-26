"""
analysis.py
"""
from collections import Counter, defaultdict
from csv import reader
from enum import Enum
from typing import Generator


class Freq(Enum):
    WORD = 0
    MONOGRAM = 1
    BIGRAM = 2
    TRIGRAM = 3
    QUADGRAM = 4
    QUINTGRAM = 5


bigram_alt_freq = (
    'TH', 'EN', 'NG', 'HE', 'ED', 'OF', 'IN', 'TO', 'AL', 'ER', 'IT', 'DE', 'AN', 'OU', 'SE', 'RE', 'EA', 'LE', 'ND',
    'HI',
    'SA', 'AT', 'IS', 'SI', 'ON', 'OR', 'AR', 'NT', 'TI', 'VE', 'HA', 'AS', 'RA', 'ES', 'TE', 'LD', 'ST', 'ET', 'UR')


def english(freq: Freq) -> dict:
    with open(f'english_{freq.name.lower()}s.txt', 'r', encoding='utf-8') as file:
        res = {k: int(v) for k, v in reader(file, delimiter=' ')}
        num = sum(res.values())
        return {k: round(v / num, 6) for k, v in res.items()}


def frequency_table(string: str) -> Counter:
    tbl = Counter(string)
    tot = sum(tbl.values())
    for k in tbl: tbl[k] /= tot
    return tbl


def letters_only(string: str) -> str:
    return ''.join(filter(str.isalpha, string))


def ngrams(string: str, n: int) -> Generator[str, None, None]:
    string = letters_only(string)
    for i in range(len(string) - n + 1):
        yield string[i:i + n]


def decode(text: str, freq: Freq) -> ...:
    text = text.upper()
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
