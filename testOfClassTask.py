import unittest
from classTask import Task, TaskStatus
import sys
import os


class TestClassTask(unittest.TestCase):

    def test_init(self):
        t = Task()
        self.assertEqual(t.id, 0)
        self.assertEqual(t.content, "")
        self.assertEqual(t.status, TaskStatus.TODO)

    def test_set_status(self):
        t = Task()
        t.status = TaskStatus.DOING
        self.assertEqual(t.status, TaskStatus.DOING)
        t.status = TaskStatus.TODO
        self.assertEqual(t.status, TaskStatus.TODO)
        t.status = TaskStatus.DONE
        self.assertEqual(t.status, TaskStatus.DONE)

    def test_get_status(self):
        t = Task()
        t.status = TaskStatus.DOING
        self.assertEqual(t.get_status(), TaskStatus.DOING)

    def test_set_content(self):
        t = Task()
        t.set_content("new content")
        self.assertEqual(t.content, "new content")

    def test_get_content(self):
        t = Task()
        t.content = "test 1 2 3"
        self.assertEqual(t.get_content(), "test 1 2 3")

    def test_eq(self):
        t1 = Task()
        t1.content = "content one"
        t1.status = TaskStatus.TODO
        t1.id = 5

        t2 = Task()
        t2.content = "content one"
        t2.status = TaskStatus.DOING
        t2.id = 7

        self.assertNotEqual(t1, t2)
        t2.id = 5
        self.assertEqual(t1, t2)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')  # it turns off all of print()
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
