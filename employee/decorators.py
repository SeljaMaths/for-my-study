# def outer(x):
#     def inner(y):
#         z = x+y
#         return z
#     return inner
# x = outer(10)
# y = x(5)
# print(y)
# print('''---------nested function--------''')


# def add(x,y):
#     return x+y
#
#
# def multiply(add,x,y):
#     return add(x,y)
#
#
#
# re = multiply(add,7,8)
#
# print(re)
#
# print("-------------pass function as an  argument-----------------")

# def greeting(name):
#     def hell():
#         return 'welocome' +' '+ name
#     return hell
# x = greeting('selja')
# print(x())
# print('============Return a Function as a Value=======================')


# def invite(func):
#     def invite_per():
#         print('Hi, Hello')
#         func()
#     return invite_per
#
# def next_process():
#     print('how are you')
#
# deco_func = invite(next_process)
# deco_func()
#
# print('---------------decorator__________________')
#
#
#
# def invite(func):
#     def invite_per():
#         print('Hi, Hello')
#         func()
#     return invite_per
# @ invite
# def next_process():
#     print('how are you')
# next_process()


def calculatetotal(val1, val2):
    return val1 + val2


def checkvalue(func):
    # Inner Function to Validate Values
    def wrapper(val1, val2):
        if val1 >= 200 or val2 >= 200:
            # Call the Original Function
            return func(val1, val2)

    # Return the final result
    return wrapper


cal = checkvalue(calculatetotal)
total = cal(20, 230)
print(total)