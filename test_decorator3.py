

def eat(cls):
    """ 吃东西 """
    cls.eat = lambda self:print('{0}>我要吃东西'.format(self.name))
    return cls


@eat
class Cat(object):
    """ 猫类 """
    def __init__(self,name):
        self.name = name


if __name__ == '__main__':
    cat = Cat('小黑')
    cat.eat()