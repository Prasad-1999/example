# Process
'''
1.The process means simply excution of program.
2.The process won't share the meomory.
3.hierarchical Inheritance  is example of process
'''

# program:(process)


class arithmetic:
    def display1(self):
        print("The first step of process")


class sum(arithmetic):
    def display2(self):
        a = int(input("Enter the a sum value:"))
        b = int(input("Enter the b sum value:"))
        print(a+b)


class sub(arithmetic):
    def display3(self):
        a = int(input("Enter the a sub value:"))
        b = int(input("Enter the b sub value:"))
        print(a-b)


c1 = sum()
c2 = sub()

c1.display1()
c1.display2()

# Threading
'''
1.Threading is a light-weight process
2.It is the connect of programs runs at background but it won't interrupt 
main program.
3.Threading will share the meomory.
'''
# Program:(threading)


# import threading
# from threading import *
# from time import sleep
# class Thread1(Thread):
#     def run(self):
#         for i in range(5):
#             print("This is 1st thread 1", i)
#             sleep(2)


# class Thread2(Thread):
#     def run(self):
#         for i in range(5):
#             print("This is 2nd thread 2", i)
#             sleep(2)


# c1 = Thread1()
# c2 = Thread2()
# c1.start()
# print(c1.is_alive())
# sleep(1)
# print(c1.join())
# c2.start()
