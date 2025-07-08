'''Take user input for a color.
Check if it's present in the list
'''

colors = ["red", "green", "blue"]

a = input("Enter Colour Name:")

if((a ==colors[0]) or (a ==colors[1]) or (a ==colors[2])):
    print("FOUND COLOUR")
else:
    print("COLOUR NOT FOUND")