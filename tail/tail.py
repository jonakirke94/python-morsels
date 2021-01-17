import collections


def tail_base(iterable, n):
    if n <= 0:
        return []
    return [
        char
        for char in iterable
    ][-n:]


# testing a more performant solution with a constrained deqeu for bonus 2
def tail(iterable, n):
    if n <= 0:
        return []

    # we can create a constrained dequeue with a max-size of n
    deq = collections.deque(maxlen=n)

    # for this strategy the dequeue will discard elements when the max_length is exceeded
    for element in iterable:
        deq.append(element)

    return list(deq)