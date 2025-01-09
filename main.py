def word_count(book):
    words = len(book.split())
               
    return words


def character_count(book):
    book = book.lower()
    characters = {}
    
    for i in range(97, 123):
        characters[chr(i)] = book.count(chr(i))
    
    return characters    


def main():
    file_location = None
    file_content = None
    
    # Take user input for text (book) to be examined
    valid = False
    while valid == False:
        file_location = input("Input File Location (.txt):")
        if file_location.endswith('.txt'):
            valid = True
        else:
            print("File is not a text file (.txt)")
    
    # Store file content and location
    with open(file_location) as f:
        file_content = f.read()
    
      
    # Print results  
    print(f"--- Begin report of {file_location} ---")
    print(f"{word_count(file_content)} words were found in the document!\n")
    characters = character_count(file_content)
    for i in range(97, 123):
        letter = chr(i)
        count = characters[chr(i)]
        print(f"The letter '{chr(i)}' was found {count} times!")
    print("--- End report ---")




main()