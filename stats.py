def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_string):
    word_list = book_string.split()
    return len(word_list)