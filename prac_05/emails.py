"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    extract_name(user_email)
    while user_email != "":
        name = extract_name(user_email)
        prompt = input(f"Is your name {name} Y/N").upper()
        if prompt != "Y" and prompt != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Email: ")

    for user_email, name in email_to_name.items():
        print(f"{name}  ({user_email})")

def extract_name(user_email):
    first_name = user_email.split('@')[0]
    parts = first_name.split(',')
    name = " ".join(parts).title()
    return name

main()

