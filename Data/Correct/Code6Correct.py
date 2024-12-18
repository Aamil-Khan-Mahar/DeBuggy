# Correct Code
# filename: Code6Correct.py

class RelativeGrader:
    def __init__(self, students):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student(self, name):
        for student in self.students:
            if student['name'] == name:
                return student
        return None

    def update_grade(self, name, grade):
        student = self.get_student(name)
        if student:
            student['grade'] = grade

    def average_grade(self):
        total = sum(student['grade'] for student in self.students)
        return total / len(self.students)

    def highest_grade(self):
        return max(self.students, key=lambda student: student['grade'])

    def lowest_grade(self):
        return min(self.students, key=lambda student: student['grade'])

    def grade_distribution(self):
        distribution = {}
        for student in self.students:
            grade = student['grade']
            if grade in distribution:
                distribution[grade] += 1
            else:
                distribution[grade] = 1
        return distribution

    def median_grade(self):
        grades = sorted(student['grade'] for student in self.students)
        n = len(grades)
        if n % 2 == 1:
            return grades[n // 2]
        else:
            return (grades[n // 2 - 1] + grades[n // 2]) / 2

    def pass_fail(self, passing_grade):
        passed = [student for student in self.students if student['grade'] >= passing_grade]
        failed = [student for student in self.students if student['grade'] < passing_grade]
        return passed, failed

    def top_n_students(self, n):
        return sorted(self.students, key=lambda student: student['grade'], reverse=True)[:n]

    def bottom_n_students(self, n):
        return sorted(self.students, key=lambda student: student['grade'])[:n]

    def grade_variance(self):
        avg = self.average_grade()
        variance = sum((student['grade'] - avg) ** 2 for student in self.students) / len(self.students)
        return variance

    def grade_standard_deviation(self):
        return self.grade_variance() ** 0.5

    def detect_collisions(self):
        seen = set()
        collisions = []
        for student in self.students:
            if student['name'] in seen:
                collisions.append(student['name'])
            else:
                seen.add(student['name'])
        return collisions