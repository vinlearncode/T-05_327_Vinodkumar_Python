# Operators are 7 types:-
#     1.Arithmetic Operator:-
#         Addition(+)
#         Subtraction(-)
#         Multiplication(*)
#         Floor division(//)
#         Division(/)
#         Exponential(**)
#         Modulus(%)
#     2.logical Operator:-
#         AND OR NOT
#     3.Comparision Operator:-
#         ==,>=,<=,!=
#     4.Assignment Operator:-
#         ==
#     5.Membership Operator:-
#         IN,NOT IN
#     6.Identity Operator:-
#         IS,IS NOT
#     7.Bitwise Operator:-


# Arithmetic operations on 2 numbers and print result program.

# a=55
# b=67
# print(a-b)
#
# #Addition:-
# print(a+b)
#
# #Multiplication:-
# print(a*b)
#
# #Division:-
# print(a/b)
#
# #Modulus:-
# print(a%b)
#
# #Exponential:-
# print(a**b)
#
# #Floor Division:-
# print(b//a)


# Comparision Operator:-
#     == is two objects value equality.
#     is the reference equality.

# a=7;b=20
# if a<b:
#     print('Yes')
# else:
#     print('NO')
#
# print(a==b)
# print(a!=b)
# print(a is not b)
# print(a is b)

# Assignment Operator:-
# a=b=7
# print(a)


#And or operators:-
# Example-1:
# price=int(input('enter an price: '))
# movie_rating=float(input('enter an rating: '))
# if price<=200 and movie_rating>=7:
#     print('go to the movie')
# else:
#     print('NO movie')

# Example_2
# a=(True and False) and (False or True) or (True and True) or (True and False)
# print(a)

# print(not True) --->False
# print(not False) --->True

# Operator precedence.
# meal='sandwich'
# money=49
#
# if meal=='fruit' or meal=='sandwich' and money>=50:
#     print('lunch is being delivered')
# else:
#     print('lunch is not delivered')

#Membership Operator:-
# in:-Returns True if a sequence with the specified value is present
# in the object
#
# not in:-Returns True if a sequence with the specified value is not present
# in the object
#
# Example for in operator:-

# x='Rani'
# y='vinil'
# lst=['Rani','vinod','vinay','durgarao']
# for i in lst:
#     print(x in lst)
# print()
#     print(x not in lst)

#Identity Operator:-
# The is operator is useful to compare whether two objects are the same or not. It will internally
# compare the identity number of the objects. If the identity numbers of the objects are the same,
# it will return True; otherwise, it returns False.

# a=25;b=25
# if a is b:
#     print("Both of them have same identity{a is b}")
# else:
#     print('Both of them have different identity{a is not b}')
#
# a=25;b=50
# if a is b:
#     print("Both of them have same identity{a is b}")
# if a is not b:
#     print('Both of them have different identity{a is not b}')