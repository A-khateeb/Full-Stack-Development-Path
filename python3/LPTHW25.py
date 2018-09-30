def break_words(stuff):
    words = stuff.split()
    return words


def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    return word

def print_last_word(words):
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_last_sentence(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_last_sorted(words):
    word = sort_sentence(words)
    print_first_word(word)
    print_last_word(word)
