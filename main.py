from sys import argv, exit
from stats import get_num_words, get_number_of_each_character
if len(argv) < 2: 
    print ("Usage: python3 main.py <path_to_book>")
    print(f"{argv} argument provided")
    exit(1)
print(f"{argv} argument provided")
def main():
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at " f"{argv[1]}...")# books/frankenstein.txt...")
    print ("----------- Word Count ----------")
#    get_num_words("./books/frankenstein.txt")
    get_num_words(argv[1])
    
    get_number_of_each_character(argv[1])

main()