def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")   
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

main()

