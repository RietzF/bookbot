from pathlib import Path
from collections import Counter
from typing import Dict

def get_book_text(filepath: str) -> str:
	return Path(filepath).read_text(encoding="utf-8")


def get_word_count(filepath: str) -> int:
	return len(get_book_text(filepath).split())

def get_char_count(filepath: str) -> Dict[str, int]:
	return Counter(get_book_text(filepath).lower())

def sort_on(items):
	return items["num"]

def get_sorted_dict(filepath):
	new_dict = []
	old_dict = get_char_count(filepath)
	for k, v in old_dict.items():
		if k.isalpha():
			new_dict.append({"char" : k, "num" : v})
		else:
			continue
	new_dict.sort(reverse=True, key=sort_on)
	return new_dict
	
def print_report(filepath):
	list = get_sorted_dict(filepath)
	print(f'''============ BOOKBOT ============\nAnalyzing book found at {str(filepath)}...\n----------- Word Count ----------\nFound {get_word_count(filepath)} total words\n--------- Character Count -------''')
	for l in list:
		print(f"{l["char"]}: {l["num"]}")
	print("============= END ===============")