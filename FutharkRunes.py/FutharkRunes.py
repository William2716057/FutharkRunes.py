
runes = {
 'ᚨ': 'a',
    'ᛒ': 'b',
    'ᚲ': 'c',
    'ᛞ': 'd',
    'ᛖ': 'e',
    'ᚠ': 'f',
    'ᚷ': 'g',
    'ᚺ': 'h',
    'ᛁ': 'i',
    'ᛃ': 'j',
    'ᚲ': 'k',
    'ᛚ': 'l',
    'ᛗ': 'm',
    'ᚾ': 'n',
    'ᛟ': 'o',
    'ᛈ': 'p',
    'ᚲ': 'q',
    'ᚱ': 'r',
    'ᛊ': 's',
    'ᛏ': 't',
    'ᚢ': 'u',
    'ᚹ': 'w',
    'ᛉ': 'z',
}

phrase = input("input text: ")

for rune in phrase:
    if rune in runes:
        print(runes[rune], end=' ')
    else:
        print(rune, end=' ')

print()
