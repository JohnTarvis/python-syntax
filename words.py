words = ['salmon','ketchup','fence','badger', 'exciting']

def print_upper_words(words):
    '''prints words in uppercase'''
    for word in words:
        print(word.upper())

def print_upper_words_e(words):
    '''prints only words that start with 'e' in upper case'''
    for word in words:
        if word[0].upper() == 'E':
            print(word.upper())

def print_upper_words_any(words,letters):
    '''prints only words that start with specified letters'''
    for word in words:
        for letter in letters:
            if word[0] == letter:
                print(word.upper())

print_upper_words(words)

print_upper_words_e(words)

print_upper_words_any(words,'xyab')



