from collections.abc import Iterable


def is_iterable(item):
    return isinstance(item, Iterable)


def deep_flatten(deep_list):
    for item in deep_list:
        if is_iterable(item) and not isinstance(item, str):
            yield from deep_flatten(item)
        else:
            yield item

