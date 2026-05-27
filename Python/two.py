##lamda function


##a lambda function is a small function that can take any number of arguments but have only one expression


# x=lambda a,b: a*b
# print(x(2,3))




#######RECURSIVE FUNCTION= a function which calls itself, it has one base case used to terminate the recursion and one recursive case , the function calling itself with modified arguments


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))



# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+ fibo(n-2)
    
# print(fibo(7))


##finding the sum of all the elements of the list using recursion

# def sum(list):
#     if len(list)==0:
#         return 0
#     else:
#         return list[0]+sum(list[1:])
    
# my_list=[3,5,6,7,8]
# print(sum(my_list))


##range function

# x=range(3,10)
# print(x)


# for i in range(10):
#     print(i)









###OOP python is oo language allowing you to structure the code using the classes and the objects


# class first:
#     x=5

# o1=first()
# print(o1.x)



# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# s1=student("ram",34)
# print(s1.name)
# print(s1.age)




##

# class student:
#     def __init__(self,name,age):
#         self.name=name  ##self parameter ,, name=property of the class
#         self.age=age

#     def greet(self):   ##class method
#             print("hello"+self.name)

# s1=student("Ram",45)
# s1.greet()




######Inheritence==inheritence allows us to define the class that inherits all the methods and the properties of the another class



# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(self.name,self.age)
# x=person("ram",4)
# x.display()


# class student(person):
#     pass
  

# x1=student("hari",5)
# x1.display()



##python polymorphism

##example of the polymorphims function in the python is len()


# class car:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

#     def move(self):
#         print("drive")

# class plane:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

#     def move(self):
#         print("fly")

# class boat:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

#     def move(self):
#         print("sail")

# c=car("ford","mustang")
# p=plane("ibi","sf")
# b=boat("af","rg")


# for x in (c,p,b):
#     x.move()
        



###Encapsulation

##encapsulation is about protecting the data inside the class


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

# p1=Person("ram",2)
# print(p1.name)
# print(p1.__age)
        


with open("demo2.txt",'a') as f:
    f.write("Madhu")

with open("demo2.txt",'r') as f:
    print(f.read())

import os
os.remove("demo.txt")