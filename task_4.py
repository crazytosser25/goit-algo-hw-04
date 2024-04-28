import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    cmd = re.sub("[^A-Za-z]", "", cmd)
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid data. You must give me Name and Phone-number."
    name, phone = args
    if len(phone) not in [10,13]:
        return "Invalid Phone-number."
    if name in contacts:
        return "Invalid Name. This contact already exists"
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid data. You must give me Name and new Phone-number."
    name, phone = args
    if len(phone) not in [10,13]:
        return "Invalid Phone-number."
    contacts[name] = phone
    return "Contact added."

def show_phone():
    pass

def show_all():
    pass

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()