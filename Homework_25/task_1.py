import json
import io


class Employee:
    def __init__(self, n, p, s):
        self.name = n
        self.position = p
        self.salary = s

    def info(self):
        return self.name, self.position, self.salary


class Department:
    def __init__(self, n, d, e):
        self.name = n
        self.description = d
        self.employee = e

    def average(self):
        employee_salary = []
        for i in range(len(self.employee)):
            employee_salary.append(self.employee[i][2])
        return sum(employee_salary)/len(employee_salary)

    def max(self):
        employee_max_salary = []
        for i in range(len(self.employee)):
            if max(employee_max_salary) < self.employee[i][2]:
                employee_max_salary.append(self.employee[i][2])
        return employee_max_salary

    def min(self):
        employee_min_salary = []
        for i in range(len(self.employee)):
            if min(employee_min_salary) > self.employee[i][2]:
                employee_min_salary.append(self.employee[i][2])
        return employee_min_salary


def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: file {filename} not found ")


def object_create():
    data_file = read_json_file("homework_1.json")





