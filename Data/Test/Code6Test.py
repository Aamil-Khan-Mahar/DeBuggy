import unittest
from Code6Correct.py import RelativeGrader  

class TestRelativeGrader(unittest.TestCase):
    def setUp(self):
        # Initial test data
        self.students = [
            {'name': 'Alice', 'grade': 85},
            {'name': 'Bob', 'grade': 92},
            {'name': 'Charlie', 'grade': 78},
            {'name': 'Diana', 'grade': 90}
        ]
        self.grader = RelativeGrader(self.students)

    def test_add_student(self):
        new_student = {'name': 'Eve', 'grade': 88}
        self.grader.add_student(new_student)
        self.assertIn(new_student, self.grader.students)

    def test_remove_student(self):
        self.grader.remove_student({'name': 'Charlie', 'grade': 78})
        self.assertNotIn({'name': 'Charlie', 'grade': 78}, self.grader.students)

    def test_get_student(self):
        student = self.grader.get_student('Alice')
        self.assertEqual(student, {'name': 'Alice', 'grade': 85})

    def test_update_grade(self):
        self.grader.update_grade('Alice', 95)
        self.assertEqual(self.grader.get_student('Alice')['grade'], 95)

    def test_average_grade(self):
        self.assertAlmostEqual(self.grader.average_grade(), 86.25)

    def test_highest_grade(self):
        self.assertEqual(self.grader.highest_grade(), {'name': 'Bob', 'grade': 92})

    def test_lowest_grade(self):
        self.assertEqual(self.grader.lowest_grade(), {'name': 'Charlie', 'grade': 78})

    def test_grade_distribution(self):
        distribution = self.grader.grade_distribution()
        expected_distribution = {85: 1, 92: 1, 78: 1, 90: 1}
        self.assertEqual(distribution, expected_distribution)

    def test_median_grade(self):
        self.assertEqual(self.grader.median_grade(), 87.5)

    def test_pass_fail(self):
        passing_grade = 80
        passed, failed = self.grader.pass_fail(passing_grade)
        self.assertEqual(len(passed), 3)
        self.assertEqual(len(failed), 1)

    def test_top_n_students(self):
        top_students = self.grader.top_n_students(2)
        self.assertEqual(top_students, [
            {'name': 'Bob', 'grade': 92},
            {'name': 'Diana', 'grade': 90}
        ])

    def test_bottom_n_students(self):
        bottom_students = self.grader.bottom_n_students(2)
        self.assertEqual(bottom_students, [
            {'name': 'Charlie', 'grade': 78},
            {'name': 'Alice', 'grade': 85}
        ])

    def test_grade_variance(self):
        self.assertAlmostEqual(self.grader.grade_variance(), 31.1875)

    def test_grade_standard_deviation(self):
        self.assertAlmostEqual(self.grader.grade_standard_deviation(), 5.5825, places=4)

    def test_detect_collisions(self):
        # Add duplicate students for testing
        self.grader.add_student({'name': 'Alice', 'grade': 90})
        self.grader.add_student({'name': 'Bob', 'grade': 85})
        collisions = self.grader.detect_collisions()
        self.assertEqual(collisions, ['Alice', 'Bob'])

if __name__ == '__main__':
    unittest.main()
