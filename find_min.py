

def get_min(a, b):
    """
        return min number among a and b
    """
    return a if a < b else b

def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('no arguments')


def get_min_with_one_argument(x):
    """
        return that value
    """
    return x


def get_min_with_many_arguments(*args):
    """
	    return smallest number among args
    """
    r = 100000000
    for ar in args:
        if ar < r:
            r = ar
    return r


def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    for ar in args:
        if ar < first:
            first = ar
    return first


def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    r = 100000000
    for ar in args:
        if ar < r and low<ar<high:
            r = ar
    return r

def make_min(*, low, high):
    """
        return inner function object which takes at last one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):
        r = 100000000
        if low<first<high:
            r = first
        for a in args:
            if r > a and low<a<high:
                r = a
        return r

    return inner
