def do_twice(func):

    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrap_func

def flip(func):

    def wrap_func(*args):
        reversed_args = args[::-1]
        return func(*reversed_args)
    return wrap_func

def negate(func):
    def wrap_func(*args, **kwargs):

        return not func(*args, **kwargs)
    return wrap_func

def once(func):
    has_run = False

    def wrap_func(*args, **kwargs):
        nonlocal has_run
        if not has_run:
            has_run = True
            return func(*args, **kwargs)
    has_run = False
    return wrap_func
