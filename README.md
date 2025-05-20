**Contact Book App**

A simple Python-based terminal application to manage your contacts. This app allows you to **create, view, update, delete, search, and count** contacts using a menu-driven interface.

---

**Features**

- Add new contacts with name, age, email, and phone number
- Search for contacts by name (partial match supported)
- Update existing contact information
- Delete contacts
- View individual contact details
- Count total number of contacts
- Exit anytime

---

**Technologies Used**

- Python 3
- Dictionary Data Structure
- Command-line Interface (CLI)

---

**Getting Started**

**Prerequisites**

Make sure Python 3 is installed on your machine.

```bash
python --version
---

**How to Run**
Clone the repository and run the script:

git clone https://github.com/yourusername/contact-book-app.git
cd contact-book-app
python contact.py
```
---

**Demo**

Contact Book App
1. CREATE CONTACT
2. VIEW CONTACT
3. UPDATE CONTACT
4. DELETE CONTACT
5. SEARCH CONTACT
6. COUNT CONTACT
7. EXIT
Enter your choice = 1
Enter your name = Alice
Enter your age = 25
Enter your email = alice@example.com
Enter your Mobile number = 9876543210
Contact name Alice has been created successfully.
---

**TODOs / Known Issues**
 Fix variable reuse bugs in view/search (currently uses global variables like age, email out of scope).

**Add persistence (save to file or database).**

**Add test cases and modularize code using functions/classes.**

**Contributing**
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
