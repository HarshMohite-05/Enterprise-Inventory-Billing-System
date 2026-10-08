# ==========================================
# Sales Module
# ==========================================

from datetime import datetime

from modules.file_handler import read_csv, write_csv


# ==========================================
# Sales Menu
# ==========================================

def sales_menu():

    print("\n" + "=" * 50)
    print("           SALES MANAGEMENT")
    print("=" * 50)

    print("1. Create Invoice")
    print("2. Sales History")
    print("3. Back")

    print("=" * 50)


# ==========================================
# Create Invoice
# ==========================================

def create_invoice():

    customers = read_csv("customers.csv")
    products = read_csv("products.csv")
    sales = read_csv("sales.csv")

    if len(customers) == 0:
        print("\nNo Customers Available.")
        return

    if len(products) == 0:
        print("\nNo Products Available.")
        return

    invoice_id = f"I{len(sales)+1:03}"

    customer_id = input("Enter Customer ID : ").strip()

    customer_found = False

    for customer in customers:

        if customer["Customer_ID"] == customer_id:
            customer_found = True
            break

    if not customer_found:
        print("\nCustomer Not Found.")
        return

    product_id = input("Enter Product ID : ").strip()

    selected_product = None

    for product in products:

        if product["Product_ID"] == product_id:
            selected_product = product
            break

    if selected_product is None:
        print("\nProduct Not Found.")
        return

    quantity = int(input("Enter Quantity : "))

    stock = int(selected_product["Stock"])

    if quantity > stock:

        print("\nInsufficient Stock.")
        return

    selected_product["Stock"] = str(stock - quantity)

    price = float(selected_product["Price"])

    total = quantity * price

    sales.append({

        "Invoice_ID": invoice_id,
        "Customer_ID": customer_id,
        "Product_ID": product_id,
        "Quantity": quantity,
        "Total": total,
        "Date": datetime.now().strftime("%d-%m-%Y")

    })

    write_csv(

        "products.csv",

        ["Product_ID","Name","Category","Price","Stock"],

        products

    )

    write_csv(

        "sales.csv",

        [

            "Invoice_ID",
            "Customer_ID",
            "Product_ID",
            "Quantity",
            "Total",
            "Date"

        ],

        sales

    )

    print("\nInvoice Created Successfully.")

# ==========================================
# Sales History
# ==========================================

def sales_history():

    sales = read_csv("sales.csv")

    if len(sales) == 0:

        print("\nNo Sales History Available.")
        return

    print("\n" + "=" * 90)

    print(

        f"{'Invoice':<10}"
        f"{'Customer':<12}"
        f"{'Product':<12}"
        f"{'Qty':<10}"
        f"{'Total':<15}"
        f"{'Date':<15}"

    )

    print("=" * 90)

    for sale in sales:

        print(

            f"{sale['Invoice_ID']:<10}"
            f"{sale['Customer_ID']:<12}"
            f"{sale['Product_ID']:<12}"
            f"{sale['Quantity']:<10}"
            f"{sale['Total']:<15}"
            f"{sale['Date']:<15}"

        )

    print("=" * 90)