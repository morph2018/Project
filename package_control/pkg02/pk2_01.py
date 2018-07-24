class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi, 欢迎来到图灵学院！")


if __name__ == '__main__':

    print("我是模块pk01呀，你特么的叫我干毛")
