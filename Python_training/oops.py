# OOPS:
''' 
oops means object oriented programming."object" is the blue print of the class
and the object contains data and code.data means the variables and code means
functions.they are six methods of oops:
1.class.
2.object.
3.Inheritance.
4.encapsulation.
5.poymorphism.
6.abstraction.
'''
# class:
'''
1.class is used to hold the function and data.
2.class is the blue print of object.
3.class is support to create the multiple objects.
4.class is defined as the class keyword.
'''
# program:




from abc import ABC, abstractmethod
class prasad():  # class
    print("Good Morning")


# Object:
'''
1.object is to hold the data and code.
2.data means variables and code means functions.
3.The process of object creation is called instiation.
'''
# program:


class prasad():  # class
    print("Gollapalli")


v = prasad()  # object

# Inheritance:
'''
1.Inheritance means to child program is similar to parent program.
2.base function is inherit to main function.
3.It is have four types of methods.
*)Single-level Inhertiance
*)Multi-level Inheritance
*)Multiple Inheritance
*)Hierarchical Inheritance 
'''
# Single-level Inheritance:
'''
1)Single-level Inheritance having one level.
2)It consist of one parent and one child.
3)parent class characteristics inherit by child class.
                Parentclass
                     |
                child class     
'''
# Program:


class parent:  # main class
    def ouput1(self):
        print("This is parent class")


class child(parent):  # Base class
    def ouput2(self):
        print("This is child class")


v = child()
v.ouput1()
v.ouput2()

# Multi-level Inheritance:
'''
1.Multi-level Inheritance consists of two(or)more classes.
2.From one level to another level the characteristics are Inherit
           GrandFather
               |
             Father
               |
             child   
'''
# program:


class GrandFather:  # Main class
    def output1(self):
        print("This is GrandFather class")


class Father(GrandFather):  # main class2
    def output2(self):
        print("This is Father class")


class child(Father):  # Base class
    def output3(self):
        print("This is Child class")


v = child()
v.output3()
v.output1()
v.output2()

# Multiple Inheritance:
'''
1.Multiple Inheritance consists of multiple levels like multi-level Inheritance.
2.Functioning is different from multi-level Inheritance
3.base function take characters from  both functions at a time.
                 Father  Mother
                   |       |
                    \     /
                    children               
'''
# Program:


class Father:
    def output1(self):
        print("This is father class.")


class Mother:
    def output2(self):
        print("This is Mother class.")


class child(Father, Mother):
    def output3(self):
        print("This is Child class.")


A = child()
A.output2()
A.output3()
A.output1()

# Hierarchical Inheritance:
'''
1.Hierarchical Inheritance also consists two(or)more levels.
2.Functioning is also different from both multi-level and multiple Inheritance.
3.Name child1 and child2 properties inherit from father.
                       Father 
                         / \
                        /   \
                     child1 child2
'''
# Program:


class Father:
    def output(self):
        print("This is Father class")


class child1(Father):
    def output1(self):
        print("This is child1 class")


class child2(Father):
    def output3(self):
        print("This is child2 class")


c = child1()
d = child2()
c.output()
c.output1()
d.output3()
d.output()

# Abstraction Method:
'''
1)Abstraction function has no body.
2)Object is not able to create for abstract method
3)Abstraction means hidden all details and represent the neccessary function
4)Import ABC package from abc method then it is said abstraction 
'''
# Program


class bike(ABC):
    @abstractmethod
    def speed(self):
        pass


class glamour(bike):
    def speed(self):
        print("The speed is 60kmph")


class pulsar(bike):
    def speed(self):
        print("The speed is 50kmph")


class honda(bike):
    def speed(self):
        print("The speed is 50kmph")


class duke(bike):
    def speed(self):
        print("The speed is 45kmph")


g = glamour()
g.speed()
h = honda()
h.speed()
