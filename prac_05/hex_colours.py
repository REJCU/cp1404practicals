"""

"""

HEX_COLOUR = {"absolute zero": "#0048ba", "cerulean": "#007ba7", "egyptian blue": "#1034a6", "electric blue": "#7df9ff"
    , "ultramarine": "#3f00ff", "lightslateblue":"#8470ff", "lilac":"#c8a2c8", "little boy blue":"#6ca0dc", "macaroni and cheese":"#ffbd88", "sapphire":"#0f52ba"}

name_of_colour = input("Name: ").lower()
while name_of_colour != "":
    if name_of_colour in HEX_COLOUR:
        print(name_of_colour, "is", HEX_COLOUR[name_of_colour])
        name_of_colour = input("Name: ")
    else:
        print("Invalid Name")
        name_of_colour = input("Name: ")
