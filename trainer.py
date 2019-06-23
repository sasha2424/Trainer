import cmd
import random
import os
import time

directory = os.path.abspath(os.path.dirname(__file__))
save_path = os.path.join(directory, "save.txt")

print(save_path)


'''
Basic Math Trainer

'''

#########################################
#########################################
#########################################

class Add2D:
    def __init__(self):
        self.name = "Two Digit Addition"
    def next(self):
        self.a = random.randint(1,5)
        self.b = random.randint(1,2)
        self.c = self.a + self.b
    def wrong(self):
        return self.c -1
    def question(self):
        return str(self.a) + " + " + str(self.b) + " = ?"
    def isCorrect(self,u):
        return self.c == u
    def points(self):
        return 1

class Add3D:
    def __init__(self):
        self.name = "Three Digit Addition"
    def next(self):
        self.a = random.randint(99,999)
        self.b = random.randint(99,999)
        self.c = self.a + self.b
    def wrong(self):
        return self.c - 1
    def question(self):
        return str(self.a) + " + " + str(self.b) + " = ?"
    def isCorrect(self,u):
        return self.c == u
    def points(self):
        return 1

class Sub2D:
    def __init__(self):
        self.name = "Two Digit Subtraction"
    def next(self):
        n1 = random.randint(9,99)
        n2 = random.randint(9,99)
        self.a = max(n1,n2)
        self.b = min(n1,n2)
        self.c = self.a - self.b
    def wrong(self):
        return self.c - 1
    def question(self):
        return str(self.a) + " - " + str(self.b) + " = ?"
    def isCorrect(self,u):
        return self.c == u
    def points(self):
        return 1

class Sub3D:
    def __init__(self):
        self.name = "Three Digit Subtraction"
    def next(self):
        n1 = random.randint(99,999)
        n2 = random.randint(99,999)
        self.a = max(n1,n2)
        self.b = min(n1,n2)
        self.c = self.a - self.b
    def wrong(self):
        return self.c - 1
    def question(self):
        return str(self.a) + " - " + str(self.b) + " = ?"
    def isCorrect(self,u):
        return self.c == u
    def points(self):
        return 1

class Mult1_5:
    def __init__(self):
        self.name = "Small Digit Multiplication"
    def next(self):
        self.a = random.randint(1,5)
        self.b = random.randint(1,5)
        self.c = self.a * self.b
    def wrong(self):
        return self.c - 1
    def question(self):
        return str(self.a) + " * " + str(self.b) + " = ?"
    def isCorrect(self,u):
        return self.c == u
    def points(self):
        return 1

#########################################
#########################################
#########################################


player = {}
levels = [Add2D(),Add3D(),Sub2D(),Sub3D()]


def give_points(points,level):
    try:
        player[level.name] = player[level.name] + points
    except:
        player[level.name] = points

def save_player():
    global player
    file = open(save_path,'w')
    file.write(str(player))

def load_player():
    global player
    player = eval(open(save_path).read())

def clear():
    os.system('cls')

def menu():
    extra = ""
    try:
        load_player()
        extra = "Save Loaded"
    except:
        extra = "No Saved Data"
    while True:
        clear()
        print("###########################")
        print("WELCOME TO THE MATH TRAINER    (" + extra + ")")
        print("1)\tSTART")
        print("2)\tPROFILE")
        print("3)\tSAVE")
        print("4)\tEXIT")
        print()
        k = input(":: ")
        
        if k == '1':
            start()
        elif k == '2':
            profile()
        elif k == '3':
            save_player()
        elif k == '4':
            exit_trainer()
        elif k == 'wipe':
            print()
            print()
            print("WIPE ALL SAVED DATA AT:")
            print(save_path)
            print()
            print("[y/n]")
            if input(":: ") == 'y':
                print("ALL DATA WIPED")
                player = {}
                save_player()
        

def exit_trainer():
    print("###########################")
    print("THANK YOU FOR TRAINING")
    print("###########################")
    exit()

def profile():
    clear()
    print("#"*10)
    print("--| USER PROFILE |--")
    print()
    try:
        load_player()
        for k in player.keys():
            print(k + " - " + str(player[k]))
    except:
        print("No Saved Data")
    print()
    print("RETURN TO MENU")
    input("")

def start():
    while True:
        clear()
        print("############")
        print("SELECT LEVEL")
        for i,L in enumerate(levels):
            print(str(i+1) + ") " + L.name)
        print()
        print()
        print("q - return to menu")
        k = input(":: ")
        if not k == 'q':
            try:
                start_level(levels[int(k)-1])
            except:
                print()
        else:
            break

def start_level(level):
    run_level(level)

def run_level(level):
    clear()
    print("#"*(14 + len(level.name)))
    print("------|" + level.name + "|------")
    print("#"*(14 + len(level.name)))
    print()
    print()
    level.next()
    print("##] " + level.question())
    u = level.wrong()
    trys = 0
    while trys < 3 and not level.isCorrect(u):
        k = input(":: ")
        trys += 1
        if k == 'q' or k == 'quit' or k == 'exit':
            print("Returning to level select...")
            print()
            time.sleep(.5)
            exit()
        try:
            u = int(k)
        except:
            print("##] Seems like that is not a number.")
            print("##] Try again")
            print()
    if level.isCorrect(u):
        print("##] Good Job!")
        give_points(level.points(),level)
        save_player()
        print("You Got " + str(level.points()) + " Point")
        print()
    else:
        give_points(-1,level)
        save_player()
        print("You Lost 1 Point")
        print()
        print("Let's Try a different one :(")
        print()
    time.sleep(1)
    run_level(level)


############

'''
Start Trainer
'''
menu()





############
