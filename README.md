🏋️‍♂️ Gym Membership Management System (Python)

A menu-driven Gym Membership Management System built using Python and Object-Oriented Programming, featuring secure authentication, membership plans, and CSV-based persistent storage.

This project demonstrates real-world Python concepts such as file handling, password hashing, and modular class design.

✨ Features

✅ Member Registration
✅ Secure Login (SHA-256 Password Hashing)
✅ Monthly & Yearly Membership Plans
✅ Automatic Plan Pricing
✅ Persistent Data Storage using CSV
✅ Menu-Driven CLI Interface
✅ Object-Oriented Design

🧠 Concepts Used

Object-Oriented Programming (OOP)

File Handling (CSV)

Password Hashing (SHA-256)

Input Validation

Menu-Driven Application Design

🛠️ Tech Stack
Technology	Usage
Python	Core language
CSV	Data persistence
Hashlib	Password security
CLI	User interaction
📁 Project Structure
Gym-Membership-Management-System/
│
├── gym_management.py
├── members.csv
└── README.md

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/sarahsair25/Gym-Membership-Management-System.git


Navigate to the project folder:

cd Gym-Membership-Management-System


Run the program:

python gym_management.py

📊 Membership Plans
Plan Type	Price
Monthly	$50
Yearly	$500
🔐 Security Implementation

Passwords are never stored in plain text

SHA-256 hashing ensures secure authentication

Login compares hashed values only

📌 Sample CSV Format
id,name,email,contact,city,plan_type,plan_price,password_hash
1,John,john@gmail.com,9876543210,New York,Monthly,50,ef92b7...

🚀 Why This Project?

This project was built to:

Strengthen Python fundamentals

Practice real-world file handling

Understand secure authentication

Build portfolio-ready applications

👩‍💻 Author

Sarah Sair
Aspiring Python Developer
📍 United States

🌟 Future Enhancements

Membership renewal system

Admin dashboard

Plan expiration tracking

SQLite database integration

GUI version using Tkinter
