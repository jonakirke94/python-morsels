def compact_base(sequence):
    result = []
    for idx, num in enumerate(sequence):
        if idx == 0 or sequence[idx - 1] != num:
            result.append(num)

    return result


# we could simply convert the iterable to a sequence by doing list(iterable)
# but this defeats the purpose of the exercise AND it may not be performant
# on large or infinite iterables

# bonus 1 & 2

def compact(iterable):
    previous = object()  # sentinel
    for num in iterable:
        if num != previous:
            yield num
        previous = num

