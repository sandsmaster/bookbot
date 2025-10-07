import re
from stats import wc, char_stats, sort_char, report_stats

def get_book_text (url):
    with open(url, "rt") as f:
        return f.read()

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = wc(book_content)
    # print(f"{num_words} words found in the document")
    stats = sort_char(char_stats(book_content))
    report_stats(num_words, stats)

main()