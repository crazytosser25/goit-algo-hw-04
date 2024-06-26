'''Import module for working with json files, regular expressions,
colorful terminal output'''
import json
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def parse_input(user_input: str) -> tuple:
    """Split the user's input into command and arguments.
    The `parse_input` function takes a single argument, `user_input`,
    which is a string representing the user's input. This function
    splits the input into the command and its arguments. The command
    is converted to lowercase and any non-alphabetic characters are
    removed using regular expressions. The function then returns
    a tuple containing the command and its arguments.
    
    Args:
        user_input (str): User input string.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub("[^A-Za-z]", "", cmd)
    return cmd, *args

def read_file() -> dict:
    """Read and parse the contents of a JSON file containing contacts.
    The `read_file` function attempts to read the contents of a JSON file
    named "contacts.json". The function returns a dictionary representing
    the contacts with names as keys and phone numbers as values. If an
    exception occurs during the reading or parsing process, the function
    returns an empty dictionary.

    Returns:
        dict: A dictionary representing the contacts with names as keys and phone numbers as values.
    """
    try:
        with open("task_4/contacts.json", "r", encoding="utf-8") as contacts_json:
            contacts_string = contacts_json.read()
            contacts_dict = json.loads(contacts_string)
        return contacts_dict
    except Exception:
        return {}

def write_file(contacts_dict: dict) -> None:
    """Writes the given dictionary of contacts to a JSON file named "contacts.json".

    Args:
        contacts_dict (dict): A dictionary representing the contacts, with
        names as keys and phone numbers as values.
    """
    contacts_string = json.dumps(contacts_dict, indent=2)
    with open("task_4/contacts.json", "w", encoding="utf-8") as contacts_json:
        contacts_json.write(contacts_string)

def add_contact(args: tuple) -> str:
    """Adds a new contact to the contacts dictionary based on user input.

    Args:
        args (tuple): A tuple containing the name and phone number of the contact.

    Returns:
        str: A message indicating if the contact was added successfully or not.
    """
    if len(args) != 2:
        return mistaken_arg('invalid args')
    name, phone = args
    if len(phone) not in [10,13]:
        return mistaken_arg('invalid phone')
    contacts: dict = read_file()
    if name in contacts:
        return mistaken_arg('contact exists')
    contacts[name] = phone
    write_file(contacts)
    return "Contact added."

def change_contact(args: tuple) -> str:
    """Updates an existing contact in the contacts dictionary based on user input.

    Args:
        args (tuple): A tuple containing the name and new phone number of the contact.

    Returns:
        str: A message indicating if the contact was updated successfully or not.
    """
    if len(args) != 2:
        return mistaken_arg('invalid args')
    name, phone = args
    if len(phone) not in [10,13]:
        return mistaken_arg('invalid phone')
    contacts: dict = read_file()
    contacts[name] = phone
    write_file(contacts)
    return "Contact added."

def delete_contact(args: tuple) -> str:
    """Deletes the contact from file.

    Args:
        args (tuple): A tuple containing the name of the contact to delete.

    Returns:
        str: A message indicating if the contact was deleted successfully or not.
    """
    if len(args) != 1:
        return mistaken_arg('no name for search')
    name = args[0]
    contacts: dict = read_file()
    if name not in contacts:
        return mistaken_arg('phone not in contacts')
    contacts.pop(name)
    write_file(contacts)
    return "Contact deleted."

def show_phone(args: tuple) -> str:
    """Displays the phone number of a contact based on user input.

    Args:
        args (tuple): A tuple containing the name of the contact to search for.

    Returns:
        str: The phone number of the contact or an error message if the contact is not found.
    """
    if len(args) != 1:
        return mistaken_arg('no name for search')
    name = args[0]
    contacts: dict = read_file()
    if name not in contacts:
        return mistaken_arg('phone not in contacts')

    return phone_line(name, contacts[name])

def show_all(args: tuple) -> str:
    """Display all the contacts.

    Args:
        args (tuple): Ignored parameters.

    Returns:
        str: The formatted list of contacts.
    """
    contacts: dict = read_file()
    output_of_contacts: str = ''
    for name in contacts:
        output_of_contacts += phone_line(name, contacts[name])
    return output_of_contacts

def phone_line(name: str, phone: str) -> str:
    """Formats a contact's name and phone number into a displayable line.

    Args:
        name (str): The contact's name.
        phone (str): The contact's phone number.

    Returns:
        str: A formatted string containing the contact's name and phone number.
    """
    return f"{Fore.GREEN}{name.ljust(30, '.')}{Fore.CYAN}{phone}\n"

def mistaken_arg(mistake: str) -> str:
    """This function takes a single argument, `mistake` which is a string
    representing an error message. It returns a formatted string with colorful
    terminal output based on the given mistake. It uses the `Fore` class
    from the `colorama` module to add colors to the output string.
    The `autoreset=True` argument in `colorama.init(autoreset=True)` ensures
    that the color reset is applied automatically at the end of each line.

    Args:
        mistake (str): The error message to be displayed.

    Returns:
        str: A formatted string containing the error message in colorful terminal output.
    """
    match mistake:
        case 'invalid command':
            return f"{Fore.RED}Invalid command."
        case 'phone not in contacts':
            return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact doesn't exist."
        case 'contact exists':
            return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact already exists."
        case 'no name for search':
            return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must give me Name."
        case 'invalid phone':
            return f"{Fore.RED}Invalid Phone-number.\n{Fore.YELLOW}Must be 10 numbers, " \
                    "or 13 if in international format."
        case 'invalid args':
            return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must give me Name and Phone-number."

def command_list() -> str:
    """Returns the list of commands.

    Returns:
        str: string with all commands
    """
    return f"'close' or 'exit'\tto exit assistant.\n" \
            "'add [name] [phone]'\tto add new contact(phone must be 10 or 13 digits).\n" \
            "'change [name] [phone]'\tto change contact's phone number.\n" \
            "'del [name]'\t\tto delete contact from list.\n" \
            "'phone [name]'\t\tto review contact's phone number.\n" \
            "'all'\t\t\tto review all contacts.\n" 

def main():
    """This code is designed to create a simple command-line interface (CLI)
    application that interacts with a contacts database. The user can perform
    actions such as adding, changing, and viewing contact information. The CLI
    uses the `colorama` module to add colors to the output strings for better
    readability.
    """
    print(f"\n{Fore.YELLOW}Welcome to the assistant bot!\n(enter 'help' for list of commands)\n")
    while True:
        user_input = input(f"Enter a command: {Fore.BLUE}")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.YELLOW}Good bye!\n")
            break

        match command:
            case "hello":
                print(f"{Fore.YELLOW}How can I help you?\n")
            case "help":
                print(command_list())
            case "add":
                print(f"{Fore.YELLOW}{add_contact(args)}\n")
            case "change":
                print(f"{Fore.YELLOW}{change_contact(args)}\n")
            case "del":
                print(f"{delete_contact(args)}\n")
            case "phone":
                print(f"{show_phone(args)}\n")
            case "all":
                print(show_all(args))
            case _:
                print(f"{mistaken_arg('invalid command')}\n")


if __name__ == "__main__":
    main()
