contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found")
        else:
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

    elif choice == "3":
        search_name = input("Enter name to search: ")

        for contact in contacts:
            if contact["name"] == search_name:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Contact found successfully!")

    elif choice == "4":
        update_name = input("Enter name to update: ")

        for contact in contacts:
            if contact["name"] == update_name:
                new_phone = input("Enter new phone number: ")
                contact["phone"] = new_phone
                print("Contact updated successfully!")

    elif choice == "5":
        delete_name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid choice")