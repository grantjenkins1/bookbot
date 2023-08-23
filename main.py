def main(book):
    frankenstein_book=get_book(book)
    num_words = count_words(frankenstein_book)
    letters=count_letters(frankenstein_book)

    print(f"---Begin report of {book}---")
    print( f"There are {num_words} words in {book}" )
    print()
    for letter in letters:
        print(f"Letter {letter} was found {letters[letter]} times")
    print("---End Report---")

def get_book(book):
    with open(book) as f:
        return f.read()

def count_words(book):
    return len( book.split() )

def count_letters(book):
    letters={}
    book=book.lower()
    for letter in book:
        if letter.isalpha():
            if letter in letters:
                letters[letter]+=1
            else:
                letters[letter]=1
    return letters


main("books/frankenstein.txt")