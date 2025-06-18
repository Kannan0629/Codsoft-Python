contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

# Function to search for a contact
def search_contact():
    keyword = input("🔍 Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n👤 Contact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print("❌ Contact not found.\n")

# Function to update a contact
def update_contact():
    name = input("✏️ Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Enter new details (leave blank to keep old value):")
            new_phone = input("New Phone: ") or contact['phone']
            new_email = input("New Email: ") or contact['email']
            new_address = input("New Address: ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("✅ Contact updated successfully!\n")
            return
    print("❌ Contact not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("🗑️ Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("✅ Contact deleted successfully!\n")
            return
    print("❌ Contact not found.\n")

# User Interface
def contact_book():
    while True:
        print("📱 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.\n")

# Start the program
contact_book()
