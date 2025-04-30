
def get_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words():
    content = get_content('books/frankenstein.txt')
    words = content.split()
    print(f"{len(words)} words found in the document")
