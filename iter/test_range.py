

def use_range():
    """ python内置的range"""
    for i in range(5, 10):
        print(i)


class IterRange(object):
    """ 使用迭代器来抹蜜range函数 """
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    """ 使用生成器来模拟range函数"""
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            self.start += 1
            if self.start >= self.end:
                break
            yield self.start


def get_num(start, end):
    start -= 1
    while True:
        start += 1
        if start >= end:
            break
        yield start


if __name__ == '__main__':
    # use_range()
    iter = IterRange(5, 10)
   # print(next(iter))
    l = list(iter)
    print(l)

    gen = GenRange(5, 10).get_num()
    print(list(gen))

    print(list(get_num(5, 10)))
