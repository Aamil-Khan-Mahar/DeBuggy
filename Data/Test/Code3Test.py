import unittest

class TestBPlusTree(unittest.TestCase):
    def test_insert_and_search(self):
        # Create a B+ Tree with degree t=3
        bptree = BPlusTree(3)

        # Insert keys into the B+ Tree
        keys = [10, 20, 5, 6, 15, 30, 25]
        for key in keys:
            bptree.insert(key)

        # Search for existing keys
        for key in keys:
            result = bptree.search(key)
            self.assertIsNotNone(result, f"Key {key} should exist in the tree.")
            self.assertEqual(result[0].keys[result[1]], key, f"Key {key} not found at expected position.")

        # Search for non-existing key
        self.assertIsNone(bptree.search(50), "Key 50 should not exist in the tree.")

class TestStudentDatabase(unittest.TestCase):
    def test_student_database(self):
        # Create a student database with degree t=3
        db = StudentDatabase(3)

        # Add students to the database
        students = [
            Student(1, "Alice", 20, 3.5),
            Student(2, "Bob", 21, 3.6),
            Student(3, "Charlie", 22, 3.7),
            Student(4, "Diana", 23, 3.8),
            Student(5, "Eve", 24, 3.9)
        ]
        for student in students:
            db.add_student(student)

        # Search for existing students by ID
        for student in students:
            result = db.find_student(student.student_id)
            self.assertIsNotNone(result, f"Student ID {student.student_id} should exist.")
            self.assertEqual(result, student.student_id, f"Student ID {student.student_id} not found correctly.")

        # Search for non-existing student
        self.assertIsNone(db.find_student(10), "Student ID 10 should not exist.")

if __name__ == "__main__":
    unittest.main()
