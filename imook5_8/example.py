

class Student(object):
    """
    学生类
    """
    def __init__(self,sid,name,selected=[]):
        self.sid = sid
        self.name = name
        self.selected = []

    def course_detail(self):
        """ 返回学生的已选课程信息 """
        return self.selected

    def add_course(self,cour_info):
        """ 实现添加课程信息 """
        self.selected.append(cour_info)

    def __str__(self):
        """ 打印学生信息 """
        str = 'name:{0},s_number:{1}'.format(self.name,self.sid)
        return str


class Teacher(object):
    """ 教师信息类 """
    def __init__(self,tid,name,phone):
        self.tid = tid
        self.name = name
        self.phone = phone

    def __str__(self):
        str = "t_number:{0},name:{1}".format(self.tid,self.name)
        return str


class Course(object):
    """ 课程类 """
    def __init__(self,cid,name,teacher = None):
        self.cid = cid
        self.name = name
        self.teacher= teacher

    def binding(self,teacher):
        if not teacher == None:
            self.teacher = teacher
            dict = {'课程名称':self.name,'教师名称':teacher.name}
            return dict
        else:
            return {}