import json

def load_contacts_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts_to_file(contacts, file_path):
    with open(file_path, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone_number, email):
    contacts[name] = {'phone': phone_number, 'email': email}

def view_contacts(contacts):
    print("Contact List:")
    for name, info in contacts.items():
        print(f"{name}: {info['phone']}, {info['email']}")

def edit_contact(contacts, name, phone_number, email):
    if name in contacts:
        contacts[name] = {'phone': phone_number, 'email': email}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    file_path = "contacts.json"
    contacts = load_contacts_from_file(file_path)

    while True:
        print("\nContact Management System:")
        print("1. Add a new contact")
        print("2. View contact list")
        print("3. Edit an existing contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone_number, email)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            name = input("Enter the name of the contact to edit: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            edit_contact(contacts, name, phone_number, email)

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)

        elif choice == '5':
            save_contacts_to_file(contacts, file_path)
            print("Exiting. Contacts saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()