def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = {}
    ltext = text.lower()
    for char in ltext:
        count = 0
        if char in characters:
            count = characters[char]
        characters[char] = count + 1
    for w in sorted(characters, key=characters.get, reverse=True):
        if w.isalpha():
            print (f"The '{w}' character was found {characters[w]} times")
    



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()