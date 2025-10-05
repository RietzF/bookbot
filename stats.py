

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def get_word_count(filepath):
	return len(get_book_text(filepath).split())

def get_char_count(filepath):
	chars = {
		"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0,
		"m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0,
        "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0, " " : 0, "!" : 0, "?" : 0, "&" : 0,
		"," : 0, "." : 0, "@" : 0
		  }
	text = get_book_text(filepath).lower().split()
	for l in text:
		for c in l:
		    if c in chars:
			    chars[c] += 1
	return chars