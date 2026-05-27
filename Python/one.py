# x="banana"
# for i  in x:
#     print(i)



# age=22
# print(f"I am Madhusudan {age}")


##List===ordered,changeable
# list=["ram","shyma","hari"]
# print(list[1])
# list.append("sita")
# print(list)
# list.insert(1,"gita")
# print(list)

# list=["ram","shyma","hari"]

##for loop

# for x in list:
#     print(x)



##while loop
# i=0;
# while i<len(list):
#     print(list[i])
#     i=i+1



# newlist=[]

# for x in list:
#     newlist.append(x)
# print(newlist)




##list join

# list1=["ram","hari","sita"]
# list2=[1,2,3]
# print(list1+list2)



##Tuple==tuples are also ordered but not changeable but can allow duplicates

# tup=("ram","shyam","hari")
# print(tup[1])

##we cannot update the tuples so we have to convert it to the list


# fruits=("apple","banana","litchi")
# list=list(fruits)
# list[1]="kiwi"
# fruits=tuple(list)
# print(fruits)






##sets==python sets are used to store multiple items in a single varible
##sets are unordered unchangeable and unindexed and dont allow duplicates


# set1={"apple","ball","cat","dog"}
# set1.add("elephant")
# for x in set1:
#     print(x)

# print("apple" not in set1)



# set1={"one","two","three"}
# set2={"four","five","six"}
# set3={"seven","eight"}
# set=set1.union(set2,set3)
# print(set)

##sets support the operations like union, intersection, difference


##Dictionaries

##dictionary is ordered changeable but donot allow duplicates


# dict={
#     "name":"ram",
#     "age":12,
#     "address":"KTM"
# }

# print(dict["name"])
# print(dict.keys())




# a=2
# b=5
# print("a is greater than b") if a>b else print("b is greater then a")


# day=2
# match day:
#     case 1:
#         print("sun")
#     case 2:
#         print("Mon")
#     case 3:
#         print("Tues")



##while loop

# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1


##Python function

# def func():
#     print("Hello")

# func()



# def func(name):   ##parameter
#     print("My name is "+name)

# func("Madhusudan") ##argument


##parameter are just variables listed in the function definition
##arguments are the actual values that are passed while calling the function




## *args=arbitrary arguments are used when we dont know how many arguments will be passed
##  *args typically becomes the tuple containing all the passed arguments

# def students(greet,*args):
#     for arg in args:
#      print("the topper student  "+arg, "is saying"+greet)

# students("Hello","ram","shyam","hari")


## **kwargs==Keyword arguments are basically used to recieve any number of the keyword arguments

# def student(**args):
#     print ("his last name is "+ args["lname"])

# student(fname="ram", lname="singh")



##Decorator is basically a function that takes another function as input and returns another function as output
###decorator allows you to add additional functionality to the function without changing its code


def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def func():
    return "hello world"

print(func())
