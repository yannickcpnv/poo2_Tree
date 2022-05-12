from structure.WordSearchTree import WordSearchTree
from line_profiler_pycharm import profile


def search_tree():
    return tree.exists(word)


def search_array():
    return word in array


@profile
def benchmark():
    search_array()
    search_tree()


tree = WordSearchTree()
array = []

with open('functions.txt', 'r') as f:
    for line in f:
        line_strip = line.strip()
        tree.add(line_strip)
        array.append(line_strip)

word = input('Enter a word to search for: ')
benchmark()
