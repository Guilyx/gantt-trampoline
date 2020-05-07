import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from lib.task import Task
from lib.task import TaskMaster
import random

def test_register():
    sched = TaskMaster()
    init_name = '_'
    n = 100
    t = []
    for i in range(n):
        init_name = init_name + '|'
        t.append(Task(init_name, [(i, 1)]))
        sched.registerTask(t[i])
    
    assert(sched.tasks_n == n)

def test_register_trick():
    sched = TaskMaster()
    init_name = '_'
    n = 100
    t = []
    for i in range(n):
        t.append(Task(init_name, [(i, 1)]))
        sched.registerTask(t[i])
    
    assert(sched.tasks_n == 1)

def test_removal():
    sched = TaskMaster()
    init_name = '_'
    n = 100
    t = []
    for i in range(n):
        t.append(Task(init_name, [(i, 1)]))
        sched.registerTask(t[i])

    l = 40
    for i in range(l):
        sched.deleteTask(random.choice(t))
    
    assert(sched.tasks_n == (n-l))