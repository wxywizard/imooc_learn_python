

class BaseCat(object):
    """
    猫科动物的基础类
    """
    tag = '猫科动物'
    def __init__(self,name):
        self.name = name

    def eat(self):
        """ 猫吃东西"""
        print("猫都要吃")

class Tiger(BaseCat):
    """
    老虎类 也是猫科动物
    """
    def eat(self):
        # 调用父类方法
        super(Tiger,self).eat()
        print('我还喜欢吃肉。大猪肉')


class Panda(BaseCat):
    """
    熊猫类 也是猫科动物
    """
    pass


class PetCat(BaseCat):
    """
    家猫类
    """
    def eat(self):
        # 调用父类方法
        super(PetCat, self).eat()
        print('我还喜欢猫粮')


class HuaCat(PetCat):
    """
    中华田园猫
    """

    def eat(self):
        # 调用父类方法
        super(HuaCat, self).eat()
        print('我还喜欢吃零食')


class DuanCat(PetCat):
    """
    英国短毛
    """
    pass


if __name__ == '__main__':

    cat = HuaCat('小黄')
    cat.eat()
    issubclass(HuaCat,PetCat)