from classModel import Model
from classTask import Task, TaskStatus
import debug

t1 = Task()
t1.set_content("""Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum""")
t1.set_status(TaskStatus.DONE)
t1.id = 0

t2 = Task()
t2.set_content("""Just as with any string, anything between the starting and
 ending quotes becomes part of the string, so this example has a leading blank
 (as pointed out by @root45). This string will also contain both blanks and
 newlines.""")
t2.set_status(TaskStatus.DOING)
t2.id = 1

t3 = Task()
t3.set_content("""If you don't want a multiline string but just have a long
 single line string, you can use parentheses, just make sure you don't include
 commas between the string segments, then it will be a tuple.""")
t3.set_status(TaskStatus.TODO)
t3.id = 3

t4 = Task()
t4.set_content("""This section often ends up being an exceedingly long and
 detailed list of tasks that is tough to maintain, but even tougher for an
 employee to remember and apply in their day-to-day work.""")
t4.set_status(TaskStatus.TODO)
t4.id = 4

t5 = Task()
t5.set_content("""Interviews patients, measures vital signs and records
 information on patients' charts. Prepares treatment rooms for examination of
 patients. """)
t5.set_status(TaskStatus.DOING)
t5.id = 5

t6 = Task()
t6.set_content("""Calls pharmacies to refill prescriptions""")
t6.set_status(TaskStatus.DONE)
t6.id = 6

t7 = Task()
t7.set_content("""Meet David at 11:00""")
t7.set_status(TaskStatus.DONE)
t7.id = 7

t8 = Task()
t8.set_content("""Call to Mary till tomorrow""")
t8.set_status(TaskStatus.TODO)
t8.id = 10

m = Model()
m.add_task(t1)
m.add_task(t2)
m.add_task(t3)
m.add_task(t4)
m.add_task(t5)
m.add_task(t6)
m.add_task(t7)
m.add_task(t8)

m.settings['db_path'] = 'database.dat'
m.save_settings()  # it overwrites "settings.dat"
m.save_tasks()

debug.print_database('database.dat')
