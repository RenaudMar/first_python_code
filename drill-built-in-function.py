#!/bin/python3

import math # import de la librairie math

text = "Hello World!" # creation de l'objet text
count_alpha = len(text) # longueur de notre objet test
count_float = float(count_alpha) # mise en float de count_alpha
pi = math.pi # pi de la librairie math
round_pi = round(pi, 2) # arroundi pi a la 2 decimal
#print(round_pi)
reversed_text = list(text[::-1]) # list mets en list le reverse de text car [::-1] reverse 
#print(reversed_text)

def user_age(): # Création de la fonction de permettant d'input age de l'user

    user_age_input = input("Enter your age : \n")
    age = str(user_age_input) # mise en str de l'input de l'user
    print(type(age)) # print le type de l'user

#user_age()

num = [2, 8, 1, 4, 6, 3, 7]
sorted_num = sorted(num)
#print(sorted_num)
sum_of_list = sum(num)
#print(sum_of_list)
min_value = min(num)
max_value = max(num)

def interpreter_string():  # Création de la fonction nous permettant interprétation de la string
    opperands = ["+", "-", "*", "/" ] # Création de la liste des opérandes
    calc = "1 + 2" # notre string
    string_interpret = 0 # création de la valeur pour string interpret nous permettant de calculer avec les operations suivantes
    
    for i in calc: # Creation d'une boucle for car nous cherchons une i sur le calc
        
        if i in opperands: #creation des conditions de si i apparait dans opperands
            integers = calc.split(i) # utilisation de split qui va couper a partir de i. i va être enlevé de calc dans ce ca + et nous laissé avec une liste.
        
        if i == "+": # si i est = +
            string_interpret = int(integers[0]) + int(integers[1]) # Création du calcule pour calcluer l'addition des integ crée au dessus 
        
        if i == "-":
            string_interpret = int(integers[0]) - int(integers[1])
        
        if i == "*":
            string_interpret = int(integers[0]) * int(integers[1])

        if i == "/":
            string_interpret = int(integers[0]) / int(integers[1])
    print(string_interpret) # print le résultat

#interpreter_string() # appel de la fonction