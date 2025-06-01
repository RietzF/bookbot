def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return f"{len(file_contents.split())} words found in the document"
def alphabet_num(filepath):
    letters_file = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "!", "?", "#", ".", ",", ":", ";"]
    file_contents = ""
    letter_dict = {}
    with open(filepath) as f:
        file_contents = f.read()

    letter_list = file_contents.lower().split()
    for word in letter_list:
        for letter in word:
            letters_file.append(letter)

    for letter in letters:
        letter_dict[letter] = 0
    for l in letters_file:
        if l in letter_dict:
            letter_dict[l] += 1
    return letter_dict 


    





        
       
    #populates list with alphabet using ASCII
    