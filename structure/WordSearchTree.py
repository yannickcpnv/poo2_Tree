from structure.Node import Node


class WordSearchTree:
    root: Node
    words: list[str]

    def __init__(self):
        self.root = Node('value')
        self.words = []

    def add(self, word):
        self.words.append(word)
