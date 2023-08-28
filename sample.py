"""Duplicates"""
# n = int(input('enter the no'))
# email = []
# for i in range(n):
#     ema = int(input('enter the unique email address'))
#     email.append(ema)
# a =len(email)
# b = len(set(email))
# if a-b>0:
#     print(a-b)

"Device Name System"
# n = int(input('enter the no'))
# device = []
# for i in range(n):
#     dec = input('enter the unique email address')
#     device.append(dec)
# coun =0
# for r in range(len(device)):
#     k = device[r]
#     a = device.count(k)
#     if a >=1 and coun == 0:
#         device[r] = device[r]
#     elif a>=1:
#         coun = coun + 1
#         device[r] = device[r]+str(coun)
# print(device)



# n= input('enter the string:').replace("@",' ')
# k = n.replace('$'," ")
# l = k.split()
# b =[]
# for i in range(len(l)):
#     a = len(l[i])
#     b.append(a)
# c = max(b)
# print(c+1)




# n = input('enter the string:')
# k =[]
# for i in n:
#     if i in n:
#         l = n.count(i)
#         k.append(l)
# a = min(k)
# b = k.index(a)
# c = n[b]
# print(c)
#


# password = input('enter the password:')
# upper =0
# lower =0
# num=0
# space=0
# slash=0
# if len(password)>6:
#     for i in range(len(password)):
#         if 'A' <= password[i] <= 'Z':
#             upper = upper+1
#         elif 'a' <= password[i] <= 'z':
#             lower = lower+1
#         elif password[i].isnumeric():
#             num = num+1
#         elif password[i].isspace():
#             space = space+1
#         elif password[i] != '/':
#             slash = slash+1
#
# if upper >= 1 and lower >= 1 and num >= 1 and space ==0 and slash ==0 :
#     print('password valid')
# else:
#     print('Invalid password, try again')

# word = input('enter the word').split()
# n = len(word)
# print(n//2)

# n = input('enter the number:')
# for i in range(len(n)):
#     k = n[:i+1]
#     l = n[i+1::]
#     first =0
#     second =0
#     for j in k:
#         for m in l:
#             first = first+int(j)
#             second = second+int(m)
#             if first>second:
#                 print(first)
#
#
#             else:
#                 print(second)
#
#
#     break

#
# def countDuplicate(numbers):
#     c = 0
#     for i in set(numbers):
#         if numbers.count(i) > 1:
#             c += numbers.count(i) - 1
#     return c
#




# a = [7, 3, 46, 2, 8]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x:x%2 ==0,k))
# odd = list(filter(lambda y :y % 2 !=0,k))
# print(even)
# print(odd)
# n =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = list(map(lambda y : y*y,n))
# print(square)
# cube = list(map(lambda y : y*y*y,n))
# print(cube)

# x = lambda x: x[0]=='p'
# print(x('python'))
#
# square = list(map(lambda y : y*y,n))
# print(square)
# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))
#
# n = input('enter the string:')
# k = lambda x: True if x.isdigit() else False
# print(k(n))
# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# from functools import reduce
#
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
#                               range(n - 2), [0, 1])
#
# print("Fibonacci series upto 2:")
# print(fib_series(2))
#
# a = [1, 2, 3, 5, 7, 8, 9, 10]
# b = [1, 2, 4, 8, 9]
# y = lambda x: x in a
# print(list(filter(y,b)))
# # Intersection of the said arrays: [1, 2, 8, 9]
#
# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
#
# result = list(filter(lambda x: x in array_nums1, array_nums2))
# print ("\nIntersection of the said arrays: ",result)
# n = int(input('enter the number:'))
# t = int(input('enter the number2:'))
# l =[]
# for  i in range(n):
#     k = int(input('entre the number'))
#     l.append(k)
# total =0
# for i  in l:
#     if i<=t:
#         total = total +1
#     else:
#         total = total+2
# print(total)
# #
#
# n = int((input('enter the no:')))
# home = []
# for i in range(n):
#     h = int(input('enter the home'))
#     home.append(h)
# people =[]
# for i in range(n):
#     p = int(input('enter the people'))
#     people.append(p)
# count = 0
# for i in range(len(people)):
#     for j in range(len(home)):
#         if people[i] <= home[j]:
#             count += 1
#             home[j]=-1
#             break
# print(n-count)
# print(home)


# f = int(input('enter the no1:'))
# l = int(input('enter the no2:'))
# m =1
# for i in range(f,l+1):
#     m = m*i
# print(m)
# # string = str(m)
# # k = string.replace('0',' ')
# # print(k)

# import array
# a = array.array('i', [1, 2, 3])
# for i in a:
#     print(i, end=' ')    #OUTPUT: 1 2 3
# a = array.array('i', [1, 2, 'string'])
# #OUTPUT: TypeError: an integer is required (got type str)
# a = [1, 2, 'string']
# for i in a:1
#    print(i, end=' ')    #OUTPUT: 1 2 string


# my_list = [[10,20,30],[40,50,60],[70,80,90]]
# flattened = [x for temp in my_list for x in temp]
# print(flattened)

# Python code to demonstrate range() vs xrange()
# on basis of return type

# initializing a with range()
a = range(1,10000)

# initializing a with xrange()
# x = xrange(1,10000)

# testing the type of a
print ("The return type of range() is : ")
print (type(a))

# testing the type of x
# print ("The return type of xrange() is : ")
# print (type(x))













