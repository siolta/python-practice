# from stats import
import sys
from collections import defaultdict


def main():
    with open(sys.argv[1]) as f:
        file_contents = f.read()

    print(f"Found {count_words(file_contents)} total words")
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
    print(f"--- Begin report of {sys.argv[1]} ---")
    for char, count in char_data.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
            print(f"{char}: {count}")
    print("--- End Report ---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main()
