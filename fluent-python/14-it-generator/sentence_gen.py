# -*- coding: utf-8 -*-

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


def test_iterable_obj(text):
    s = Sentence(text)
    print(s)
    for word in s:
        print(word)

    print(list(s))
    # print(s[0], s[5], s[-1])


if __name__ == '__main__':
    text = '"The time has come," the walrus said,'
    test_iterable_obj(text)
