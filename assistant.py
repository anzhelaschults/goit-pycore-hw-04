"""
Console assistant bot (CLI) — Task 4

All input() and print() calls are inside main() as required.
Command handling logic is implemented in separate functions that return strings.
Commands:
- hello
- add <username> <phone>
- change <username> <phone>
- phone <username>
- all
- close | exit
Unknown commands return "Invalid command."
"""
from typing import Tuple, Dict, List


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parse raw user input into a command and list of args.

    - Strips extra spaces.
    - Command is case-insensitive and returned in lowercase.
    - Returns (command, args_list)
    """
    cleaned = user_input.strip()
    if not cleaned:
        return "", []
    parts = cleaned.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Add or overwrite a contact. args expected: [username, phone]"""
    if len(args) < 2:
        return "Usage: add <username> <phone>"
    username = args[0]
    phone = args[1]
    contacts[username] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Change phone number for an existing contact. args expected: [username, phone]"""
    if len(args) < 2:
        return "Usage: change <username> <phone>"
    username = args[0]
    phone = args[1]
    if username not in contacts:
        return f"Error: contact {username} not found."
    contacts[username] = phone
    return "Contact updated."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Return phone number for a contact. args expected: [username]"""
    if len(args) < 1:
        return "Usage: phone <username>"
    username = args[0]
    if username not in contacts:
        return f"Error: contact {username} not found."
    return contacts[username]


def show_all(contacts: Dict[str, str]) -> str:
    """Return a formatted string of all contacts."""
    if not contacts:
        return "No contacts."
    lines = [f"{name}: {phone}" for name, phone in sorted(contacts.items())]
    return "\n".join(lines)


def main():
    contacts: Dict[str, str] = {}
    while True:
        user_input = input("> ")
        command, args = parse_input(user_input)

        if command in ("",):
            print("Invalid command.")
            continue

        if command == "hello":
            print("How can I help you?")
            continue

        if command == "add":
            result = add_contact(args, contacts)
            print(result)
            continue

        if command == "change":
            result = change_contact(args, contacts)
            print(result)
            continue

        if command == "phone":
            result = show_phone(args, contacts)
            print(result)
            continue

        if command == "all":
            result = show_all(contacts)
            print(result)
            continue

        if command in ("close", "exit"):
            print("Good bye!")
            break

        print("Invalid command.")


if __name__ == "__main__":
    main()
