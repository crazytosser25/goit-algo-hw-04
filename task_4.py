import json
import re
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub("[^A-Za-z]", "", cmd)
    return cmd, *args

def read_file():
    try:
        with open("task_4/contacts.json", "r") as contacts_json:
            contacts_string = contacts_json.read()
            contacts_dict = json.loads(contacts_string)
        return contacts_dict
    except Exception:
        return {}

def write_file(contacts_dict):
    contacts_string = json.dumps(contacts_dict, indent=2)
    with open("task_4/contacts.json", "w") as contacts_json:
        contacts_json.write(contacts_string)

def add_contact(args):
    if len(args) != 2:
        return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must give me Name and Phone-number.\n"
    name, phone = args
    if len(phone) not in [10,13]:
        return f"{Fore.RED}Invalid Phone-number.\n{Fore.YELLOW}Must be 10 numbers, or 13 if in international standart.\n"
    contacts = read_file()
    if name in contacts:
        return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact already exists.\n"
    contacts[name] = phone
    write_file(contacts)
    return f"{Fore.YELLOW}Contact added."

def change_contact(args):
    if len(args) != 2:
        return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must give me Name and new Phone-number.\n"
    name, phone = args
    if len(phone) not in [10,13]:
        return f"{Fore.RED}Invalid Phone-number.\n{Fore.YELLOW}Must be 10 numbers, or 13 if in international standart.\n"
    contacts = read_file()
    contacts[name] = phone
    write_file(contacts)
    return f"{Fore.YELLOW}Contact added."

def show_phone(args):
    if len(args) != 1:
        return f"{Fore.RED}Invalid data.\n{Fore.YELLOW}You must give me Name.\n"
    name = args[0]
    contacts = read_file()
    if name not in contacts:
        return f"{Fore.RED}Invalid Name.\n{Fore.YELLOW}This contact doesn't exist.\n"
    
    return contacts[name]

def show_all(args):
    args = None
    contacts = read_file()
    output_of_contacts = ''
    for name in contacts:
        output_of_contacts += (f"{name.ljust(30, '.')}{contacts[name]}\n")
    return output_of_contacts

def mistaken_arg(mistake):
    match mistake:
        case 'invalid command':
            return f"{Fore.RED}Invalid command.\n"

def main():
    
    print(f"\n{Fore.YELLOW}Welcome to the assistant bot!\n")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.YELLOW}Good bye!\n")
            break

        match command:
            case "hello":
                print(f"{Fore.YELLOW}How can I help you?\n")
            case "add":
                print(f"{add_contact(args)}\n")
            case "change":
                print(f"{change_contact(args)}\n")
            case "phone":
                print(f"{show_phone(args)}\n")
            case "all":
                print(f"{show_all(args)}")
            case _:
                print(mistaken_arg('invalid command'))


if __name__ == "__main__":
    main()