from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *exception_tuple):
        self.exception_tuple = exception_tuple

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if not type:
            return None

        self.exception = value
        self.traceback = traceback

        if isinstance(type, self.exception_tuple) or issubclass(type, self.exception_tuple):
            return True