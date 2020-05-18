

class ApiException(Exception):
    err_code = ''
    err_msg = ''
    """
    当参数不合法时触发
    """
    def __init__(self,err_code = None,err_msg = None):
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return 'Error: {0} - {1}'.format(self.err_code, self.err_msg)

class InvalidCtrlExec(ApiException):
    err_code = '40001'
    err_msg = '不合法的调用凭证'




def divide(num1,num2):
    """
    除法的实现
    :param num1:
    :param num2:
    :return:
    """
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise ApiException('40001','参数不合法')
    if num2 == 0:
        raise ApiException('0','除数不能为零')
    return num1 / num2

if __name__ == '__main__':
    try:
        divide(5,'s')
    except ApiException as err:
        print('出错了')
        print(err)