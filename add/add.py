import itertools


def add(*args):
    outer = []
    for x, y, *remaining_outer in itertools.zip_longest(*args, fillvalue=None):
        if not all((x, y, *remaining_outer)):
            raise ValueError("Given matrices are not the same size.")
        inner = []
        for i, j, *remaining_inner in itertools.zip_longest(x, y, *remaining_outer, fillvalue=None):
            if not all((i, j, *remaining_inner)):
                raise ValueError("Given matrices are not the same size.")
            as_tuple = (i, j, *remaining_inner)
            inner.append(sum(as_tuple))
        outer.append(inner)
    return outer
