from scheduling import create_schedule

def test_create_schedule_with_priority():
    # Define tasks and their priorities, random task generation will be used later
    task = {
        "Gym": 2,
        "CS130 HW": 3,
        "CS180 HW": 1,
        "Reading": 4,
        "Study": 5
    }
    
    # Define available time
    available_time = "Monday 9:00-12:00"
    
    # Create schedule
    schedule = create_schedule(task, available_time)
    
    # Test that the task with lowest priority is not in the schedule
    expected_schedule = {
        "CS130": "Monday 9:00-10:00",
        "Reading": "Monday 10:00-11:00",
        "Study": "Monday 11:00-12:00"
    }
    assert schedule == expected_schedule
    assert "Gym" not in schedule.tasks()
    assert "CS180 HW" not in schedule.tasks()
