from functools import total_ordering
import unicodedata

@total_ordering
class FuzzyString:
    def __init__(self, word):
        self.word =  word
        self.normalized = FuzzyString.normalize(word)

    def __eq__(self, other):
        return self.normalized == FuzzyString.normalize(other)

    def __str__(self):
        return self.word

    def __repr__(self):
        return f'\'{self.word}\''

    def __lt__(self, other):
        return self.word > other

    #  string concatenation
    def __add__(self, other):
        str3 = [self.word, FuzzyString.normalize(other)]
        return FuzzyString(''.join(str3))

    @staticmethod
    def normalize(string):
        return unicodedata.normalize("NFKD", string.casefold())

    def __contains__(self, string):
        return self.normalize(string) in self.normalized
