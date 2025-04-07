"""Blah blah, docstring, fix later""" #actually do or this will be awkward

from time import sleep

Ques = ["Who created Amazon?",
        "Who played The Grandmaster?",
        "Which Jeffrey liked a lil' bit of murder?",
        "Who released the album 'Grace'?",
        "What is Jeff Gorvette?",
        "Who voices Jeff Gorvette?",
        "The line 'My name is Jeff' is from which movie?",
        "Who played Iron Monger in the first Iron man movie?",
        "How else can you spell 'Jeffrey'?",
        "Where is the name 'Jeffrey' from?"]

Cor_ans = [["Jeff Bezos", "Jeffrey Bezos", "Bezos"],
           ["Jeff Goldblum", "Jeffrey Goldblum", "Goldblum"],
           ["Jeffrey Dahmer", "Jeff Dahmer", "Dahmer"],
           ["Jeff Buckley", "Jeffrey Buckley", "Buckley"],
           ["A car", "car", "a car", "racecar", "a racecar"],
           ["Jeff Gordon", "Jeffrey Gordon", "Gordon"],
           ["22 Jump Street", "22 jump street"],
           ["Jeff Bridges", "Jeffrey Bridges", "Bridges"],
           ["Geoffrey", "Jeffry", "Jefferey", "Jefrie", "Geffrey"],
           ["Germany", "germany"]]


#Introduction:
print("Hi there, welcome to the Jeffrey Quiz!")
start=input("Would you like to begin?")

if start == "Yes" or start == "yes":
    print("sweet")

elif start == "No" or start == "no":
    print("Ah well, see you next time!")
    quit()

while start != "Yes" and start != "No" and start != "yes" and start != "no":
    print("Please enter either 'Yes' or 'No'")
    start = input("Would you like to begin?")

print("Let us begin!")
print("*Disclaimer, you will need capitals for names*")

questions = 10
level = 0
attempts = 0
score = 0

print (questions)
print(level)

for x in range (questions):
    ans=input(Ques[level])
    print(Cor_ans[level])
    if ans in Cor_ans[level]:
        print("Congrats, that is correct!")
        level += 1
        score += 1
    elif ans != Cor_ans[level]:
        print("Hello?")
        while attempts <= 1 and ans != Cor_ans[level]:
            print("Sorry, you got that wrong. You have " +
                  str(2-attempts) + " more attempts left.")
            ans=input(Ques[level])
            attempts += 1
            if attempts == 2 and ans != Cor_ans[level]:
                print("I'm sorry, you've run out of guesses.")
                print("The answer could have been any of these options: " +
                      str(Cor_ans[level]))
                attempts == 0
                level += 1
                
            elif attempts >=1 and ans == Cor_ans[level]:
                print("Congrats, you got that right!")
                print("That won't count towards your score though :(")
                attempts == 0
                level += 1
                
    
if score == questions:
    print("That's the end of The Jeff Quiz!")
    print("Let's check your score...")
    sleep(1.5)
    print("Wow, congratulations, you got " + str(score) + "/" +
          str(questions) + " correct!")
    print("Thanks a lot for playing!")
    quit()

else:
    print("That's the end of The Jeff Quiz!")
    print("Now, what did you score out of " + str(questions) + " ?")
    sleep(1.5)
    print("Aw man, you got " + str(score) + " out of " + str(questions) +
          "!")
    print("You should definetly play it again to get full marks!")
    print("Thanks for playing!")
    quit()

 
#add score element, so that we can print it at the end.
#also, remove square brackets (around answers when printed).



#Read through the ENTIRE code before saying you're done.
#Don't want to forget to change docstring,
#and get rid of testing elements before submitting.
