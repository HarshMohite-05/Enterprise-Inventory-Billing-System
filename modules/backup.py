# ==========================================
# Backup Module
# ==========================================

import os
import shutil
from datetime import datetime


def backup_data():

    backup_folder = "backups"

    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)

    files = [

        "products.csv",
        "customers.csv",
        "suppliers.csv",
        "purchases.csv",
        "sales.csv"

    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for file in files:

        if os.path.exists(file):

            filename = file.replace(".csv", "")

            backup_file = (
                f"{backup_folder}/"
                f"{filename}_{timestamp}.csv"
            )

            shutil.copy(file, backup_file)

    print("\nBackup Created Successfully.")