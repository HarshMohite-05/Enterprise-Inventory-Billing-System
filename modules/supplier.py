# ==========================================
# Supplier Module
# ==========================================

from modules.file_handler import read_csv, write_csv


# ==========================================
# Supplier Menu
# ==========================================

def supplier_menu():

    print("\n" + "=" * 50)
    print("         SUPPLIER MANAGEMENT")
    print("=" * 50)

    print("1. Add Supplier")
    print("2. View Suppliers")
    print("3. Search Supplier")
    print("4. Update Supplier")
    print("5. Delete Supplier")
    print("6. Back")

    print("=" * 50)


# ==========================================
# Add Supplier
# ==========================================

def add_supplier():

    suppliers = read_csv("suppliers.csv")

    supplier_id = input("Enter Supplier ID : ").strip()

    for supplier in suppliers:

        if supplier["Supplier_ID"] == supplier_id:
            print("\nSupplier ID already exists.")
            return

    name = input("Enter Supplier Name : ").strip()
    phone = input("Enter Phone Number : ").strip()

    new_supplier = {
        "Supplier_ID": supplier_id,
        "Name": name,
        "Phone": phone
    }

    suppliers.append(new_supplier)

    fieldnames = [
        "Supplier_ID",
        "Name",
        "Phone"
    ]

    write_csv("suppliers.csv", fieldnames, suppliers)

    print("\nSupplier Added Successfully.")


# ==========================================
# View Suppliers
# ==========================================

def view_suppliers():

    suppliers = read_csv("suppliers.csv")

    if len(suppliers) == 0:
        print("\nNo Suppliers Available.")
        return

    print("\n" + "=" * 60)

    print(
        f"{'Supplier ID':<20}"
        f"{'Name':<20}"
        f"{'Phone':<20}"
    )

    print("=" * 60)

    for supplier in suppliers:

        print(
            f"{supplier['Supplier_ID']:<20}"
            f"{supplier['Name']:<20}"
            f"{supplier['Phone']:<20}"
        )

    print("=" * 60)


# ==========================================
# Search Supplier
# ==========================================

def search_supplier():

    suppliers = read_csv("suppliers.csv")

    if len(suppliers) == 0:
        print("\nNo Suppliers Available.")
        return

    supplier_id = input("Enter Supplier ID : ").strip()

    for supplier in suppliers:

        if supplier["Supplier_ID"] == supplier_id:

            print("\nSupplier Found")
            print("=" * 40)

            print(f"Supplier ID : {supplier['Supplier_ID']}")
            print(f"Name        : {supplier['Name']}")
            print(f"Phone       : {supplier['Phone']}")

            print("=" * 40)

            return

    print("\nSupplier Not Found.")


# ==========================================
# Update Supplier
# ==========================================

def update_supplier():

    suppliers = read_csv("suppliers.csv")

    if len(suppliers) == 0:
        print("\nNo Suppliers Available.")
        return

    supplier_id = input("Enter Supplier ID : ").strip()

    for supplier in suppliers:

        if supplier["Supplier_ID"] == supplier_id:

            print("\nCurrent Details")

            print(f"Name  : {supplier['Name']}")
            print(f"Phone : {supplier['Phone']}")

            print("\nEnter New Details")

            supplier["Name"] = input("Name : ").strip()
            supplier["Phone"] = input("Phone : ").strip()

            fieldnames = [
                "Supplier_ID",
                "Name",
                "Phone"
            ]

            write_csv("suppliers.csv", fieldnames, suppliers)

            print("\nSupplier Updated Successfully.")
            return

    print("\nSupplier Not Found.")


# ==========================================
# Delete Supplier
# ==========================================

def delete_supplier():

    suppliers = read_csv("suppliers.csv")

    if len(suppliers) == 0:
        print("\nNo Suppliers Available.")
        return

    supplier_id = input("Enter Supplier ID : ").strip()

    for supplier in suppliers:

        if supplier["Supplier_ID"] == supplier_id:

            suppliers.remove(supplier)

            fieldnames = [
                "Supplier_ID",
                "Name",
                "Phone"
            ]

            write_csv("suppliers.csv", fieldnames, suppliers)

            print("\nSupplier Deleted Successfully.")
            return

    print("\nSupplier Not Found.")