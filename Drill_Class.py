#!/bin/python3

class Becodian: #Création d'une classes
    def __init__(self, name, is_staff_member): #def __init__ permet de crées des attributs qui seront présentent quand nous allons créer l'objet

        self.name = name # self fais référence a l'objet lui même
        self.is_staff_member = is_staff_member


    def introduce_becodian(self): # Creation d'une fonction if pour la condition de is_staff_member
        if self.is_staff_member:
            return f"{self.name} is a staff member !" # condition si is_staff_member est True
        else:
            return f"{self.name} is a learner !" # condition si is_staff_member est false

class Learner(Becodian): # Création de la classe learner et héritage de la classe Becodian
    def __init__(self, name,  promotion, campus): # definition des attributs qui devront être présent dans la classes Learner
        super().__init__(name, False) # super() fais référence a la classe ce situant

        self.promotion = promotion # attributs de la classe
        self.campus = campus

    def introduce_learner(self): # Création de la fonction pour introduce le learner
        indroduction = super().introduce_becodian() + self.promotion +" " +self.campus # utilsation de super(). pour reprendre la fonction introduce_becodian() et les plus pour rajouté les arguments de notre classe
        return indroduction

jeremy = Learner("Jeremy","Bouman 1","Charleroi") # objet jeremy de la classe learner son nom, sa promotion, campus.
print(jeremy.introduce_learner()) # print l'objet jeremy avec la fonction introduce learner
Renaud = Becodian("Renaud", True)
print(Renaud.introduce_becodian())