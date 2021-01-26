import re


def normalize_sentences(sentences):
    # if we use () regex group capture it will also include the delimiter
    # the + means we match one or more
    # the \1 is a backreference to the first match group
    return re.sub(r'([.?!]) +', r'\1  ', sentences)
