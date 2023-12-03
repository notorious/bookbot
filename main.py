def main():
    # Replace file_name with any txt file name
    file_name = "frankenstein.txt"
    file_content = get_book_text(file_name)
    num_words = get_num_words(file_content)
    letters_dict = get_num_letters(file_content)
    print_report(num_words, letters_dict, file_name)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    letters_dict = {}
    # Splitting text into lowercased letters
    for word in text.lower().split():
        for letter in word:
            # If count for letter is not in letters_dict, initialize it to 0
            if letter not in letters_dict:
                letters_dict[letter] = 0
            # Increment the letter count
            letters_dict[letter] += 1
    return letters_dict


def get_book_text(file_name):
    with open(f"books/{file_name}") as f:
        return f.read()


def print_report(num_words, letters_dict, file_name):
    print(f"--- Begin report of books/{file_name} ---")
    print(f"{num_words} words found in the document\n")
    for letter in sorted(letters_dict.items(), key=lambda x: x[1], reverse=True):
        if letter[0].isalpha():
            print(
                f"The '{letter[0]}' character was found {letter[1]} times")
    print(f"--- End report ---")


main()
