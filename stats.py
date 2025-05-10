def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_string):
    word_list = book_string.split()
    return len(word_list)


def sort_on(dict):
    return dict["num"]



def char_count(path):
    chars = get_book_text(path)
    char_count = {}
#   count chars

    for char in chars:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        elif char.lower() not in char_count:
            char_count[char.lower()] = 1
    char_count_pair = []

#   sort chars

    for char, count in char_count.items():
        char_count_pair.append({"char": char, "num": count})

    char_count_pair.sort(reverse=True, key=sort_on)

    return char_count_pair


    