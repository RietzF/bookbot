def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return f"{len(file_contents.split())}"
def alphabet_num(filepath):
    letters_file = []
    report = ""
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
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
        if l in letter_dict and l.isalpha():
            letter_dict[l] += 1
    

    sorted_items = sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    for key, value in sorted_dict.items():
        report += f'''{key}: {value}\n'''
    full_report = f'''
Analyzing book found at {filepath}...\n
Found {get_book_text(filepath)} total words\n
___
Character Count\n
{report}\n
END'''
    return full_report




    





        
    