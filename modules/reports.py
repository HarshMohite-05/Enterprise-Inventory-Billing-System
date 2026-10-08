# ==========================================
# Reports Module
# ==========================================

from modules.file_handler import read_csv


# ==========================================
# Reports Menu
# ==========================================

def reports_menu():

    print("\n" + "=" * 50)
    print("              REPORTS")
    print("=" * 50)

    print("1. Total Products")
    print("2. Low Stock Report")
    print("3. Sales Report")
    print("4. Purchase Report")
    print("5. Inventory Summary")
    print("6. Back")

    print("=" * 50)


# ==========================================
# Total Products
# ==========================================

def total_products():

    products = read_csv("products.csv")

    print(f"\nTotal Products : {len(products)}")


# ==========================================
# Low Stock Report
# ==========================================

def low_stock():

    products = read_csv("products.csv")

    print("\nLOW STOCK PRODUCTS")

    found = False

    for product in products:

        if int(product["Stock"]) <= 5:

            found = True

            print(
                f"{product['Product_ID']} - "
                f"{product['Name']} "
                f"(Stock : {product['Stock']})"
            )

    if not found:
        print("No Low Stock Products.")


# ==========================================
# Sales Report
# ==========================================

def sales_report():

    sales = read_csv("sales.csv")

    total_sales = 0

    for sale in sales:

        total_sales += float(sale["Total"])

    print(f"\nTotal Sales : ₹{total_sales:.2f}")


# ==========================================
# Purchase Report
# ==========================================

def purchase_report():

    purchases = read_csv("purchases.csv")

    total_purchase = 0

    for purchase in purchases:

        total_purchase += (
            float(purchase["Price"])
            * int(purchase["Quantity"])
        )

    print(f"\nTotal Purchase : ₹{total_purchase:.2f}")


# ==========================================
# Inventory Summary
# ==========================================

def inventory_summary():

    products = read_csv("products.csv")

    total_stock = 0

    for product in products:

        total_stock += int(product["Stock"])

    print("\nInventory Summary")

    print(f"Products : {len(products)}")

    print(f"Total Stock Units : {total_stock}")