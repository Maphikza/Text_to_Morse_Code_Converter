# bisect_left will search through the list and return its index. I will use the index to locate the code.
from bisect import bisect_left

# List of letters in Morse
morse = [('a', '*-'), ('b', '-***'), ('c', '-*-*'), ('d', '-**'), ('e', '*'), ('f', '**-*'), ('g', '--*'),
         ('h', '****'), ('i', '**'), ('j', '*---'), ('k', '-*-'), ('l', '*-**'), ('m', '--'), ('n', '-*'),
         ('o', '---'), ('p', '*--*'), ('q', '--*-'), ('r', '*-*'), ('s', '***'), ('t', '-'), ('u', '**-'),
         ('v', '***-'), ('w', '*--'), ('x', '-**-'), ('y', '-*--'), ('z', '--**')]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print("Welcome to the Text to Morse Code Converter!! \n")

text = input('please enter the text you would like to convert.\n').lower()
morse_translated = []
result = ' '
for letter in text:
    if letter == ' ':
        morse_translated.append('  ')
    elif letter not in alphabet:
        pass
    else:
        morse_translated.append(morse[bisect_left(alphabet, letter)][1])

print(result.join(morse_translated))
