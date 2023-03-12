import random
    
def test_no_collisions():
    #create a new schedule with random tasks
    schedule = Schedule()
    numTasks = random.randint(0,10)
    defaultTasks = schedule.generate_random_tasks(numTasks)
    schedule.place_tasks(defaultTasks)
    
    for default in numTasks
        assert default in schedule.tasks

    #generate a second set of tasks to place in the schedule
    addTasks = random.randint(0,10)
    new_tasks = schedule.generate_random_tasks(addTasks)

    #uses place_tasks to place new tasks
    schedule.place_tasks(new_tasks)

    #check that the new tasks have been placed in the schedule correctly
    for task in new_tasks:
        assert task in schedule.tasks

    #check that there are no time collisions between the tasks
    for task1 in schedule.tasks:
        for task2 in schedule.tasks:
            if task1 != task2:
                assert not task1.time_overlap(task2)


def generate_random_tasks(n):
    for i in range(n):
        #generate a task with a random start time and duration
        start_time = random.randint(0, 1440) #represent 24 hrs in minuts
        duration = random.randint(30, 120) #each task given time range of 30-120
        task = Task(start_time, duration)

        #add the task to the list of tasks
        self.tasks.append(task)

    return self.tasks