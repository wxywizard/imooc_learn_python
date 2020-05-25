from imook5_8.example import Student,Teacher,Course

def introduction(str):
    print('********{}********'.format(str))

def prepare_course():
    dict = {"01": "网络爬虫", "02": "数据分析",\
            "03": "人工智能", "04": "机器学习",\
            "05": "云计算", "06": "大数据", \
            "07": "图像识别", "08": "Web开发"}
    list = []
    for x in dict.keys():
        course = Course(x,dict.get(x))
        list.append(course)
    return list

def create_teacher():
    tea_1 = Teacher("T1", "张亮", "13301122001")
    tea_2 = Teacher("T2", "王朋", "13301122002")
    tea_3 = Teacher("T3", "李旭", "13301122003")
    tea_4 = Teacher("T4", "黄国发", "13301122004")
    tea_5 = Teacher("T5", "周勤", "13301122005")
    tea_6 = Teacher("T6", "谢富顺", "13301122006")
    tea_7 = Teacher("T7", "贾老师", "13301122007")
    tea_8 = Teacher("T8", "杨老师", "13301122008")
    ls = [tea_1, tea_2, tea_3, tea_4, tea_5, tea_6, tea_7, tea_8]
    return ls

def course_to_teacher():
    list = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    i = 0
    for c in ls_course:
        list.append(c.binding(ls_teacher[len(ls_teacher)-(i+1)]))
        i += 1
    return list

def create_student():
    ls_student = [ "小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    ls_number = range(1000,1008)
    list = []
    i = 0
    for n in ls_number:
        stu = Student(n,ls_student[len(ls_student)-(i+1)])
        list.append(stu)
        i += 1
    return list

if __name__ == '__main__':
    tea = course_to_teacher()
    stu = create_student()
    introduction("慕课学院(1)班学生信息")
    for s in stu:
        print(s.__str__())
    introduction("慕课学院(1)班选课结果")
    i = 0
    for t in tea:
        stu[i].add_course(t)
        i += 1
    for s in stu:
        print('Name：{},Selected:{}'.format(s.name,s.selected))