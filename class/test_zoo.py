

class Cat(object):
    """
    猫科动物
    """

    tag = '我是家猫'

    def __init__(self,name,age,sex=None):
        self.name = name
        #双下划綫开头的表示私有的属性，实例化不能访问或设置其值
        self.__age = age
        self.sex = sex

    def set_age(self,age):
        """
        改变猫的年龄
        :param age:
        :return:
        """
        self.__age = age
        return self.__age

    def show__info(self):
        """
        显示猫的信息
        :return:
        """
        rest = "我叫：{0}，今年{1}岁。".format(self.name,self.__age)
        print("我的性别：{0}".format(self.sex))
        print(rest)
        return rest

    def eat(self):
        """ 吃 """
        print('猫喜欢吃鱼')

    def catch(self):
        """ 猫捉老鼠 """
        print('我能捉')


class Car(object):
    pass


if __name__ == '__main__':
    # 实例化
    cat_black = Cat('小黑','3')
    cat_black.show__info()

    # 类的实例判断
    print(isinstance(cat_black,Cat))