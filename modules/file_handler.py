# ==========================================
# Enterprise Inventory & Billing System
# File Handler Module
# ==========================================

import csv
import json
import os


# ==========================================
# Read CSV File
# ==========================================

def read_csv(filename):

    data = []

    if not os.path.exists(filename):
        return data

    with open(filename, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


# ==========================================
# Write CSV File
# ==========================================

def write_csv(filename, fieldnames, data):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)


# ==========================================
# Read JSON File
# ==========================================

def read_json(filename):

    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as file:

        return json.load(file)


# ==========================================
# Write JSON File
# ==========================================

def write_json(filename, data):

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)