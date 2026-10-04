# name = "irfan"
# age = 20
# fee = 22.69
# print(name, age, fee)
# print(type(age))


# name = input("enter your name :")

# name = input("enter u r name")
# print(len(name))


# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("Go")
# else:
#     print("light is broken")


# Marks = int(input("Enter the student marks: "))
# if(Marks >= 90):
#     print("Grade = A")
# elif(Marks >= 80 and Marks<=90):
#     print("Grade = B")
# elif(Marks >= 70 and Marks<=80):
#     print("Grade = C")        
# else:
#     print("Grade = D")


# num = int(input("Enter any number: ")) 
# rem = num % 2
# if(rem == 0):
#     print("Even")
# else:
#     print("odd")

# a = 4
# b = 5
# c = 6

# if(a>b and a>c):
#     print("A is greatter number")
# elif(b>c):
#     print("B is greatter number")  

# else:
#     print("C is larger number ")







# Marks = [92, 84.5, 77.6, 22.03,45.23 ]
# print(Marks)
# print(Marks[0])
# print(Marks[1])
# print(Marks[3])
# print(len(Marks))





# student = ["arjun", 90, 87," irfan"]
# print(student[0])
# student[0] = "Mohammed"
# print(student)
# print(student[0], student[3]) 



# marks = [23, 33, 54, 88, 93]
# print(marks[1:3])
# print(marks[:5])
# print(marks[-4:-1])
# print(marks[-5:])




# list = [1, 4, 3, 2]
# list.append(5)
# list.sort()
# list.reverse()
# list.sort(reverse=True)
# list.insert(3, 6)
# print(list)





# tup = (12, 32 ,31, 54)

# tup = (12,)

# print(tup.count(32))
# print(type(tup))





# movi1=input("Ener the movie name ")
# movi2=input("Ener the movie name ")
# movi3=input("Ener the movie name ")

# list = []
# list.append(movi1)
# list.append(movi2)
# list.append(movi3)
# print(list)



# list1= [1,2, 3, 2, 1]
# list2= [1, 4, 3, 2]

# copy_list2= list1.copy()
# copy_list2.reverse()

# if(copy_list2==list2):
#     print("Palindrome")
# else:
#     print("not palindrome") 


# grade =["c", "d", "a", "a", "b", "b", "a"]
# grade.sort()
# print(grade)





#dictionary

# student = {
#     "Name" : "Irfan",
#     "Age" : 20,
#     "subjets" : {
#          "Aiml" : 98,
#          "python" :88,
#         "Java" :76,
#     }
    
# }

# print(student["subjets"]["Aiml"])




# #sets
# collection1 = {1,2, 3, 4, 4, 3, 5, 7, 6, 7, 2, 1, 2, 1}
# collection2 = {22, 34, 35, 2, 3, 4, 7}
# print(collection1.union(collection2))
# print(collection1.intersection(collection2))

# print(type(collection))
# print(len(collection))
# collection.add(9)
# collection.add(22)
# collection.add("Irfan")
# collection.add((1, 2, 3))

# collection.pop()
# collection.clear()
# # print(collection)
# # collection = set()  #empty set






# class WJ:
#     def __init__(s,a,b,t):
#         s.a,s.b,s.t=a,b,t;
#         s.v=set()
#     def dfs(s,x=0,y=0,p=[]):
#         if (x,y)in s.v:
#             return
#         p=p+[(x,y)]
#         if s.t in (x,y):
#             return p
#         s.v.add ((x,y))
#         for nx,ny in [(s.a,y),(x,s.b),(0,y),(x,0),(x-min(x,s.b-y),y+min(x,s.b-y)),(x+min(y,s.a-x),y-min(y,s.a-x))]:
#             r=s.dfs(nx,ny,p)
#             if r:
#                 return r
#     def solve(s):
#         for i in s.dfs():
#             print(i)
# WJ(4,3,2).solve()


count = 0 
while count < 5: 
    print(count) 
    count += 1