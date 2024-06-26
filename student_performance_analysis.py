# -*- coding: utf-8 -*-
"""student performance analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11ZXFiXvZyjg8vT4TucQmpLURcTVQH4NH
"""

import random

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"{self.name}: {self.grades}"

class StudentPerformanceAnalysisSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def generate_student_records(self, num_students):
        for i in range(1, num_students + 1):
            student_name = f"Student{i}"
            grades = [random.randint(60, 100) for _ in range(5)]  # Generating random grades for 5 subjects
            student = Student(student_name, grades)
            self.add_student(student)

    def analyze_performance(self):
        all_grades = [grade for student in self.students for grade in student.grades]
        average_grade = sum(all_grades) / len(all_grades) if all_grades else 0
        highest_grade = max(all_grades) if all_grades else 0
        lowest_grade = min(all_grades) if all_grades else 0
        return average_grade, highest_grade, lowest_grade

    def print_student_records(self):
        for student in self.students:
            print(student)

    def print_performance_overview(self, average, highest, lowest):
        print("\nPerformance Overview:")
        print(f"Class Average: {average:.2f}")
        print(f"Highest Grade: {highest}")
        print(f"Lowest Grade: {lowest}")

    def run_analysis_system(self, num_students):
        self.generate_student_records(num_students)
        self.print_student_records()
        average, highest, lowest = self.analyze_performance()
        self.print_performance_overview(average, highest, lowest)

if __name__ == "__main__":
    analysis_system = StudentPerformanceAnalysisSystem()
    analysis_system.run_analysis_system(num_students=10)