from line_profiler_pycharm import profile

from structure.WordSearchTree import WordSearchTree


@profile
def benchmark():
    search_array()
    search_tree()


def search_tree():
    return tree.exists(word)


def search_array():
    return word in array


tree = WordSearchTree()
array = []

with open('functions.txt', 'r') as f:
    for line in f:
        line_strip = line.strip()
        tree.add(line_strip)
        array.append(line_strip)

word = input('Enter a word to search for: ')
benchmark()
