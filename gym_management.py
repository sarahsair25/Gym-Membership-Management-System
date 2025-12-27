import csv
import os
import hashlib


class Member:
    def __init__(self, id, name, email, contact, city, plan_type, plan_price, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self.plan_type = plan_type
        self.plan_price = plan_price
        self.password_hash = password_hash


class Gym:
    FILE_NAME = "members.csv"
    member_list = []
    count = 1

    PLANS = {
        "monthly": 50,
        "yearly": 500
    }

    def __init__(self):
        self.load_members()

    # 🔐 Hash password
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_members(self):
        if not os.path.exists(self.FILE_NAME):
            return

        with open(self.FILE_NAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    member = Member(
                        int(row[0]),
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        float(row[6]),
                        row[7]
                    )
                    Gym.member_list.append(member)

        if Gym.member_list:
            Gym.count = Gym.member_list[-1].id + 1

    def save_member(self, member):
        with open(self.FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                member.id,
                member.name,
                member.email,
                member.contact,
                member.city,
                member.plan_type,
                member.plan_price,
                member.password_hash
            ])

    def choose_plan(self):
        print("\nChoose Membership Plan:")
        print("1. Monthly ($50)")
        print("2. Yearly ($500)")

        while True:
            choice = input("Enter choice (1 or 2): ")

            if choice == "1":
                return "Monthly", self.PLANS["monthly"]
            elif choice == "2":
                return "Yearly", self.PLANS["yearly"]
            else:
                print("Invalid choice. Try again.")

    def register_member(self):
        print("\n----- Gym Member Registration -----")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        contact = input("Enter Contact: ")
        city = input("Enter City: ")

        plan_type, plan_price = self.choose_plan()

        password = input("Enter Password: ")
        password_hash = self.hash_password(password)

        member = Member(
            Gym.count,
            name,
            email,
            contact,
            city,
            plan_type,
            plan_price,
            password_hash
        )

        Gym.member_list.append(member)
        self.save_member(member)
        Gym.count += 1

        print(f"\n✅ Member registered with {plan_type} plan (${plan_price}).")

    def login_member(self):
        print("\n----- Member Login -----")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        password_hash = self.hash_password(password)

        for member in Gym.member_list:
            if member.email == email and member.password_hash == password_hash:
                print(
                    f"\n✅ Welcome {member.name}!\n"
                    f"Plan: {member.plan_type}\n"
                    f"Fee Paid: ${member.plan_price}"
                )
                return

        print("\n❌ Invalid email or password.")

    def display_members(self):
        if not Gym.member_list:
            print("\nNo members found.")
            return

        print("\nID\tName\tEmail\tContact\tCity\tPlan\tPrice")
        for m in Gym.member_list:
            print(
                f"{m.id}\t{m.name}\t{m.email}\t{m.contact}\t"
                f"{m.city}\t{m.plan_type}\t${m.plan_price}"
            )

    def menu(self):
        while True:
            print("\n--- Gym Membership Management System ---")
            print("1. Register Member")
            print("2. Member Login")
            print("3. View All Members")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(choice)

            if choice == 1:
                self.register_member()
            elif choice == 2:
                self.login_member()
            elif choice == 3:
                self.display_members()
            elif choice == 4:
                print("Exiting system...")
                break
            else:
                print("Invalid choice.")


g = Gym()
g.menu()
