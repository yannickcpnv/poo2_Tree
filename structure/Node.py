from typing import Optional


class Node:
    children: list[Optional['Node']]
    is_word: bool

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    def add(self, word: str) -> None:
        if word == '':
            self.is_word = True
            return

        char_index = ord(word[0]) - ord('a')
        if self.children[self.__alpha_pos(word[0])] is None:
            self.children[char_index] = Node()

        next_node = self.children[char_index]
        cut_word = word[1:]
        next_node.add(cut_word)

    def search(self, word: str) -> bool:
        if word == '':
            return self.is_word

        if self.children[self.__alpha_pos(word[0])] is None:
            return False

        next_node = self.children[self.__alpha_pos(word[0])]
        cut_word = word[1:]

        return next_node.search(cut_word)

    @staticmethod
    def __alpha_pos(char: str) -> int:
        return ord(char) - ord('a')
