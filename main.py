def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_words(file_contents))
    print(count_characters(file_contents))


def count_words(text):
    return len(text.split())

def count_characters(text):
    dictionary = {}
    for char in text:
        char = char.lower()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

main()