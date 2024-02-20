#!/bin/python3

age = 32   #création de l'attribut age avec une valeur de 32
age += 10 # addition de l'age de 10 grace au += qui additionne et calcule le résultat
divAge = age // 7 # division de l'age par 7 et le \\ indique que l'on veut le résultat en integer
textDiv = "{} divided by 7 equals {}".format(age, divAge) # création du text avec le .format

restDiv = age % 7 #Modulo qui permet d'avoir le restant de la division de divAge
expDiv = restDiv ** 3 # Met le resultat de restDiv en puissance 3

def program():        #création d'une fonction pour que l'utilisateur puisse rentrer un input

    user_input = input("pls enter a number \n")  #le \n présent permet un retour a la ligne pour que l'user écrit sur une nouvelle ligne
    print(user_input, type(user_input)) #montre le résultat de l'user et montre qu'elle classe son input fait partie

#program()

# Creation d'une liste des items présent dans la liste de course
bottle_milk = 0.45
raw_cider = 3.85
bag_flour = 0.9
packet_of_butter = 0.77
jar_nutella = 1.87

# Création de la fonction order qui permet de calculer notre liste de course

def order():

    order_price = (bottle_milk*2) + (raw_cider*3) + (bag_flour*1) + (packet_of_butter*1) + (jar_nutella*1) # permet de calculer le prix de notre commande
    allowanceMoney = 20.00 #l'argent que nous possèdons pour nos courses
    money_rest = order_price - allowanceMoney # Calcule le prix restant de notre course
    amountMissing = allowanceMoney - order_price # Calcule le prix manquant si il manque de l'argent pour notre commande

    if allowanceMoney >= order_price: #creation d'une condition pour montrer que l'on a assez d'argent pour la commande
        print("You have spent " + str(order_price) + " you have left " + str(money_rest))

    elif allowanceMoney < order_price: #creation d'une condition si l'on a pas assez d'argent pour passer commande
        print("Sorry you're missing" + amountMissing + "euros")

    else :   # Fin de condition est si l'argent qui nous reste est égal a 0
        money_rest = 0
        print("You are broke !")

#order()

def input_value(): #Création de fonction différente valeur 

    first_input = int(input("Enter your first value \n")) # Creation d'une variable en int pour pouvoir voir le min
    second_input = int(input("Enter your second value \n")) # Creation variable
    min_value = min(first_input, second_input) # Creation d'une cariable permettant de montrer avec le min le plus petit input
    print("The smallest value is: " + str(min_value)) 

#input_value() #Appel de la fonction

#Creation de la fonction pour la taille de input
    
def input_len():

    FirstInput = input("waiting for input ^^\n")
    SecondInput = input("An other one pls  ^^\n")
    #len_input = max(len(FirstInput), len(SecondInput))             # Tentative de créer avec max(len...) Problème ca n'affiche pas l'input mais la longueur de l'input
    #print("The bigger input is : " + str(len_input))

    if len(FirstInput) > len(SecondInput):                      # Creation de conditions des variables de notre fonction avec if
        print("\n The largest input is: " + FirstInput)

    elif len(FirstInput) < len(SecondInput):
        print("\n The largest input is: " + SecondInput)

    else:
        print("Les deux inputs on la même longueur")


#input_len()
        
# Script pour convertir € en $
        
def money_converter():  #Creation de la fonction convertisseur
    euros_symbol = "E"   #Liste de variables présentes dans la fonction
    dollars_symbol = "$"
    euros = 0.92
    dollars = 1.08

    input_currency = input("Choose E or $ \n") # Demande a l'user d'encoder 

    if input_currency.upper() == euros_symbol:  #Condition de si l'input de l'user est = euros_symbol
        
        user_amountE = float(input("Enter the ammount you want to convert in euros: \n"))   #demande a l'user d'encoder le montant a convertir et transformation en fmoat pour le calcule
        amountE_converter = user_amountE * dollars # Calcule du résultat
        print("Your amount in dollars is: " + str(amountE_converter)) 
    
    elif input_currency.upper() == dollars_symbol:
        
        user_amout_D = float(input("Please enter the amount you want to convert in dollars: \n"))
        amountD_converter = user_amout_D * euros
        print("Your amount in euros is: " + str(amountD_converter))

    else:
        print("currency not know sorry :(")

money_converter()

