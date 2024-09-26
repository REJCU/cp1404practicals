"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(user_score(score))
    print(user_score(random.randint(1, 100)))

def user_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
            return "Excellent!"
    elif score >= 50:
            return "Passable"
    else:
            return "Bad"

main()