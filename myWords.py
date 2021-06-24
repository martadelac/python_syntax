# capitalize(self, /)
#  |      Return a capitalized version of the string.
#  |      
#  |      More specifically, make the first character have upper case and the rest lower
#  |      case.

def print_upper_words(words):
    """For a list of words, print out each word on a separate line, 
    but in all uppercase."""
    for word in words:
        print(word.upper())

def print_upper_wordsE(words):
    """it only prints words that start with
    the letter ‘e’ (either upper or lowercase).""" 
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.uppre())

def print_upper_words3(words, start_with):
    """Print each word on sep line, uppercased, if starts with the one given"""
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
                
