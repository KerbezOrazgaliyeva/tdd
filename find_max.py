def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    raise TypeError('no arg')


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    inf = -100000
    for a in args:
        if a > inf:
            inf = a
    return inf


def get_max_with_one_or_more_arguments(first, *args):
    for a in args:
        if first < a:
            first = a
    return first


def get_max_bounded(*args, low, high):
    inf = -100000000
    for a in args:
        if a > inf and low<a<high:
            inf = a
    return inf


def make_max(*, low, high):
    def inner(first, *args):
        r = -100000
        if low<first<high:
            r = first
        for a in args:
            if r < a and low<a<high:
                r = a
        return r

    return inner
