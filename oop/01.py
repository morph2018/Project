#定义一个学生类
#定义一个空的类
class Student():
    #一个空的类，pass必须有
    pass
#定义一个对象
mingyue = Student()
#定义一个Python学生类
class PythonStudent():
    #用None给不确定值的变量赋值
    name = None
    age = 18
    course = 'Python'

    def doHomework(self):
        print('做作业')
        #推荐函数末尾使用return
        return None
#实例化一个具体的学生yueyue
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意函数的调用没有传入参数
yueyue.doHomework()


