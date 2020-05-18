import os


class FileBackup(object):
    """
    文本文件备份
    """
    def __init__(self,src,dist):
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取src目录下的所有文件
        :return:
        """
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self,file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        :return:
        """
        pass
        # 1.判断dist是否存在，如果不存在，要创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定目录不存在，创建完成')

        # 2.判断文件是否为我们要备份的文件

        # 拼接文件的完整路径
        full_src_path = os.path.join(self.src,file_name)
        full_dist_path = os.path.join(self.dist,file_name)
        # 首先要判断是否为文件夹，然后借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            with open(full_dist_path,'w',encoding='UTF-8') as f_dist:
                print('>> 开始备份【{0}】'.format(file_name))
                # 3.读取文件内容
                with open(full_src_path,'r',encoding='UTF-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break

                        # 4.把读取到的内容写入到新的文件中
                        f_dist.write(rest)
                    f_dist.flush()
                print('>>> 【{0}】备份完成'.format(file_name))
        else:
            print('文件类型不符合备份要求，跳过》》')

    def backup_file2(self,file_name):
        """
        处理备份-优化
        :param file_name: 文件/文件夹的名称
        :return:
        """
        pass
        # 1.判断dist是否存在，如果不存在，要创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定目录不存在，创建完成')

        # 2.判断文件是否为我们要备份的文件

        # 拼接文件的完整路径
        full_src_path = os.path.join(self.src,file_name)
        full_dist_path = os.path.join(self.dist,file_name)
        # 首先要判断是否为文件夹，然后借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            with open(full_dist_path,'w',encoding='UTF-8') as f_dist,\
                    open(full_src_path,'r',encoding='UTF-8') as f_src:
                print('>> 开始备份【{0}】'.format(file_name))
                # 3.读取文件内容
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break

                    # 4.把读取到的内容写入到新的文件中
                    f_dist.write(rest)
                f_dist.flush()
                print('>>> 【{0}】备份完成'.format(file_name))
        else:
            print('文件类型不符合备份要求，跳过》》')

if __name__ == '__main__':
    # src_path = 'D:\\python_workspaceAll\\imooc_learn\\backup\\src'
    # dist_path = 'D:\\python_workspaceAll\\imooc_learn\\backup\\dist'
    # 通过os.path生成
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path,'src')
    dist_path = os.path.join(base_path,'dist')
    bak = FileBackup(src_path,dist_path)
    bak.read_files()