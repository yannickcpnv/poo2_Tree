from structure.WordSearchTree import WordSearchTree

tree = WordSearchTree()
with open('functions.txt', 'r') as f:
    for line in f:
        tree.add(line.strip())

print('\n')
