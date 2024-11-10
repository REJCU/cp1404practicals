import datetime

from project import Project


MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects"
        "\n- (F)ilter projects\n- (A)dd new project\n- (U)pdate project\n- (Q)uit project")


def main():
    projects = []
    get_projects(projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} from projects.txt")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(projects)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    save_input = input("Would you like to save to projects.txt? ").upper()
    if save_input == "Y":
        print("Saved")

    print("Thank you for using custom-built project management software.")

    # for project in projects:
    #     print(project)


def get_projects(projects):
    # loads information from a present file
    in_file = open("projects.txt", "r")
    in_file.readline()
    # ignores the first line full of irrelevant information
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    in_file.close()


    """ User submitted projects """
def load_projects(projects):
    project_file = input("Enter project file name: ")
    project_file = open(project_file, "r")
    project_file.readline()
    for line_of_project in project_file:
        parts_of_project = line_of_project.strip().split("\t")
        user_project = Project(parts_of_project[0],parts_of_project[1],parts_of_project[2],parts_of_project[3],parts_of_project[4])
        projects.append(user_project)
    project_file.close()


def save_projects(projects):
    example_project = open(input('w'))
    name = input("Name: ")
    while name != "":
        start_date = input("Start Date: ")
        priority = input("Priority: ")
        cost_estimate = input("Cost Estimate: ")
        completion_percentage = input("Completion Percentage: ")
        project_to_append = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project_to_append)
        name = input("Name: ")
    example_project.close()


def display_projects(projects):
    print("Uncompleted projects:")
    for project in projects:
        if not project.is_complete():
            # uses method made in the class to determine if task is completed
            print(f"{project.name}, Start date:{project.start_date}, priority {project.priority}, "
                  f"Estimate: {project.cost_estimate}, Completion: {project.completion_percentage}")
        elif project.is_complete():
            print(f"Completed Projects: \n{project.name}, Start date:{project.start_date}, priority {project.priority}, "
                f" Estimate: {project.cost_estimate}, Completion: {project.completion_percentage}")

def filter_by_date(projects):
    """ Filters project with inputted date using datetime method  """
    date_string = input("Show projects after the date (d/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    # converts user input to a date object
    date_string = date.strftime("%d/%m/%Y")
    # converts from date object to string to be usable with < operator

    for project in projects:
        if project.start_date < date_string:
            print(project)


main()
