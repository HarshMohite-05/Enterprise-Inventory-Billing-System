# Enterprise Inventory & Billing System

A lightweight, modular, and terminal-based **Enterprise Inventory & Billing System** built with Python. Designed for retail and small-to-medium enterprise stores to manage inventory, track purchases, handle customer billing with automated GST calculation, and generate analytical business reports.

---

## Features

- **Product Management**:
  - Add, view, search, update, and delete products.
  - Automatic validation of product IDs (`P001`, `P002`, etc.), prices, and initial stock levels.
- **Customer Management**:
  - Maintain customer database with unique IDs (`C001`, `C002`, etc.) and validated contact numbers.
  - Search, update, and view customer records.
- **Supplier Management**:
  - Track supplier directory with validated IDs (`S001`, `S002`, etc.) and contact information.
- **Purchase Stock Management**:
  - Inward stock entry linked with suppliers and products.
  - Automatically updates product inventory upon receiving new stock.
  - Detailed purchase history logging.
- **Billing & Sales Management**:
  - Generate customer invoices with automated stock deduction.
  - Real-time tax calculation using configurable GST rates from `config.json`.
  - Comprehensive sales history ledger.
- **Reports & Analytics**:
  - Total product count.
  - Low-stock alert threshold (notifies when stock drops to $\le 5$ units).
  - Total sales and purchase revenue summaries.
  - Overall inventory unit summary.
- **Data Backup**:
  - Timestamped snapshot backups for all database CSV files saved into the `backups/` folder.
- **Zero External Dependencies**:
  - Runs natively on standard Python 3 with built-in modules (`csv`, `json`, `os`, `shutil`, `datetime`, `re`).

---

## Project Structure

```text
Enterprise_Inventory_Billing_System/
├── main.py                 # Application entry point & main event loop
├── menu.py                 # Console menu interface rendering
├── config.json             # Shop configuration (name, currency, GST %, version)
├── test.py                 # Configuration test script
├── products.csv            # Product inventory database
├── customers.csv           # Customer directory
├── suppliers.csv           # Supplier directory
├── purchases.csv           # Inward stock purchase records
├── sales.csv               # Outward billing & invoice sales records
├── backups/                # Directory containing timestamped CSV backups
└── modules/
    ├── __init__.py         # Package initializer
    ├── product.py          # Product CRUD operations
    ├── customer.py         # Customer CRUD operations
    ├── supplier.py         # Supplier CRUD operations
    ├── purchase.py         # Stock purchase & inventory update logic
    ├── sales.py            # Invoice generation, GST, & sales ledger
    ├── reports.py          # Inventory, low-stock, & financial reports
    ├── backup.py           # Automated CSV backup creator
    ├── file_handler.py     # Generic CSV & JSON I/O utilities
    └── validator.py        # Input formats & regex validators
```

---

## Prerequisites

- **Python 3.8+** (No third-party packages required).

---

## Installation & Setup

1. **Clone or Navigate to the Repository**:
   ```bash
   cd Enterprise_Inventory_Billing_System
   ```

2. **Verify Configuration**:
   Check or modify [config.json](config.json) to customize your store settings:
   ```json
   {
       "shop_name": "Enterprise Store",
       "currency": "INR",
       "gst": 18,
       "version": "1.0"
   }
   ```

3. **Run the Application**:
   ```bash
   python3 main.py
   ```

---

## Usage Guide

Upon launching `python3 main.py`, select an option from the main interactive menu:

```text
============================================================
      ENTERPRISE INVENTORY & BILLING SYSTEM
============================================================
1. Product Management
2. Customer Management
3. Supplier Management
4. Purchase Management
5. Sales Management
6. Reports
7. Backup Data
8. Exit
============================================================
```

### ID Validation Formats
- **Products**: `P###` (e.g., `P001`, `P002`)
- **Customers**: `C###` (e.g., `C001`, `C002`)
- **Suppliers**: `S###` (e.g., `S001`, `S002`)
- **Phone Numbers**: 10 digits starting with 6, 7, 8, or 9 (Indian mobile format).

### Creating Invoices
When generating a sales invoice (Option 5 $\rightarrow$ 1):
1. Enter Customer ID and Product ID.
2. Enter purchase quantity (must be $\le$ current stock).
3. The invoice automatically calculates:
   - Subtotal = $\text{Price} \times \text{Quantity}$
   - GST Amount = $\text{Subtotal} \times \frac{\text{GST \%}}{100}$
   - Total Amount = $\text{Subtotal} + \text{GST Amount}$
4. Stock is immediately deducted from [products.csv](products.csv) and the invoice entry is appended to [sales.csv](sales.csv).

### Backing Up Data
Select Option 7 to create timestamped copies of all `.csv` databases under the `backups/` directory (e.g., `backups/products_20261008_151000.csv`).

---

## License

This project is licensed under the MIT License - feel free to adapt and expand for your business needs.
