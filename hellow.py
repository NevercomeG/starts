from re import X
import os
import functions
import settings

settings.HP()

os.system('cls')

print ("What would you do?")
menu = input("| a: Damage | b:Heal | c: escape | ")
functions.f(menu)
