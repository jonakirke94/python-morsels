import re


#  not too satisfied to control flow with exceptions but it works
def count_words_old(words):
    my_dict = {}
    cleansed = re.findall(r'\b\S+\b', words)
    for word in cleansed:
        lowered_word = word.lower()
        try:
            count = my_dict[lowered_word]
            my_dict[lowered_word] = count + 1
        except KeyError:
            my_dict[lowered_word] = 1

    return my_dict


def count_words(words):
    my_dict = {}
    cleansed = re.findall(r'\b\S+\b', words.lower())
    for word in cleansed:
        my_dict[word] = my_dict.get(word, 0) + 1
    return my_dict
