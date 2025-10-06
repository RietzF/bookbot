import sys
from stats import get_word_count, get_char_count, print_report



def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print_report(sys.argv[1])
main()


		
