class C():
    #__init__构造函数
    def __init__(gz):
        gz.name = 'aaaa'
        gz.age = 19
    def say(self):
        print(self.name)
        print(self.age)
    name = 'dana'
    age = 18
class B():
    name = 'bbbb'
    age = 100
c = C()
c.say()
#调用say函数时将C()代入函数时会先执行构造函数
C.say(c)
#调用say函数时将类名C代入函数时不会先执行构造函数
C.say(C)
C.say(B)
print(C.__dict__)