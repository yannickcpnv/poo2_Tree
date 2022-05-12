from typing import Optional


class Node:
    children: list[Optional['Node']]
    is_word: bool

    def __init__(self):
        self.children = list(None for _ in range(26))
        self.is_word = False

    def add(self, word: str) -> None:
        if word == '':
            self.is_word = True
            return

        if self.children[ord(word[0]) - ord('a')] is None:
            self.children[ord(word[0]) - ord('a')] = Node()

        next_node = self.children[ord(word[0]) - ord('a')]
        cut_word = word[1:]
        next_node.add(cut_word)

    def search(self, word: str) -> bool:
        if word == '':
            return self.is_word

        if self.children[ord(word[0]) - ord('a')] is None:
            return False

        next_node = self.children[ord(word[0]) - ord('a')]
        cut_word = word[1:]

        return next_node.search(cut_word)
