#Owen Matyi 9/26/17

#13 page paper
papers = {"Page1":False, "Page2":False, "Page3":False, "Page4":False, "Page5":False, "Page6":False, "Page7": False, "Page8":False, "Page9":False, "Page10":False, "Page11":False, "Page12":False, "Page13":False,}
#school supplies
tools = {"pencil":False,"Pen":False, "DormKey":True, "StudentPass":True, "TeacherPass":False, "Paper":False, }
items = {}

#Variables
grade = 100
charge = 0
alchlvl = 0.0
money = 0.00
day = 0

#Defined functions
def character():
    print("Welcome to the first(definitely not) Ithaca college text based adventure game!")
    print(
        "We are just going to need a little bit of infomation so that we know where to request that quarter of a million dollars.")
    Char = input("What is your name?")
    age = int(input("How old are you going coming into IC?"))

    if age == 18:
        freshyr()
    elif age == 19:
        sophyr()
    elif age == 20:
        jryr()
    elif age == 21:
        senyr()
    elif age >= 22:
        grad()
    else:
        print("You are not old enough to attend college see ya in the future")
        exit(0)


def win():
    print("you win!")
    exit(0)

def freshyr():
    print("Welcome to freshman year!")



def sophyr():
    print("Welcome back for Sophomore year!")


def jryr():
    print("Oh you are still here for Junior year welcome back!")


def senyr():
    print("Your are on the home stretch for Senior year!")


def grad():
    print("you graduated already why the fuck you here?")
    win()



