from stats import get_book_text
from stats import word_count
from stats import char_count

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = word_count(book_text)
    chars = char_count(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in chars:
        char = i["char"]
        count = i["num"]
        if char == "\n":
            char_display = "\\n"
        else:
            char_display = char
        print(f"{char_display}: {count}")
    print("============= END ===============")

main()