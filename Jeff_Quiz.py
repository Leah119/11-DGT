"""A short quiz that tests people on their knowledge of famous Jeffreys.

It also includes a few other Jeff-related questions.

For each correct answer they get one point added to their score, which is

then read out at the end of the quiz.

It is designed so that people 10 and under can not play.
"""

import easygui

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

questions = 10
score = 0
# Introduction:
easygui.msgbox("Hi, welcome the Jeffrey Quiz!")
age = easygui.integerbox("How old are you?")

if age <= 10:
    easygui.msgbox("Sorry, you are too young for this game!")
    easygui.msgbox("Please come back when you are older :)")
    quit()

user = easygui.enterbox("Could you also tell me your name?")
easygui.msgbox("Awesome! Welcome to the quiz " + user + "!")
begin = easygui.ynbox("Shall we begin?")

if begin is False:
    easygui.msgbox("Ah, that's all good. See ya next time " + user + ".")
    quit()


# Questions:
for x in range(questions):
    answer = easygui.buttonbox(Ques[x], choices=Opt[x])

    if answer == Cor_ans[x]:
        easygui.msgbox("That is correct!")
        score += 1

    elif answer != Cor_ans[x]:
        easygui.msgbox("Aw, better luck next time.")


# The end of The Jeffrey Quiz:
easygui.msgbox("Well done on completing The Jeff Quiz!")
easygui.msgbox("Your score is...")
easygui.msgbox(str(score) + " out of 10!")
easygui.msgbox("Please come back soon " + user + "!")
quit()
