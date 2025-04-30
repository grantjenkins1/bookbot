
def get_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_words():
    content = get_content('books/frankenstein.txt')
    words = content.split()
    return words

def get_num_words():
    words = get_words() 
    print(f"{len(words)} words found in the document")

def get_letters():
    letters = {}
    words = get_words()
    for word in words:
        for letter in word:
            if letters[letter]:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

