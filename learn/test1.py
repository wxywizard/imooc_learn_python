from functools import reduce

def fn(x,y):
    return x*10+y

def charToNum(s):
    dict = {'0':0,'1':1,'2':2,'3':3,'4':4}
    return dict[s]

if __name__ == '__main__':
    r1 = reduce(fn,map(charToNum,"23443"))
    print(r1)
    print(type(r1))