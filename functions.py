import time
import os
from time import sleep
from tqdm import tqdm
import random
from settings import *

def fmenu():

    Health = player("88888",100,100,100)
    while True:
        os.system('cls')
        print ("What would you do?")
        menu = input("| a: Damage | b:Heal | c: escape | ") #menu   
        match menu:
            # Damage
            case 'a': 
                r = 1
                if r == 1:
                    os.system('cls')
                    y = random.randint(3,5)
                    for x in range(y):
                        z = Health.health - x
                        print ("shots",z,"!")
                    time.sleep(0.5)

                elif r == 0:
                    print("you miss all the shoots")
                    os.system('cls')
                    time.sleep(0.5)
            # heal
            case 'b': 
                os.system('cls')
                pbar = tqdm(total= 100)
                for i in range(100):
                        y = random.uniform(0.1,0.2)
                        time.sleep(y)
                        pbar.set_description("Healing in progress")
                        pbar.update(i)
                pbar.close()

            case 'c': # escape
                print ("you have espaced")
                break
            case _: #in case invalid selection
                print ("bye!")
                break
