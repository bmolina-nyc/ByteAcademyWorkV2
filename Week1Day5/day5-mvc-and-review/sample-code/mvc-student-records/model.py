import json
import os

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}


def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)


def save():
    with open(DATAPATH, "w") as file_object:
        json.dump(data, file_object, indent=2)


def get_grades(student):
    return data[student]['grades']


def add_student(student):
    data[student] = {"grades": []}


def add_grade(student, grade):
    data[student]["grades"].append(grade)


def get_gpa(student):
    grades = get_grades(student)
    return sum(grades) / len(grades)


def student_exists(student):
    if student in data:
        return True
    return False
