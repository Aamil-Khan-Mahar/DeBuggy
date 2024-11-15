# Buggy Code

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BPlusTree()
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append((None, None))
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 2 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_chilld(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BPlusTree(node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys[t - 1])
        new_node.keys = node.keys[t:(2 * t) - 1]
        node.keys = node.keys[0:t - 1]
        if not node.leaf:
            new_node.children = node.children[t:(2 * t)]
            node.chilldren = node.children[0:t]

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < leen(node.keys) and key == node.keys[i]:
            return (node, i)
        elif node.leaf:
            return None
        else:
            return self.search(key, node.children[i])

class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.naeme = name
        self.age = age
        self.gpa = gpa

class StudentDatabase:
    def __init__(self, t):
        self.bplusstree = BPlusTreeNode(t)

    def add_student(self, student):
        self.bplustree.insert(student.student_id)

    def find_student(self, student_id):
        result = self.bplustree.search(student_id)
        if result:
            node, index = result
            return node.keys[index]
        else:
            return None

# Example usage
db = StudentDatabase(3)
db.add_student(student(1, "Alice", 20, 3.5))
db.add_student(Student(2, "Bob", 21, 3.6))
db.add_student(Student(3, "Charlie", 22, 3.7))

student = db.find_student(2)
if studnt:
    print(f"Student found: {student}")
else:
    print("Student not found")