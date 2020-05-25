import sys
import random
from datetime import datetime


#自定义游戏进入提示函数
def guide_page(guide_word):
    """
    提示玩家进入游戏，并输出信息
    :param guide_word: 提示信息
    """
    print("**********{0}**********".format(guide_word))


#自定义数字类型判断函数
def all_num(n):
    """
    判断指定的值是否为数字
    :param n: 输入的值
    :return: 返回布尔值
    """
    return str(n).isdigit()


#自定义数值合法性判定函数
def num_legal(ls):
    """
    判定指定序列中的数值是否相等以及记录数字区间起始位置的值
    是否大于记录数字区间终止位置的值
    :param ls: 输入区间的数组
    :return: 返回为1则为正确区间
    """
    if ls[0] == ls[1]:
        print("您输入的区间数字相同！！请重新启动程序。")
        sys.exit()
    elif ls[0] > ls[1]:
        print("您输入的数字区间大小有误！！请重新启动程序。")
        sys.exit()
    else:
        return 1


#自定义产生指定区间随机数函数
def set_final_num(num1,num2):
    """
    根据参数值，产生一个位于参数值区间以内的随机数
    :param num1: 输入的第一个数
    :param num2: 输入的第二个数
    :return: 返回结果
    """
    l = [num1,num2]
    rest = list(filter(all_num,l))
    if 1 == num_legal(rest):
        print("所产生的随机数字区间为：{0}".format(rest))
        return random.randrange(int(rest[0]),int(rest[1]))
    else:
        print("您所输入的为非数字字符，请重新启动！")
        sys.exit()


#自定义核查数值是否属于指定区间函数
def check_num_legal(num):
    """
    判定所输入的数值是否在指定的区间
    :param num: 用户输入的数字
    :return: 返回结果
    """
    if num >= int(i) and num <= int(j):
        return True
    else:
        print("对不起您输入的数字未在指定区间！！！")
        return False


#自定义日志写入函数
def write_record(times,value):
    """
    将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件
    :param times: 玩家猜测的次数
    :param value: 本次猜测的具体数字
    :return:
    """
    with open("record.txt",'a+',encoding="utf-8") as file:
        date_time = datetime.now()
        file.write("{0}: 第{1}次您猜测的数字为:{2}".format(date_time,times,value))
        file.write('\n')


#自定义main(rand1)函数
def main(rand1):
    """
    依据所产生的随机数字(rand1)，提示玩家输入猜测数字并进行比对直到猜测到正确数字
    :param rand1: 产生的随机数
    :return:
    """
    temp = rand1
    times = 0
    while True :
        num1 = int(input("请继续输入您猜测的数字："))
        print("")
        print("******************")
        if not check_num_legal(num1):
            continue
        if num1 == temp:
            times += 1
            write_record(times,num1)
            print("恭喜您！只用了{}次就赢得了游戏".format(times))
            break
        elif num1 < temp:
            times += 1
            write_record(times,num1)
            print('Lower than the answer')
        else:
            times += 1
            write_record(times, num1)
            print('Higher than the answer')


if __name__ == '__main__':
    guide_page("欢迎进入数字猜猜猜小游戏")
    i = input("数字区间起始值：")
    j = input("数字区间终止值：")
    rand = set_final_num(i,j)
    main(rand)