import time
import os
from time import sleep
from tqdm import tqdm
import random
import settings
import main

settings.HP()

def f(x):
        match x:
            case 'a':

                r = random.randint(0,1)
                if r == 1:
                    for x in range(101):
                        z = (settings.HP())-x
                        print ("disparo",z,"!")
                    main.start()
                        
                elif r == 0:
                    print("you miss all the shoots")

            case 'b':
                os.system('cls')
                pbar = tqdm(total= 100)
                for i in range(100):
                        y = random.uniform(0.1,0.2)
                        time.sleep(y)
                        pbar.set_description("Healing in progress")
                        pbar.update(i)
                pbar.close()
            case 'c':
                print ("you have espaced")
            case _:
                print ("what?")
                pass
