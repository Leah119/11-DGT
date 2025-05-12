"""A short quiz that tests people on their knowledge of famous Jeffreys.

It also includes a few other Jeff-related questions.

For each correct answer they get one point added to their score, which is

then read out at the end of the quiz.

It is designed so that people 10 and under can not play.
"""

import easygui

QUESTIONS = 10  #is the amount of questions the quiz runs
MIN_AGE = 14  #required age needed to play the quiz
MAX_AGE = 18  #the cut-off age, if you're older than it you can't play

COR_MSG = "That is correct!"  #message for correct answers
BAD_MSG = "Aw, better luck next time.\nThe correct answer was '"  #incorrect



Ques = ["Which Jeff created Amazon?",
        "Which Jeff played The Grandmaster?",
        "Which Jeffrey liked a lil' bit of murder?",
        "Who released the album 'Grace'?",
        "What is Jeff  Gorvette?",
        "Who voices Jeff Gorvette?",
        "The line 'My name is Jeff' is from which movie?",
        "Who played Iron Monger in the first Iron man movie?",
        "What band is Jeff Ament from?",
        "Where is the name 'Jeffrey' from?"]

Opt = [["Buckley", "Bezos", "Besoz", "Beckley"],
       ["Goldblum", "Golfer", "Geralds", "Graham"],
       ["Davids", "Davis", "Douglas", "Dahmer"],
       ["Jeff Bezos", "Jeff Bridges", "Jeff Buckley", "Jeff Bailey"],
       ["A car", "A person", "A table", "A truck"],
       ["Jeff Gregor", "Jeff Groudon", "Jeff Gordon", "Jeff Gregory"],
       ["21 Jump Street", "22 Jump Street", "23 Jump Street", "Scream"],
       ["Jeff Bridges", "Jeff Bezos", "Jeff Baker", "Jeff Bell"],
       ["Nirvana", "Pearl Jam", "Muse", "Foo Fighters"],
       ["France", "Britain", "Finland", "Germany"]]


Cor_ans = ["Bezos",
           "Goldblum",
           "Dahmer",
           "Jeff Buckley",
           "A car",
           "Jeff Gordon",
           "22 Jump Street",
           "Jeff Bridges",
           "Pearl Jam",
           "Germany"]


score = 0    #is the base score the user starts with

# Introduction- Age check + username input:
easygui.msgbox("""Hi, welcome to the Jeffrey Quiz! \nThis quiz will test you
               on your knowledge of Jeff-related questions""")
easygui.msgbox("""You will be asked a question, and given four choices to
answer with! \nDon't worry if it's incorrect, theres always
the next question!""")

age = easygui.integerbox("How old are you?")

if age <= MIN_AGE:
    easygui.msgbox("Sorry, you are too young for this game!")
    easygui.msgbox("Please come back when you are older :)")
    quit()

elif age >= MAX_AGE:
    easygui.msgbox("Sorry, you're too old for this game!\n...That must suck.")
    easygui.msgbox("See ya!")
    quit()

user = easygui.enterbox("Could you also tell me your name?")
while user == "":
    easygui.msgbox("You need to enter a username")
    user = easygui.enterbox("Please tell me your name")
    
easygui.msgbox("Awesome! Welcome to the quiz " + user + "!")
begin = easygui.ynbox("Shall we begin?")

if begin is False:
    easygui.msgbox("Ah, that's all good. See ya next time " + user + ".")
    quit()


# Questions + checking to see if correct (and award scores):
for x in range(QUESTIONS):
    answer = easygui.buttonbox(Ques[x], choices=Opt[x])

    if answer == Cor_ans[x]:
        easygui.msgbox(COR_MSG)
        score += 1

    elif answer != Cor_ans[x]:
        easygui.msgbox(BAD_MSG + Cor_ans[x] + "'.")


# The end of The Jeffrey Quiz (provides score):
easygui.msgbox("Well done on completing The Jeff Quiz!\nYour score is...")
easygui.msgbox(str(score) + " out of " + str(QUESTIONS) + "!")
easygui.msgbox("Please come back soon " + user + "!")
quit()
