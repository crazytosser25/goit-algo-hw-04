from colorama import Fore, Back, Style
from pathlib import Path
import sys

def processing_arguments() -> str:
    """This function processes command line arguments and returns the given path to the folder.

    Returns:
        str: The provided path to the folder
    """
    try:
        argument = sys.argv[1]
        return argument
    
    except IndexError:
        print('No path to folder')


def parsing_attachments(path: str, counter=1) -> None:
    """This function recursively processes each directory and file in the given path.

    Args:
        path (str): The provided path to the folder.
        counter (int, optional): A counter used for printing arrows. Defaults to 1.
    """
    try:
        path_to_file = Path(path)
        for element in path_to_file.iterdir():
            if element.is_dir():
                print_line(element.name, 'folder', counter)
                parsing_attachments(element, counter+1)
            if element.is_file():
                print_line(element.name, 'file', counter)
        
    except FileNotFoundError:
        print('No such directory')


def print_line(name: str, title: str, counter: int) -> None:
    """This function prints the name, arrow, and title in a formatted way.

    Args:
        name (str): The name of either the folder or file.
        title (str): Either 'folder' or 'file'.
        counter (int): A counter used for printing arrows.
    """
    arrow = ('-' * (counter - 1)) + '>'

    if title == 'file':
        name = f'{Fore.GREEN}{name}'
    else:
        name = f'{Fore.YELLOW}{name}'
    
    print(name.ljust(25, ' ') + f'{Fore.WHITE}{arrow}' + f'{Fore.CYAN}{title}' + f'{Fore.WHITE}')


# Start of program
if __name__ == "__main__":
    path_to_dir = processing_arguments()
    if path_to_dir:
        parsing_attachments(path_to_dir)
