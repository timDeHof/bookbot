def get_word_count(args):
    num_words = len(args.split())
    return num_words

def get_character_count(args):
    new_string = args.lower()
    chars_list = list(new_string)
    chars = dict()
    for char in chars_list:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def convert_dict_to_list(dict):
    new_list = list()
    for key, value in dict.items():
        char_dict = {"char": key, "count": value}
        new_list.append(char_dict)
    return new_list

def sort_list(list):
    return sorted(list, key=sort_on, reverse=True)

def filter_alpha_characters(sorted_list):
    filtered_list = list()
    for char in sorted_list:
        if char["char"].isalpha():
            filtered_list.append(char)
    return filtered_list

def main():
    unsorted_list = [
    {"char": "a", "count": 15},
    {"char": "b", "count": 30},
    {"char": "c", "count": 10},
    {"char": "!", "count": 20},
]
    sorted_list = sort_list(unsorted_list)
    filtered_list = filter_alpha_characters(sorted_list)

    print(sorted_list)
    print(filtered_list)

if __name__ == "__main__":
    main()