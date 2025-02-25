from collections import defaultdict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_words(file_contents))
    char_data = count_characters(file_contents)
    character_report(char_data)


def count_words(input_text: str):
    return len(input_text.split())


def count_characters(input_text: str):
    char_count = defaultdict(int)
    for char in input_text.lower():
        char_count[char] += 1

    return char_count


def character_report(char_data: dict):
    print("--- Begin report of books/frankenstein.txt ---")
    for char, count in char_data.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")


if __name__ == "__main__":
    main()
