def get_num_words(path_to_file):
    word_count = 0
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
    #print(words)
    print(f"{word_count} words found in the document")