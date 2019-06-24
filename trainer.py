import cmd
import random
import os
import time
import smtplib
import datetime

'''
Basic Math Trainer

'''

def get_date(s):
    return s.join([str(now.month),str(now.day),str(now.year)])

directory = os.path.abspath(os.path.dirname(__file__))
save_dir = os.path.join(directory, "logs")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

now = datetime.datetime.now()
save_name = "save_" + get_date("_") + ".txt"

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

class MultSmall:
    def __init__(self):
        self.name = "Small Digit Multiplication"
    def next(self):
        self.a = random.randint(2,5)
        self.b = random.randint(2,5)
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
levels = [Add2D(),Add3D(),Sub2D(),Sub3D(),MultSmall()]
question_log = []
daily_goal = [10,5,10,5,0]


def send_report():
    load_player()
    fromaddr = 'mathtrainer123456@gmail.com'
    toaddrs  = 'ivanovajulia@yahoo.com'
    msg = 'Subject: Adrian Math Report\r\n'
    msg = msg + '\r\n'
    msg = msg + 'Adrian Math Report '
    msg = msg + get_date("\\") + "\r\n"
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
def points_on_level(level):
    if not level.name in player.keys():
        return 0
    else:
        return player[level.name]
    

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
        print("###########################\t" + get_date("/"))
        print("WELCOME TO THE MATH TRAINER\t(" + extra + ")")
        print()
        print("1)\tSTART")
        print("2)\tDAILY TRAINING")
        print("3)\tPROFILE")
        print("4)\tSAVE")
        print("5)\tSEND REPORT")
        print("6)\tEXIT")
        print()
        k = input(":: ")
        
        if k == '1':
            start()
        elif k == '2':
            daily_training
        elif k == '3':
            profile()
        elif k == '4':
            save_player()
        elif k == '5':
            send_report()
            print("REPORT SENT")
            print("PRESS ENTER TO RETURN")
            input("")
        elif k == '6':
            exit_trainer()
        elif k == 'wipe':
            print()
            print()
            print("WIPE ALL SAVED DATA AT:")
            print(save_file)
            print()
            print("[y/n]")
            if input(":: ") == 'y':
                print("ALL DATA WIPED")
                global player, question_log
                player = {}
                question_log = []
                save_player()
            print()
            print("PRESS ENTER TO RETURN")
            input("")
        elif k == 'log':
            [print(q) for q in question_log]
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
    print("#"*(16 + len(level.name)) + "\tPoints: " + str(points_on_level(level)))
    print("------| " + level.name + " |------")
    print("#"*(16 + len(level.name)))
    print("type \'q\',\'quit\', or \'exit\' to exit")
    print()
    print()
    level.next()
    print("##] " + level.question())
    u = level.wrong()
    tries = 0
    while tries < 3 and not level.isCorrect(u):
        k = input(":: ")
        tries += 1
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
            tries -= 1
    if level.isCorrect(u):
        print("##] Good Job!")
        give_points(level.points(),level)
        save_player()
        question_log.append(level.question() + " | tries: " + str(tries))
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


def daily_training():
    global daily_goal
    counts = [0 for l in levels]
    while sum(counts) < sum(daily_goal):
        options = [i for i in range(len(daily_goal)) if daily_goal[i] - counts[i] > 0]
        selection = options[random.randint(0,len(options)-1)]
        level = levels[selection]
        clear()
        print("##############################")
        print("------| DAILY TRAINING |------\t Progress: ")
        print("##############################\t" + str(sum(counts)) + "/" + str(sum(daily_goal)))
        print()
        print(level.name)
        print()
        print()
        level.next()
        print("##] " + level.question())
        u = level.wrong()
        tries = 0
        while tries < 3 and not level.isCorrect(u):
            k = input(":: ")
            tries += 1
            try:
                u = int(k)
            except:
                print("##] Seems like that is not a number.")
                print("##] Try again")
                print()
                tries -= 1
        if level.isCorrect(u):
            print("##] Good Job!")
            counts[selection] = counts[selection] + 1
            give_points(level.points(),level)
            save_player()
            question_log.append(level.question() + " | tries: " + str(tries))
            print()
        else:
            give_points(-1,level)
            save_player()
            question_log.append(level.question() + " | Incorrect")
            print()
            print("Let's Try a different one :(")
            print()
        time.sleep(delay)
    question_log.append("DAILY TRAINING COMPLETE")

############

'''
Start Trainer
'''
menu()
    

############
