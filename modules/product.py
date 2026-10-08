# ==========================================
# Product Module
# ==========================================

from modules.file_handler import read_csv, write_csv


# ==========================================
# Product Menu
# ==========================================

def product_menu():

    print("\n" + "=" * 50)
    print("          PRODUCT MANAGEMENT")
    print("=" * 50)

    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Back")

    print("=" * 50)


# ==========================================
# Add Product
# ==========================================

def add_product():

    products = read_csv("products.csv")

    product_id = input("Enter Product ID : ").strip()

    # Check Duplicate Product ID
    for product in products:

        if product["Product_ID"] == product_id:

            print("\nProduct ID already exists.")
            return

    name = input("Enter Product Name : ").strip()

    category = input("Enter Category : ").strip()

    price = input("Enter Price : ").strip()

    stock = input("Enter Stock : ").strip()

    new_product = {

        "Product_ID": product_id,
        "Name": name,
        "Category": category,
        "Price": price,
        "Stock": stock
    }

    products.append(new_product)

    fieldnames = [
        "Product_ID",
        "Name",
        "Category",
        "Price",
        "Stock"
    ]

    write_csv("products.csv", fieldnames, products)

    print("\nProduct Added Successfully.")




# ==========================================
# View Products
# ==========================================

def view_products():

    products = read_csv("products.csv")

    if len(products) == 0:

        print("\nNo Products Available.")
        return

    print("\n" + "=" * 80)
    print(
        f"{'Product ID':<15}"
        f"{'Name':<20}"
        f"{'Category':<20}"
        f"{'Price':<12}"
        f"{'Stock':<10}"
    )
    print("=" * 80)

    for product in products:

        print(
            f"{product['Product_ID']:<15}"
            f"{product['Name']:<20}"
            f"{product['Category']:<20}"
            f"{product['Price']:<12}"
            f"{product['Stock']:<10}"
        )

    print("=" * 80)

# ==========================================
# Search Product
# ==========================================

def search_product():

    products = read_csv("products.csv")

    if len(products) == 0:
        print("\nNo Products Available.")
        return

    product_id = input("Enter Product ID : ").strip()

    for product in products:

        if product["Product_ID"] == product_id:

            print("\nProduct Found")
            print("=" * 50)

            print(f"Product ID : {product['Product_ID']}")
            print(f"Name       : {product['Name']}")
            print(f"Category   : {product['Category']}")
            print(f"Price      : {product['Price']}")
            print(f"Stock      : {product['Stock']}")

            print("=" * 50)

            return

    print("\nProduct Not Found.")


# ==========================================
# Update Product
# ==========================================

def update_product():

    products = read_csv("products.csv")

    if len(products) == 0:
        print("\nNo Products Available.")
        return

    product_id = input("Enter Product ID : ").strip()

    for product in products:

        if product["Product_ID"] == product_id:

            print("\nCurrent Product Details")

            print(f"Name     : {product['Name']}")
            print(f"Category : {product['Category']}")
            print(f"Price    : {product['Price']}")
            print(f"Stock    : {product['Stock']}")

            print("\nEnter New Details")

            product["Name"] = input("Name : ").strip()
            product["Category"] = input("Category : ").strip()
            product["Price"] = input("Price : ").strip()
            product["Stock"] = input("Stock : ").strip()

            fieldnames = [
                "Product_ID",
                "Name",
                "Category",
                "Price",
                "Stock"
            ]

            write_csv("products.csv", fieldnames, products)

            print("\nProduct Updated Successfully.")
            return

    print("\nProduct Not Found.")

# ==========================================
# Delete Product
# ==========================================

def delete_product():

    products = read_csv("products.csv")

    if len(products) == 0:
        print("\nNo Products Available.")
        return

    product_id = input("Enter Product ID : ").strip()

    for product in products:

        if product["Product_ID"] == product_id:

            products.remove(product)

            fieldnames = [
                "Product_ID",
                "Name",
                "Category",
                "Price",
                "Stock"
            ]

            write_csv("products.csv", fieldnames, products)

            print("\nProduct Deleted Successfully.")
            return

    print("\nProduct Not Found.")