from itertools import zip_longest
import re
import unicodedata

#  an inefficient solution that compares each char after converting each word to a sorted list
def is_anagram_first(first, second):
    first_sorted = sorted(list(first.lower()))
    second_sorted = sorted(list(second.lower()))

    for x, y in zip_longest(first_sorted, second_sorted, fillvalue=None):
        if x != y:
            return False

    return True



SENTINEL = None


#  we can make two dictionaries and add the count for each word and them compare them
def is_anagram(first, second):
    first_dict = {}
    second_dict = {}

    regex = r"[^A-Za-z0-9]+"
    first_cleansed = re.sub(regex, "", remove_accents(first.lower()))
    second_cleansed = re.sub(regex, "", remove_accents(second.lower()))

    for x, y in zip_longest(first_cleansed, second_cleansed, fillvalue=SENTINEL):
        #  handle different word lengths
        if x == SENTINEL or y == SENTINEL:
            return False

        first_dict[x] = first_dict.get(x, 0) + 1
        second_dict[y] = second_dict.get(y, 0) + 1

    return first_dict == second_dict


#  https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode('utf-8')

