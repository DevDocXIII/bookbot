def get_num_words(path_to_file):
    word_count = 0
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
    #print(words)
    print(f"{word_count} words found in the document")


def get_number_of_each_character(path_to_file):
    character_counts = {}
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.split()
        for word in words:
            for char in word:
                char = char.lower()
                if char.isalpha():
                    if char in character_counts:
                        character_counts[char] += 1
                    else:
                        character_counts[char] = 1
        print(character_counts)