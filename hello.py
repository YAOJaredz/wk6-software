def hello(name : str) -> None:
    """ This function will take a name and print Hello to the name.
    
    Args:
        name (str): The name appeared in the output.
    """

    print(f'Hello, {name}!')

def goodbye(name : str) -> None:
    """ This function will take a name and print Goodbye to the name.
    
    Args:
        name (str): The name appeared in the output.
    """

    print(f'Goodbye, {name}!')

if __name__ == '__main__':
    hello('Jared')
    goodbye('Jared')

