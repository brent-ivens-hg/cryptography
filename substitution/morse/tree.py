from collections.abc import Iterable
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.__class__.__name__}{self.data, self.left, self.right}'

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, iterable: Iterable):
        self.root = Node(None)
        cur = self.root
        stack = []
        for x in iterable:
            if x is not None:
                if cur.left is None:
                    cur.left = Node(x)
                elif cur.right is None:
                    cur.right = Node(x)
                else:
                    stack.extend([cur.left, cur.right])
                    cur = stack.pop(0)
                    cur.left = Node(x)

    def __str__(self):
        def stringify(node, level=0):
            if node is not None:
                yield from stringify(node.right, level + 1)
                yield ' ' * 4 * level + f'-> {node}'
                yield from stringify(node.left, level + 1)

        return '\n'.join(stringify(self.root))


def translate_morse(morse):
    morse_tree = Tree('ETIANMSURWDKGOHVF*L*PJBXCYZQ**')
    decoded = []
    for code in morse.split():
        try:
            cur = morse_tree.root
            for char in code:
                if char == '.':
                    cur = cur.left
                elif char == '-':
                    cur = cur.right
            decoded.append('None' if cur.data == '*' else str(cur.data))
        except AttributeError:
            decoded.append('None')
    return ''.join(decoded)


print(translate_morse('... --- ...'))
