import task_operations as to


def add_handler(i, args):
    if i + 1 >= len(args):
        print("You need to provide additional argument to add a task!")
        return
    to.add_task(args[i + 1])


def delete_handler(i, args):
    if i + 1 >= len(args):
        print("You need to provide task id as an argument to delete a task!")
        return
    if not args[i + 1].isnumeric():
        print("You need to provide a numeric argument to add a task!")
        return
    to.delete_task(args[i + 1])


def update_handler(i, args):
    if i + 2 >= len(args):
        print("You need to provide additional argument(s) to update a task!")
        return
    if not args[i + 1].isnumeric():
        print("First argument has to be a numeric value!")
        return
    to.update_task(args[i + 1], args[i + 2])
    
def list_handler(i, args):
    pass


command_map = {
    "add": add_handler,
    "delete": delete_handler,
    "update": update_handler,
    "list": list_handler,
}


def checker(args):
    if args[0] != "task-cli":
        print("Invalid argument: ", args[0])
        return False

    args = args[1:]
    i = 0
    while i < len(args):
        cmd = args[i]
        handler = command_map.get(cmd)

        if handler:
            handler(args, i)
            i += 2  # Skip the command and its argument
        else:
            print(f"Unknown command: {cmd}")
            return False
