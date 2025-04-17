import task_operations as to
from checker import print_additional_args_msg


def add_handler(args):
    if len(args) < 2:
        print_additional_args_msg("add", "task_content")
        return
    to.add_task(args[1])


def delete_handler(args):
    if len(args) < 2:
        print_additional_args_msg("delete", "task_id")
        return
    if not args[1].isnumeric():
        print("You need to provide a numeric argument to add a task!")
        return
    to.delete_task(args[1])


def update_handler(args):
    if len(args) < 3:
        print_additional_args_msg("update", "task_id", "content")
        return
    if not args[1].isnumeric():
        print("You need to provide a valid task id!")
        return
    to.update_task(args[1], args[2])


def list_handler(args):
    to.list_tasks() if len(args) == 1 else to.list_tasks(args[1])


def mark_progress_handler(args):
    if len(args) < 2:
        print_additional_args_msg("mark-in-progress", "task_id")
        return
    if not args[1].isnumeric():
        print("You need to provide a valid task id!")
        return
    to.delete_task(args[1])


def mark_done_handler(args):
    if len(args) < 2:
        print_additional_args_msg("mark-done", "task_id")
        return
    if not args[1].isnumeric():
        print("You need to provide a valid task id!")
        return
    to.delete_task(args[1])


command_map = {
    "add": add_handler,
    "delete": delete_handler,
    "update": update_handler,
    "list": list_handler,
    "mark-in-progress": mark_progress_handler,
    "mark-done": mark_done_handler,
}


def checker(args):
    if args[0] != "task-cli":
        print("Invalid argument: ", args[0])
        return False
    if len(args) > 4:
        print("Too many arguments provided!")

    args = args[1:]
    cmd = args[0]
    handler = command_map.get(cmd)

    if handler:
        handler(args)
    else:
        print(f"Unknown command: {cmd}")
        return False
