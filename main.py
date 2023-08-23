def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    print('--- Begin report of books/frankenstein.txt ---')
    print(num_words(file_contents),'words found in the document')
    char_dict = num_letters(file_contents)
    print()
    end_list = list(char_dict.items())
    end_list.sort(key = lambda x: x[1], reverse=True)
    for item in end_list:
        if item[0].isalpha():
            print("The '"+item[0]+"' character was found "+
                  str(item[1])+" times")
    print('--- End report ---')
    

def num_words(nejaky_string):
    num = nejaky_string.split()
    return len(num)

def num_letters(nejaky_string):
    dictionary = {}
    for letter in nejaky_string.lower():
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

main()