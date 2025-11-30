# library_inventory_manager_Assignment-3-python
A Python-based Library Inventory Management System using OOP, JSON file handling, and a menu-driven CLI interface.

📚 Library Inventory Manager

A Python-based Library Inventory Management System using OOP, JSON file handling, and a menu-driven CLI interface.

📌 Project Overview

This project is a simple yet powerful Library Inventory Management System that allows users to:

Add new books

View all available books

Search books by Title

Search books by ISBN

Issue books

Return books

Store all data permanently using a JSON file

The system is built using Python, Object-Oriented Programming, and a menu-driven CLI.

🗂 Project Structure
library-inventory-manager-shahjad/
│
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   └── inventory.py
│
├── cli/
│   └── main.py
│
├── books.json
├── README.md
├── requirements.txt
└── .gitignore

🧠 Concepts Used

Python OOP (Classes & Objects)

File Handling (JSON)

Modular Project Structure

CLI-based User Interaction

Data Persistence

Package Imports

▶️ How to Run the Project

Make sure you are inside the project root folder, then run:

python -m cli.main


Important:
Do NOT run main.py directly. Always use module mode:

python -m cli.main

📌 Features
✔ Add Book

Add new books with Title, Author, and ISBN.

✔ View All Books

Displays a complete list of all books.

✔ Search by Title

Find any book using its exact title.

✔ Search by ISBN

Quick lookup using ISBN number.

✔ Issue Book

Marks a book as “issued” if available.

✔ Return Book

Restores book status to “available”.

✔ Auto-Save System

Every change is saved automatically in books.json.

📝 Sample books.json (auto-generated)
[
    {
        "title": "Python Basics",
        "author": "Md Shahjad",
        "isbn": "101",
        "status": "available"
    }
]

🙌 Developed By

Md Shahjad

Library Inventory Manager — Python Mini Project
