""" Password check """

MINIMUM_LENGTH = 4

def main():
        password = get_password()
        print_password(password)


def print_password(password):
        print("*" * len(password))


def get_password():
        password = input(f"Enter password to the length of {MINIMUM_LENGTH}: ")
        while len(password) < MINIMUM_LENGTH:
                password = input(f"Enter password to the length of {MINIMUM_LENGTH}")
        return password



main()
