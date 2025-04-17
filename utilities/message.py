def print_additional_args_msg(cmd, *argv):
    """Prints a message to the user when they haven't provided enough arguments to run a command.

    :param cmd: The command that the user is trying to run.
    :param argv: The arguments that the user needs to provide to run the command.
    :return: None
    """
    print(f"You need to provide additional argument(s) to {cmd} a task!")
    args = ' '.join([ f"[{arg}]" for arg in argv])
    print(f"Usage: task-cli {args}")
    return