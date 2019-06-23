import cmd
import random
import os
import time
import smtplib
import datetime

'''
Basic Math Trainer

'''

directory = os.path.abspath(os.path.dirname(__file__))
save_dir = os.path.join(directory, "logs")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

now = datetime.datetime.now()
save_name = "save_" + str(now.month) + "_" + str(now.day) + "_" + str(now.year) + ".txt"

save_file = os.path.join(save_dir, save_name)


#########################################
#########################################
#########################################

class Add2D:
    def __init__(self):
        self.name = "Two Digit Addition"
    def next(self):
        self.a = random.randint(9,99)
        self.b = random.randint(9,99)
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

class Mult1_6:
    def __init__(self):
        self.name = "Small Digit Multiplication"
    def next(self):
        self.a = random.randint(1,6)
        self.b = random.randint(1,6)
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

delay = 1

player = {}
levels = [Add2D(),Add3D(),Sub2D(),Sub3D(),Mult1_6()]
question_log = []


def send_report():
    load_player()
    fromaddr = 'mathtrainer123456@gmail.com'
    toaddrs  = 'ivanovajulia@yahoo.com'
    msg = 'Subject: Adrian Math Report\r\n'
    msg = msg + '\r\n'
    msg = msg + 'Adrian Math Report '
    msg = msg + str(now.month) + "\\"
    msg = msg + str(now.day) + "\\"
    msg = msg + str(now.year) + "\r\n"
    msg = msg + str(player) + "\r\n"
    for line in question_log:
        msg = msg + line + "\r\n"
    username = 'mathtrainer123456@gmail.com'
    password = 'qweRTY123$%^'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def give_points(points,level):
    try:
        player[level.name] = player[level.name] + points
    except:
        player[level.name] = points

def save_player():
    global player
    file = open(save_file,'w')
    file.write(str(player))

def load_player():
    global player
    player = eval(open(save_file).read())

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
        print()
        print("1)\tSTART")
        print("2)\tPROFILE")
        print("3)\tSAVE")
        print("4)\tSEND REPORT")
        print("5)\tEXIT")
        print()
        k = input(":: ")
        
        if k == '1':
            start()
        elif k == '2':
            profile()
        elif k == '3':
            save_player()
        elif k == '3':
            send_report()
        elif k == '5':
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
        elif k == 'log':
            [print(q) for q in question_log]
            print("PRESS ENTER TO RETURN")
            input("")
        elif k == 'report':
            send_report()
            print("REPORT SENT")
            print("PRESS ENTER TO RETURN")
            input("")
        

def exit_trainer():
    print("###########################")
    print("THANK YOU FOR TRAINING")
    print("###########################")
    print()
    time.sleep(delay)
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
    print("PRESS ENTER TO RETURN")
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
    print("#"*(16 + len(level.name)))
    print("------| " + level.name + " |------")
    print("#"*(16 + len(level.name)))
    print("type \'q\',\'quit\', or \'exit\' to exit")
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
            time.sleep(delay)
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
        question_log.append(level.question() + " | tries: " + str(trys))
        print("You Got " + str(level.points()) + " Point")
        print()
    else:
        give_points(-1,level)
        save_player()
        question_log.append(level.question() + " | Incorrect")
        print("You Lost 1 Point")
        print()
        print("Let's Try a different one :(")
        print()
    time.sleep(delay)
    run_level(level)


############

'''
Start Trainer
'''
menu()
    

############
