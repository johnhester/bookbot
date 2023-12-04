path = "books/frankenstein.txt"

def get_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents    

def get_words(str):
    return len(str.split())

def get_letter_counts(str):
    str = str.lower()
    char_count = {}
    for letter in str:
        if letter.isalpha():
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    return char_count

text = get_text(path)

words = get_words(text)
letter_count = get_letter_counts(text)

print(f"--- Begin report of {path} ---")
print(f"{words} are found in this document.")

for letter, count in sorted(letter_count.items()):
    print(f"The {letter} character was found {count} times.")

print(f"--- End report of {path} ---")
