# ==========================================
# Validator Module
# ==========================================

import re


# ----------------------------
# Empty Check
# ----------------------------

def is_not_empty(value):

    return value.strip() != ""


# ----------------------------
# Integer Check
# ----------------------------

def is_positive_integer(value):

    return value.isdigit() and int(value) > 0


# ----------------------------
# Float Check
# ----------------------------

def is_positive_float(value):

    try:
        return float(value) > 0
    except ValueError:
        return False


# ----------------------------
# Phone Number Validation
# ----------------------------

def is_valid_phone(phone):

    pattern = r"^[6-9]\d{9}$"

    return re.match(pattern, phone) is not None


# ----------------------------
# Product ID Validation
# ----------------------------

def is_valid_product_id(product_id):

    pattern = r"^P\d{3}$"

    return re.match(pattern, product_id) is not None


# ----------------------------
# Customer ID Validation
# ----------------------------

def is_valid_customer_id(customer_id):

    pattern = r"^C\d{3}$"

    return re.match(pattern, customer_id) is not None


# ----------------------------
# Supplier ID Validation
# ----------------------------

def is_valid_supplier_id(supplier_id):

    pattern = r"^S\d{3}$"

    return re.match(pattern, supplier_id) is not None