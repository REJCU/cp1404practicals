"""  """


menu = """
    (G)et score
    (P)rint result
    (S)how stars
    (Q)uit"""



def main():
    score = 0
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid Option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Score: "))
    return score



def print_result(score):
    while score < 0 or score > 100:
        print("Invalid score")
    if  score >= 90:
        print("Excellent!")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    print("*" * score)


main()

