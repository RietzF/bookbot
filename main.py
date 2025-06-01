from stats import get_book_text, alphabet_num
import sys
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print(get_book_text(sys.argv[1]))
    print(alphabet_num(sys.argv[1]))
    





main()
