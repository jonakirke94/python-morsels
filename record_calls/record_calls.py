from functools import wraps
from collections import namedtuple

# in python the bracket notation calls __get_item__
# and dot notation calls __get_attr__

# we can achieve dot notation by either using a class or a namedtuple but not a regular Dict
#@dataclass
#class Call:
    #args: Dict
    #kwargs: Dict

Call = namedtuple("Call", ["args", "kwargs", 'exception', 'return_value'])

NO_RETURN = 'very_special_value'


def record_calls(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        wrapped.call_count += 1
        try:
            return_value = func(*args, **kwargs)
            wrapped.calls.append(Call(args=args, kwargs=kwargs, return_value=return_value, exception=None))
        except Exception as e:
            wrapped.calls.append(Call(args=args, kwargs=kwargs, return_value=NO_RETURN, exception=e))
            raise e

        return return_value

    wrapped.call_count = 0
    wrapped.calls = []
    return wrapped
