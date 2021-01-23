from collections import deque
from itertools import zip_longest

'''
the asterix is a neat little trick to capture all positional arguments
so that the fillvalue must be passed as a keyword argument 
'''
def window(iterables, n, *, fillvalue=None):
    if n == 0:
        return []

    queue = deque(maxlen=n)

    for item, _ in zip_longest(iterables, range(n), fillvalue=fillvalue):
        queue.append(item)
        if len(queue) == n:
            yield tuple(queue)

