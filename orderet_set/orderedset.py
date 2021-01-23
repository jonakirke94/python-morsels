from collections import Set
from itertools import zip_longest
from collections.abc import Sequence

SENTINEL = 1
ZIP_SENTINEL = None


class OrderedSet(Sequence):
    def __init__(self, values):
        self.ordered_dict = {}

        for val in values:
            self.add(val)

    def __len__(self):
        return len(self.ordered_dict)

    def __iter__(self):
        return iter(self.ordered_dict.keys())

    def __contains__(self, item):
        return self.ordered_dict.get(item)

    def __getitem__(self, i):
        # this could probably be done more time effeciently
        return list(self.ordered_dict)[i]

    def add(self, item):
        if not self.ordered_dict.get(item):
            self.ordered_dict[item] = SENTINEL

    def discard(self, item):
        if self.ordered_dict.get(item):
            self.ordered_dict.pop(item)

    def __eq__(self, other):
        if isinstance(other, Set):
            return all(x in other for x in self.ordered_dict)
        elif isinstance(other, OrderedSet):
            return all(x == y for x, y in zip_longest(self.ordered_dict.keys(),
                                                      other.ordered_dict.keys(), fillvalue=ZIP_SENTINEL))

        # should have called super().__eq__(other) here
        return self.ordered_dict == other
