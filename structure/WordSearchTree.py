from structure.Node import Node


class WordSearchTree:
    root: Node

    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        self.root.add(word)

    def exists(self, word: str) -> bool:
        return self.root.search(word)
