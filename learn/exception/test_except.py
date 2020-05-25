

def test_div(num1,num2):
   return num1/num2


if __name__ == '__main__':
    try:
        test_div(5,'s')
    except ZeroDivisionError:
        print('除数不能为零！')
    except TypeError:
        print('参数类型错误！')