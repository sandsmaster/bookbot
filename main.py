def get_book_text (url):
    with open(url, "rt") as f:
        return f.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

main()