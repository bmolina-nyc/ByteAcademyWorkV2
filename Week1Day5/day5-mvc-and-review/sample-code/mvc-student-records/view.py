def get_student():
    return input("Student Name: ")


def show_menu(student):
    print()
    print("Working on student {}".format(student))
    print()
    print("Options:")
    print("1 add grade")
    print("2 show gpa")
    print("3 quit")


def get_input():
    print()
    print("Your choice: ", end="")
    return input()


def get_grade():
    print()
    print("Input the grade: ", end="")
    return int(input())


def show_gpa(gpa):
    print()
    print("Student's gpa is {}.".format(gpa))
