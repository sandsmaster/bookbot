import re
import sys
from stats import wc, char_stats, sort_char, report_stats

def get_book_text (url):
    with open(url, "rt") as f:
        return f.read()

def main():
    main_args = sys.argv
    if len(main_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = main_args[1]
    book_content = get_book_text(book_path)
    num_words = wc(book_content)
    # print(f"{num_words} words found in the document")
    stats = sort_char(char_stats(book_content))
    report_stats(book_path, num_words, stats)

main()