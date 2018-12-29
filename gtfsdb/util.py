import sys


def get_all_subclasses(cls):
    """
    :See:
    https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name
    """
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in get_all_subclasses(c)])


class UTF8Recoder(object):
    """Iterator that reads an encoded stream and encodes the input to UTF-8"""
    def __init__(self, f, encoding):
        import codecs
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        if sys.version_info >= (3, 0):
            return next(self.reader)
        else:
            return self.reader.next().encode('utf-8')

    def __next__(self):
        return self.next()
