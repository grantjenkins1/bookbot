
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

def get_letters(str_content):
    letters = {}
    words = str_content.lower()
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def get_letters_list(content):
    letters_list = []
    letters = get_letters(content)
    for letter in letters:
        new_letter = {}
        new_letter['char'] = letter
        new_letter['num'] = letters[letter]
        letters_list.append(new_letter)
    return letters_list

def sort_on(dict):
    return dict['num']

def sort_dict(dict):
    return dict.sort(reverse=True, key=sort_on)
