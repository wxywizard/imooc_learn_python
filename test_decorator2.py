from functools import wraps


def log(name=None):


    def decorator(func):
        #获取原始函数的名称的doc
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('{0}.start...'.format(name))
            print(args)
            print(kwargs)
            rest = func(*args,**kwargs)
            print('{0}.end...'.format(name))
            return rest
        return wrapper
    return decorator

#@log('you')
@log()
def hello():
    """ 简单功能模板 """
    print('hello world')



if __name__ == '__main__':
    print('doc:{0}'.format(hello.__doc__))
    print('name:{0}'.format(hello.__name__))
    hello()