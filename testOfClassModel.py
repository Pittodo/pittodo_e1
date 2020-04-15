import unittest
from classModel import Model
from classTask import Task, TaskStatus
import sys, os


class TestClassModel(unittest.TestCase):

    def test_init(self):
        m = Model()
        self.assertEqual(m.settings, {})
        self.assertEqual(m.tasks, [])

    def test_add_task(self):
        m = Model()
        t = Task()

        t.set_content("test content")
        t.set_status(TaskStatus.DONE)
        m.add_task(t)

        t.set_content("test content2")
        t.set_status(TaskStatus.DOING)
        m.add_task(t)

        gt2 = m.get_task(0)
        self.assertEqual(gt2.get_status(), TaskStatus.DONE)
        self.assertEqual(gt2.get_content(), "test content")

        gt = m.get_task(1)
        self.assertEqual(gt.get_status(), TaskStatus.DOING)
        self.assertEqual(gt.get_content(), "test content2")

    def test_del_task(self):
        m = Model()
        t = Task()

        t.set_content("test content")
        t.set_status(TaskStatus.DONE)
        m.add_task(t)

        t.set_content("test content2")
        t.set_status(TaskStatus.DOING)
        m.add_task(t)

        m.del_task(0)

        gt = m.get_task(0)
        self.assertEqual(gt.get_status(), TaskStatus.DOING)
        self.assertEqual(gt.get_content(), "test content2")

    def test_get_task(self):
        m = Model()

        t1 = Task()
        t1.set_content("test content")
        t1.set_status(TaskStatus.DONE)
        m.add_task(t1)

        t2 = Task()
        t2.set_content("test content2")
        t2.set_status(TaskStatus.DOING)
        m.add_task(t2)

        gt1 = m.get_task(0)
        gt2 = m.get_task(1)
        self.assertEqual(gt1, t1)
        self.assertEqual(gt2, t2)

    def test_get_last_task_id(self):
        m = Model()

        t = Task()
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)

        self.assertEqual(m.get_last_task_id(), 4)

    def test_save_load_tasks(self):
        m = Model()

        t = Task()
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)
        m.add_task(t)
        m.settings['db_path'] = "test_db.txt"

        m.save_tasks()
        m2 = Model()
        m2.settings['db_path'] = "test_db.txt"
        m2.load_tasks()
        self.assertEqual(m.tasks, m2.tasks)

    def test_save_load_settings(self):
        m = Model()
        m.settings['my_new_setting'] = "setting1"
        m.settings['db_path'] = "db.txt"
        m.save_settings()

        m2 = Model()
        m2.load_settings()
        self.assertEqual(m.settings, m2.settings)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')  # it turns off all of print()
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
