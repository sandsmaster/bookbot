import re
def get_book_text (url):
    with open(url, "rt") as f:
        return f.read()

def wc(text):
    return len(text.split())

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = wc(book_content)
    print(f"{num_words} words found in the document")

main()