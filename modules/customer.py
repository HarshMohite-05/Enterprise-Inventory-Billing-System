# ==========================================
# Customer Module
# ==========================================

from modules.file_handler import read_csv, write_csv


# ==========================================
# Customer Menu
# ==========================================

def customer_menu():

    print("\n" + "=" * 50)
    print("         CUSTOMER MANAGEMENT")
    print("=" * 50)

    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Update Customer")
    print("5. Delete Customer")
    print("6. Back")

    print("=" * 50)


# ==========================================
# Add Customer
# ==========================================

def add_customer():

    customers = read_csv("customers.csv")

    customer_id = input("Enter Customer ID : ").strip()

    for customer in customers:

        if customer["Customer_ID"] == customer_id:
            print("\nCustomer ID already exists.")
            return

    name = input("Enter Customer Name : ").strip()
    phone = input("Enter Phone Number : ").strip()

    new_customer = {
        "Customer_ID": customer_id,
        "Name": name,
        "Phone": phone
    }

    customers.append(new_customer)

    fieldnames = [
        "Customer_ID",
        "Name",
        "Phone"
    ]

    write_csv("customers.csv", fieldnames, customers)

    print("\nCustomer Added Successfully.")


# ==========================================
# View Customers
# ==========================================

def view_customers():

    customers = read_csv("customers.csv")

    if len(customers) == 0:
        print("\nNo Customers Available.")
        return

    print("\n" + "=" * 60)

    print(
        f"{'Customer ID':<20}"
        f"{'Name':<20}"
        f"{'Phone':<20}"
    )

    print("=" * 60)

    for customer in customers:

        print(
            f"{customer['Customer_ID']:<20}"
            f"{customer['Name']:<20}"
            f"{customer['Phone']:<20}"
        )

    print("=" * 60)


# ==========================================
# Search Customer
# ==========================================

def search_customer():

    customers = read_csv("customers.csv")

    if len(customers) == 0:
        print("\nNo Customers Available.")
        return

    customer_id = input("Enter Customer ID : ").strip()

    for customer in customers:

        if customer["Customer_ID"] == customer_id:

            print("\nCustomer Found")
            print("=" * 40)

            print(f"Customer ID : {customer['Customer_ID']}")
            print(f"Name        : {customer['Name']}")
            print(f"Phone       : {customer['Phone']}")

            print("=" * 40)

            return

    print("\nCustomer Not Found.")


# ==========================================
# Update Customer
# ==========================================

def update_customer():

    customers = read_csv("customers.csv")

    if len(customers) == 0:
        print("\nNo Customers Available.")
        return

    customer_id = input("Enter Customer ID : ").strip()

    for customer in customers:

        if customer["Customer_ID"] == customer_id:

            print("\nCurrent Details")

            print(f"Name  : {customer['Name']}")
            print(f"Phone : {customer['Phone']}")

            print("\nEnter New Details")

            customer["Name"] = input("Name : ").strip()
            customer["Phone"] = input("Phone : ").strip()

            fieldnames = [
                "Customer_ID",
                "Name",
                "Phone"
            ]

            write_csv("customers.csv", fieldnames, customers)

            print("\nCustomer Updated Successfully.")
            return

    print("\nCustomer Not Found.")


# ==========================================
# Delete Customer
# ==========================================

def delete_customer():

    customers = read_csv("customers.csv")

    if len(customers) == 0:
        print("\nNo Customers Available.")
        return

    customer_id = input("Enter Customer ID : ").strip()

    for customer in customers:

        if customer["Customer_ID"] == customer_id:

            customers.remove(customer)

            fieldnames = [
                "Customer_ID",
                "Name",
                "Phone"
            ]

            write_csv("customers.csv", fieldnames, customers)

            print("\nCustomer Deleted Successfully.")
            return

    print("\nCustomer Not Found.")