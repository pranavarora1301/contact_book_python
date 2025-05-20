contacts = {}

while True:
    print('\nContact Book App')
    print("1. CREATE CONTACT")
    print("2. VIEW CONTACT")
    print("3. UPDATE CONTACT")
    print("4. DELETE CONTACT")
    print("5. SEARCH CONTACT")
    print("6. COUNT CONTACT")
    print("7. EXIT")

    choice = input("Enter your choice = ")

    if choice == '1' :
        name = input("Enter your name = ")
        if name in contacts :
            print(f"Contact name {name} already exists")

        else:
            age = input("Enter your age = ")
            email = input("Enter your email = ")
            mobile = input("Enter your Mobile number = ")
            contacts[name] = {'age':int(age), 'email': email, 'mobile' : int(mobile)}
            print(f"Contact name {name} has been created successfully.")

    elif choice == '2' :
        name = input("Enter contact name to view = ")
        if name in contacts :
            contact = contacts[name]
            print(f"'Name':{name} , 'age':{int(age)}, 'email': {email}, 'mobile' : {int(mobile)}")
        else:
            print("Contat not found!")

    elif choice == '3' :
        name = input("Enter name to update contact")
        if name in contacts:
            age = input("Enter updated age = ")
            email = input("Enter updated email = ")
            mobile = input("Enter updated Mobile number = ")
            contacts[name] = {'age':int(age), 'email': email, 'mobile' : int(mobile)}
            print(f"Contact name {name} updated successfully.")
        else:
            print("Contat not found!")

    elif choice == '4' :
        name = input("Enter the name to be deleted")
        if name in contacts :
            del contacts[name]
            print("Contact name {name} deleted successfully!")
        else:
            print("Contat not found!")

    elif choice == '5' :
        search_name = input("Enter Contact name to search = ")
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - 'Name':{name} , 'age':{int(age)}, 'email': {email}, 'mobile' : {int(mobile)}")
                found = True
        if not found : print("No contact found with that name!")

    elif choice == '6':
        print(f"Total contacts in your contact book : {len(contacts)}")

    elif choice == '7' :
        print("Goodbye!")
        break

    else :
        print("Invalid input!")
