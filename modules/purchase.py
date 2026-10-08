# ==========================================
# Purchase Module
# ==========================================

from datetime import datetime

from modules.file_handler import read_csv, write_csv


# ==========================================
# Purchase Menu
# ==========================================

def purchase_menu():

    print("\n" + "=" * 50)
    print("         PURCHASE MANAGEMENT")
    print("=" * 50)

    print("1. Purchase Stock")
    print("2. Purchase History")
    print("3. Back")

    print("=" * 50)


# ==========================================
# Purchase Stock
# ==========================================

def purchase_stock():

    suppliers = read_csv("suppliers.csv")
    products = read_csv("products.csv")
    purchases = read_csv("purchases.csv")

    if len(suppliers) == 0:
        print("\nNo Suppliers Available.")
        return

    if len(products) == 0:
        print("\nNo Products Available.")
        return

    purchase_id = f"P{len(purchases)+1:03}"

    supplier_id = input("Enter Supplier ID : ").strip()

    supplier_found = False

    for supplier in suppliers:

        if supplier["Supplier_ID"] == supplier_id:
            supplier_found = True
            break

    if not supplier_found:
        print("\nSupplier Not Found.")
        return

    product_id = input("Enter Product ID : ").strip()

    product_found = None

    for product in products:

        if product["Product_ID"] == product_id:
            product_found = product
            break

    if product_found is None:
        print("\nProduct Not Found.")
        return

    quantity = int(input("Enter Quantity : "))

    product_found["Stock"] = str(
        int(product_found["Stock"]) + quantity
    )

    price = input("Enter Purchase Price : ")

    purchases.append({

        "Purchase_ID": purchase_id,
        "Product_ID": product_id,
        "Supplier_ID": supplier_id,
        "Quantity": quantity,
        "Price": price,
        "Date": datetime.now().strftime("%d-%m-%Y")
    })

    write_csv(
        "products.csv",
        ["Product_ID","Name","Category","Price","Stock"],
        products
    )

    write_csv(
        "purchases.csv",
        [
            "Purchase_ID",
            "Product_ID",
            "Supplier_ID",
            "Quantity",
            "Price",
            "Date"
        ],
        purchases
    )

    print("\nPurchase Recorded Successfully.")

# ==========================================
# Purchase History
# ==========================================

def purchase_history():

    purchases = read_csv("purchases.csv")

    if len(purchases) == 0:
        print("\nNo Purchase History Available.")
        return

    print("\n" + "=" * 90)

    print(
        f"{'ID':<10}"
        f"{'Product':<12}"
        f"{'Supplier':<12}"
        f"{'Qty':<10}"
        f"{'Price':<12}"
        f"{'Date':<15}"
    )

    print("=" * 90)

    for purchase in purchases:

        print(
            f"{purchase['Purchase_ID']:<10}"
            f"{purchase['Product_ID']:<12}"
            f"{purchase['Supplier_ID']:<12}"
            f"{purchase['Quantity']:<10}"
            f"{purchase['Price']:<12}"
            f"{purchase['Date']:<15}"
        )

    print("=" * 90)