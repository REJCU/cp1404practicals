import datetime

from project import Project

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects"
        "\n- (F)ilter projects\n- (A)dd new project\n- (U)pdate project\n- (Q)uit project")

def main():
    projects = []
    load_projects(projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} from projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")

    # for project in projects:
    #     print(project)


def load_projects(projects):
    in_file = open("projects.txt", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    in_file.close()


main()
