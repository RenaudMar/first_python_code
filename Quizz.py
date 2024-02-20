#!/bin/python3
import unicodedata

name_toto = "toto"
age_toto = 10

#unicode_toto = unicode(name_toto, "utf-8") #python 3 TOUTES string est unicode !!!!!!!!!

float_age_toto = float(age_toto)

revers_name = name_toto[::-1]
print(revers_name)
revers_age = str(age_toto)[::-1]
print(revers_age)

first_list = [1, 3, 2, 7, 4, 10, 46]
print(first_list)
second_list = first_list[2:5]
print(second_list)
third_list = first_list + second_list
print(third_list)
tuple_of_lists = list(zip(first_list, second_list))
print(tuple_of_lists)
first_list_more = first_list + [5]
print(first_list_more)
third_list_None = third_list + [None]
print(third_list_None)


my_list = [1,2,3,4,5]
n = 3

def multiplyList(my_list, n):
    
    res = n*my_list
    return res

print(multiplyList(my_list, n))

def multiplyLis(my_list, n=2):
    
    res = n*my_list
    return res

print(multiplyLis(my_list))

def third():

    x = 0
    
    while third_list_None[x] != None:
        print("elem = ", third_list_None[x])
        x += 1
    

third()

for pair in first_list:

    if pair %2 == 0:
        print(pair)

even_numbers = []

for element in first_list:
    if element % 2 == 0:
        even_numbers.append(element)

print(even_numbers)