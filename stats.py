def get_num_words(path_to_file):
    word_count = 0
    with open(path_to_file) as file:
        file_contents = file.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
    #print(words)
    print ("Found "f"{word_count}" " total words")
    print ("--------- Character Count -------")


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
    sort_by_count(character_counts)

def sort_on(items):
    return items["num"]

def sort_by_count(character_counts):
    char_stats = []
                #   "char":"",
                #   "num": 0
                #   }
    #print (f"{character_counts}" )
#    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]
#    char_list.sort(key=lambda x: x["num"], reverse=True)
    for character in character_counts:
        #print(character)
        char_stats.append({"char": character,"num": character_counts[character]})
        #            }
        # char_stats = [
        #              {"char": character,"num": character_counts[character]
        #               }
        #              ]
#        char_stats["num"] 
    char_stats.sort(reverse=True,key=sort_on)
    for result in char_stats:
        print (f"{result["char"]}: {result["num"]}" )

