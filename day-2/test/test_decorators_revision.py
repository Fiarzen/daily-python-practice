from src.decorators_revision import do_twice, negate, flip, once

def test_do_twice_decorator_invokes_function_twice():
    count = 0

    @do_twice
    def add_number(num):
        nonlocal count
        count += num
    add_number(2)
    assert count == 4

def test_flip_reverses_arguments():
    @flip
    def concatenate(*args):
        return "".join(args)
    result = concatenate('h', 'e', 'l', 'l', 'o')
    assert result == "olleh"

def test_negate_returns_opposite_boolean():

    @negate
    def sameple_func():
        return False
    assert sameple_func() is True

def test_func_invoked_once():
    count = 0

    @once
    def sample_func():
        nonlocal count
        count += 1
        return "Would you look at that, I've been invoked!"

    sample_func()
    sample_func()
    sample_func()
    sample_func()
    assert count == 1
