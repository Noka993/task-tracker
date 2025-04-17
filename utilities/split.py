def split_string(input: str):
    """
    Splits the input string into a list of arguments.

    This function will first check whether the input string has properly closed quotes.
    If not, it will print an error message and return False.
    
    If the input string does not contain any quotes, it will split the string into
    a list of arguments by spaces.

    If the input string contains quotes, it will split the string into a list of
    arguments by spaces, but will ignore spaces inside quotes.

    :param input: str
    :return: list or False
    """
    if input.count("'") % 2 == 1 or input.count("\"") % 2 == 1:
        print("Invalid expression! You have to close the quotes")
        return False
    
    input = input.strip().replace("'", "\"")
    if "\"" not in input:
        return input.split(' ')
    
    args = []
    quote_count = 0
    word = ''
        
    for letter in input:
        if letter == "\"":
            quote_count += 1
            if quote_count % 2 == 0:
                args.append(word)
                word = ''
        # Check whether we are currently processing a string argument with quotes
        elif letter == ' ' and quote_count % 2 == 0:
            args.append(word)
            word = ''
        else:
            word += letter
    return args