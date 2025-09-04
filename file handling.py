with open('example.txt', 'w') as file:
    file.write('Line 1: Hello, world!\n')
    file.write('Line 2: Python file handling is fun.\n')

with open('example.txt', 'a') as file:
    file.write('Line 3: Appending new text.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print("Reading full content:")
    print(content)

print("Reading line by line:")
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

import os
if os.path.exists('example.txt'):
    print("File exists! You can safely read it.")
else:
    print("File does not exist.")
