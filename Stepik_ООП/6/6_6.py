from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    original_print = sys.stdout.write

    def reversed_write(text):
        original_print(text[::-1])

    sys.stdout.write = reversed_write
    yield
    sys.stdout.write = original_print




# from contextlib import contextmanager
#
#
# @contextmanager
# def make_tag(tag):
#     print(tag)
#     yield
#     print(tag)
