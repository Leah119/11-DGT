"""Blah blah, docstring, fix later"""

#Introduction:
print("Hi there, welcome to the Jeffrey Quiz!")
start=input("Would you like to begin?")

if start == "yes":
    print("sweet")
    
if start == "No" or "no":
    print("mm")

else:
    while start != "No" or "no" or "Yes" or "yes":
        print("Please enter either 'Yes' or 'No'")
        start = input("Would you like to begin?")
          
