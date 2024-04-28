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
    contacts[name] = phone
    return "Contact added."

def change_contact():
    pass

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
            case _:
                print("Invalid command.")

        # if command == "hello":
        #     print("How can I help you?")
        # elif command == "add":
        #     print(add_contact(args, contacts))
        # else:
        #     print("Invalid command.")


if __name__ == "__main__":
    main()