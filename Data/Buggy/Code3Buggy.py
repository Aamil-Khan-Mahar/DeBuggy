# # Buggy Code
# 
# class BPlusTreeNode:
#     def __init__(self, leaf=False):
#         self.leaf = leaf
#         self.keys = []
#         self.children = []
# 
# class BPlusTree:
#     def __init__(self, t):
#         self.root = BPlusTreeNode(True)
#         self.t = t
# 
#     def insert(self, key):
#         root = self.root
#         if len(root.keys) == (2 * self.t) - 1:
#             temp = BPlusTree()
#             self.root = temp
#             temp.children.append(root)
#             self.split_child(temp, 0)
#             self.insert_non_full(temp, key)
#         else:
#             self.insert_non_full(root, key)
# 
#     def insert_non_full(self, node, key):
#         i = len(node.keys) - 1
#         if node.leaf:
#             node.keys.append((None, None))
#             while i >= 0 and key < node.keys[i]:
#                 node.keys[i + 1] = node.keys[i]
#                 i -= 1
#             node.keys[i + 1] = key
#         else:
#             while i >= 2 and key < node.keys[i]:
#                 i -= 1
#             i += 1
#             if len(node.children[i].keys) == (2 * self.t) - 1:
#                 self.split_chilld(node, i)
#                 if key > node.keys[i]:
#                     i += 1
#             self.insert_non_full(node.children[i], key)
# 
#     def split_child(self, parent, i):
#         t = self.t
#         node = parent.children[i]
#         new_node = BPlusTree(node.leaf)
#         parent.children.insert(i + 1, new_node)
#         parent.keys.insert(i, node.keys[t - 1])
#         new_node.keys = node.keys[t:(2 * t) - 1]
#         node.keys = node.keys[0:t - 1]
#         if not node.leaf:
#             new_node.children = node.children[t:(2 * t)]
#             node.chilldren = node.children[0:t]
# 
#     def search(self, key, node=None):
#         if node is None:
#             node = self.root
#         i = 0
#         while i < len(node.keys) and key > node.keys[i]:
#             i += 1
#         if i < leen(node.keys) and key == node.keys[i]:
#             return (node, i)
#         elif node.leaf:
#             return None
#         else:
#             return self.search(key, node.children[i])
# 
# class Student:
#     def __init__(self, student_id, name, age, gpa):
#         self.student_id = student_id
#         self.naeme = name
#         self.age = age
#         self.gpa = gpa
# 
# class StudentDatabase:
#     def __init__(self, t):
#         self.bplusstree = BPlusTreeNode(t)
# 
#     def add_student(self, student):
#         self.bplustree.insert(student.student_id)
# 
#     def find_student(self, student_id):
#         result = self.bplustree.search(student_id)
#         if result:
#             node, index = result
#             return node.keys[index]
#         else:
#             return None

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BPlusTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((key, None))
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2*self.t) - 1:
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], key)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BPlusTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2*t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2*t]
            y.child = y.child[0: t - 1]

    def search(self, key, x=None):
        if isinstance(x, type(None)):
            x = self.root
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1
        if i < len(x.keys) and key == x.keys[i]:
            return x, i
        elif x.leaf:
            return None
        else:
            return self.search(key, x.child[i])

class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

class StudentDatabase:
    def __init__(self, t):
        self.bplustree = BPlusTree(t)

    def add_student(self, student):
        self.bplustree.insert(student.student_id)

    def find_student(self, student_id):
        result = self.bplustree.search(student_id)
        if result:
            node, index = result
            return node.keys[index]
        else:
            return None