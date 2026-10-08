# ==========================================
# Enterprise Inventory & Billing System
# Main File
# ==========================================

from menu import show_main_menu

from modules.product import product_menu,add_product,view_products,search_product,update_product,delete_product
from modules.customer import customer_menu,add_customer, view_customers,search_customer,update_customer,delete_customer
from modules.supplier import supplier_menu,add_supplier,view_suppliers,search_supplier, update_supplier,delete_supplier
from modules.purchase import purchase_menu,purchase_stock,purchase_history
from modules.sales import sales_menu,create_invoice, sales_history
from modules.reports import reports_menu,total_products,low_stock,sales_report,purchase_report,inventory_summary
from modules.backup import backup_data

def main():

    while True:

        show_main_menu()

        choice = input("Enter Your Choice : ")

        if choice == "1":

                while True:

                    product_menu()

                    product_choice = input("Enter Your Choice : ")

                    if product_choice == "1":
                        add_product()

                    elif product_choice == "2":
                        view_products()

                    elif product_choice == "3":
                        search_product()

                    elif product_choice == "4":
                        update_product()

                    elif product_choice == "5":
                        delete_product()

                    elif product_choice == "6":
                        break

                    else:
                        print("\nInvalid Choice!")

        elif choice == "2":

            while True:

                customer_menu()

                customer_choice = input("Enter Your Choice : ")

                if customer_choice == "1":
                    add_customer()

                elif customer_choice == "2":
                    view_customers()

                elif customer_choice == "3":
                     search_customer()

                elif customer_choice == "4":
                    update_customer()

                elif customer_choice == "5":
                     delete_customer()

                elif customer_choice == "6":
                         break

                else:
                     print("\nInvalid Choice!")

        elif choice == "3":

            while True:

                supplier_menu()

                supplier_choice = input("Enter Your Choice : ")

                if supplier_choice == "1":
                    add_supplier()

                elif supplier_choice == "2":
                    view_suppliers()

                elif supplier_choice == "3":
                    search_supplier()

                elif supplier_choice == "4":
                    update_supplier()

                elif supplier_choice == "5":
                    delete_supplier()

                elif supplier_choice == "6":
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == "4":

            while True:

                purchase_menu()

                purchase_choice = input("Enter Your Choice : ")

                if purchase_choice == "1":
                    purchase_stock()

                elif purchase_choice == "2":
                    purchase_history()

                elif purchase_choice == "3":
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == "5":

            while True:

                sales_menu()

                sales_choice = input("Enter Your Choice : ")

                if sales_choice == "1":
                    create_invoice()

                elif sales_choice == "2":
                    sales_history()

                elif sales_choice == "3":
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == "6":

            while True:

                reports_menu()

                report_choice = input("Enter Your Choice : ")

                if report_choice == "1":
                    total_products()

                elif report_choice == "2":
                    low_stock()

                elif report_choice == "3":
                    sales_report()

                elif report_choice == "4":
                    purchase_report()

                elif report_choice == "5":
                    inventory_summary()

                elif report_choice == "6":
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == "7":
            backup_data()

        elif choice == "8":

            print("\nThank You For Using Enterprise Inventory & Billing System.")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()