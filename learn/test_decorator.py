
def log(name=None):


    def decorator(func):
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
    print('hello world')


@log('from add')
def add(a,b):
    return a + b

if __name__ == '__main__':
    #hello()
    print(add(5,6))