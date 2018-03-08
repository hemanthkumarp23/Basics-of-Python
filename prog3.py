# Dictionary:

# Program 1:
# x = {1:"Speckbit", 2:"World", 3:"Quiet"}
# y = input("Enter the value to be searched: ")
# z = []
# for k in x.values():
#     z.append(k)
#
# if y in z:
#     print(True)
# elif y not in z:
#     print(False)

# Program 2:
# x = {1:"Speckbit", 2:"World", 3:"Quiet"}
# for k, v in x.items():
#     # print(k,end="")
#     # print("--",end="")
#     # print(v)  or
#     print(str(k) + "--" + v)  or
#     print("{}--{}".format(k,v))

# Program 3:
# x = {'a':"Speckbit", 'b':"World", 'c':"Quiet"}
# y = input("Enter the key to be searched: ")
# z = []
# for k in x.keys():
#     z.append(k)
#
# if y in z:
#     print("key is",y)
# else:
#     print(False)

# Program 4:
# x = eval(input("Enter the number of candidates to be added: "))
# z = {}
# i = 1
# while(i <= x):
#     y = input("Enter the usn: ")
#     w = input("Enter the name: ")
#     z[y] = w
#     i += 1
#
# print(z)
