from utilities.split import split_string


def run_loop():
    """Main loop to run the whole app"""
    print("Task Tracker CLI \n")
    while True:
        args = split_string(input())
        if len(args) < 2 or len(args) > 4:
            print("Invalid number of arguments! Usage: task-cli [command] [argument]")
        print(args)
