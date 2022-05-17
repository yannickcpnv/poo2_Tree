from structure.WordSearchTree import WordSearchTree

tree = WordSearchTree()
with open('functions.txt', 'r') as f:
    for line in f:
        tree.add(line.strip())

while True:
    word = input('Enter a word to search for: ')
    if word == 'tatsugeki':
        break
    print('Found!') if tree.exists(word) else print('Not found!')
