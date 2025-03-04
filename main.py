from stats import get_word_count
from stats import get_character_count
from stats import convert_dict_to_list
from stats import sort_list
from stats import filter_alpha_characters

import sys

def get_book_text(args):
    with open(args, encoding="utf-8") as f:
        return f.read()

def print_report(filtered_list):
    for char in filtered_list:
        print(f"{char['char']}: {char['count']}")


def main(sys_args):
    book_location = sys_args[1]
    text = get_book_text(book_location)
    word_count = get_word_count(text)
    chars_count = get_character_count(text)
    sorted_dict = convert_dict_to_list(chars_count)
    sorted_list = sort_list(sorted_dict)
    filtered_list = filter_alpha_characters(sorted_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_report(filtered_list)
    print("============= END ===============")
    # print(f"Characters in book: {len(chars_count)}")
    # for char in chars_count:
    #     print(f"'{char}': {chars_count[char]}")

if __name__ == "__main__":
    main(sys.argv)