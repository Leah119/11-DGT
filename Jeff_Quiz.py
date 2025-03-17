"""Blah blah, docstring, fix later"""

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


#Introduction:
print("Hi there, welcome to the Jeffrey Quiz!")
start=input("Would you like to begin?\n(Capitals matter)")

if start == "Yes" or start == "yes":
    print("sweet")
    
if start == "No" or start == "no":
    print("mm")

else:
    while start != "No":
        print("Please enter either 'Yes' or 'No'")
        start = input("Would you like to begin?")
          
