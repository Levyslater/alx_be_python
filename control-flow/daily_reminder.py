"""
This script will ask the user for a single task, its priority level, and if it is time-sensitive.
 The program will then provide a customized reminder for that task.
"""
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
is_time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if is_time_bound == "yes":
            print("Reminder:" + "'" + task + "'" + " is a high priority task that requires immediate \
            attention today!")
        else:
            print("Note: " + "'" + task + "'" + " is a high priority task but can be completed \
            when you have free time.")
    case "medium":
        if is_time_bound == "yes":
            print("Reminder:" + "'" + task + "'" + " is a medium priority task that requires immediate \
            attention today!")
        else:
            print("Note: " + "'" + task + "'" + " is a medium priority task. Consider completing \
            it when you have free time.")

    case "low":
        if is_time_bound == "yes":
            print("Reminder:" + "'" + task + "'" + " is a low priority task that requires immediate \
            attention today!")
        else:
            print("Note: " + "'" + task + "'" + " is a low priority task. Consider completing \
            it when you have free time.")

