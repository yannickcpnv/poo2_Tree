from structure.WordSearchTree import WordSearchTree

tree = WordSearchTree()
with open('functions.txt', 'r') as f:
    for line in f:
        tree.add(line.strip())

# Ask user to search for a word
while True:
    word = input('Enter a word to search for: ')
    if word == 'tatsugeki':
        break
    print('Found!') if tree.search(word) else print('Not found!')
