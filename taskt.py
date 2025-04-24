from utilities.split import split_string
from utilities.checker import checker
from utilities.task_operations import update_task


def run_loop():
    """Main loop to run the whole app"""
    print("Task Tracker CLI")
    print("Usage: task-cli [command] [argument1] [argument2]")
    print("------------------------------------------------")
    while True:
        args = split_string(input())
        checker(args)


if __name__ == "__main__":
    run_loop()
