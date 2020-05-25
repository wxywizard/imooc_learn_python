

def write_file():
    """ 写入文件 """
    file_name = "write_test.txt"
    f = open(file_name,'w')
    f.write("hello")
    f.write('\n')
    f.write("world")

    f.close()


def write_mult_line():
    file_name = "write_mult_line.txt"
    with open(file_name,'w',encoding="utf-8") as f:
        l = ['第一行','\n','第二行','\r\n','3']
        f.writelines(l)


if __name__ == '__main__':
    write_mult_line()