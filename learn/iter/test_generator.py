

def pow():
    yield 1
    yield 2
    yield 3
    yield 4


def pow_number():
    return (x * x for x in [1, 2, 3, 4, 5])


def pow_number2():
    for x in [1, 2, 3, 4, 5]:
        yield x * x


if __name__ == '__main__':
    rest = pow()
    print(next(rest))