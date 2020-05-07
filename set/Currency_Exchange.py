#定义转换变量
service_menu = {"1":"人民币转换美元","2":"美元转换人民币","3":"人民币转换欧元","0":"结束程序"}



#定义用户输入的转换金额
your_money = 0.0

#定义退出条件 flag
flag = True
while flag:
    # 打印输出第一行
    # 定义星号接收变量
    str1 = ''
    for i in range(0, 10):
        str1 += '*'
    print(str1 + "欢迎使用货币转换服务系统" + str1)

    # 循环字典
    for k, v in service_menu.items():
        print(k + '.' + v)

    # 定义输入变量
    Your_Choice = input("请您选择需要的服务：")
    # 换行
    print('')

    str2 = ''
    for i in range(0, 36):
        str2 += '~'
    print(str2)

    if Your_Choice == str(1):
        print("欢迎使用{}服务".format(service_menu["1"]))
        your_money = input("清输入您需要转换的人民币金额：")
        print("")
        print("您需要转换的人民币为：{}".format(your_money))
        #转换计算
        RMB_to_US = int(your_money) / 6.72
        print("兑换成美元为：{a:.2f}$".format(a=RMB_to_US))
    elif Your_Choice == str(2):
        print("欢迎使用{}服务".format(service_menu["2"]))
        your_money = input("清输入您需要转换的美元金额：")
        print("您需要转换的美元为：{}$".format(your_money))
        print("")
        # 转换计算
        US_to_RMB = int(your_money) * 6.72
        print("兑换成人民币为：{a:.2f}￥".format(a=US_to_RMB))
    elif Your_Choice == str(3):
        print("欢迎使用{}服务".format(service_menu["3"]))
        your_money = input("清输入您需要转换的人民币金额：")
        print("")
        print("您需要转换的人民币为：{}".format(your_money))
        #转换计算
        RMB_to_EUR = int(your_money) * 0.13
        print("兑换成欧元为：{a:.2f}欧元".format(a=RMB_to_EUR))
    elif Your_Choice == str(0):
        print("感谢您的使用，祝您生活愉快，再见！")
        flag = False
    else:
        print("输入有误，请重新选择！")

    print("========================================")