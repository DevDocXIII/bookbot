from stats import get_num_words, get_number_of_each_character


def main():
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    get_num_words("./books/frankenstein.txt")
    
    get_number_of_each_character("./books/frankenstein.txt")

main()