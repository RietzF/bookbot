def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents
def get_word_count(filepath):
	return len(get_book_text(filepath).split())
def main():
	print(f"Found {get_word_count('''./books/frankenstein.txt''')} total words")

main()


		
