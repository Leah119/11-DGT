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

Choices = [["Buckley", "Bezos", "Besoz", "Beckley"],
           ["Goldblum", "Golfer", "Geralds", "Graham"],
           ["Davids", "Davis", "Douglas", "Dahmer"],
           ["Jeff Bezos", "Jeff Bridges", "Jeff Buckley", "Jeff Bailey"],
           ["a car", "A person", "a table", "a truck"],
           ["Jeff Gregor", "Jeff Groudon", "Jeff Gordon", "Jeff Gregory"],
           
           
        
        

ans=easygui.buttonbox("Which Jeff created Amazon?",
                      choices=["Buckley", "Bezos", "Besoz", "Beckley"])
