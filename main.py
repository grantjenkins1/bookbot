from stats import get_num_words
from stats import get_letters
from stats import sort_dict
from stats import get_letters_list
import sys

args = sys.argv
if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = args[1]

def get_content(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    content = get_content(book_path)
    #number of words
    words = content.split()
    #dict of letters
    letters = get_letters_list(content)
    new_letters = sort_dict(letters)

    print(
       "============ BOOKBOT ============" + "\n" + 
       "Analyzing book found at " + book_path + "\n" + 
       "----------- Word Count ----------" + "\n" + 
       f"Found {len(words)} total words \n" +
       "--------- Character Count -------"
            )
    for letter in letters:
        if letter['char'].isalpha():
            print(letter['char'] + ': ' + str(letter['num']))
    print('============= END ===============')

main()
