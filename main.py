def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    print(f"""--- Begin report of {path} ---
{count_words(file_contents)} words found in the document
          """)
    
    chars = count_characters(file_contents)
    
    for char in sorted(chars.items(), key=lambda x: x[1], reverse=True):
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {chars[char[0]]} times")
    
    print("--- End report ---")


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