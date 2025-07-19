"""
generate_synthetic_sales.py

Generates synthetic sales data for Make My Design Inc. and saves it as CSV.
Author: Your Name
Date: YYYY-MM-DD
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# -------------------
# Configuration
# -------------------

np.random.seed(42)  # for reproducibility

OUTPUT_PATH = "../data/raw/sales_data.csv"
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2025, 7, 11)

PRODUCTS = [
    {
        "Service": "Foam Core Cutout",
        "Description": "2ft tall: Radha Cutout",
        "Rate": 35.00
    },
    {
        "Service": "Foam Core Cutout",
        "Description": "2ft tall: Krishna Cutout",
        "Rate": 35.00
    },
    {
        "Service": "Cardstock",
        "Description": "10in: Sea Cutouts",
        "Rate": 6.25
    },
    {
        "Service": "Foam Core Cutout",
        "Description": "1.5ft: Green coral grass",
        "Rate": 30.00
    },
    {
        "Service": "Foam Core Cutout",
        "Description": "1.5ft: Shell cutout",
        "Rate": 30.00
    }
]

# -------------------
# Generate Data
# -------------------

def generate_sales_data():
    date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='D')
    records = []

    for single_date in date_range:
        # 30% chance of sales on any given day
        if np.random.rand() < 0.3:
            num_orders = np.random.randint(1, 4)  # 1–3 orders that day
            for _ in range(num_orders):
                product = np.random.choice(PRODUCTS)
                qty = np.random.randint(1, 6)  # 1–5 units
                amount = round(qty * product["Rate"], 2)
                records.append({
                    "Date": single_date.strftime("%Y-%m-%d"),
                    "Service": product["Service"],
                    "Description": product["Description"],
                    "Qty": qty,
                    "Rate": product["Rate"],
                    "Amount": amount
                })

    df = pd.DataFrame(records)
    return df


def main():
    df = generate_sales_data()
    # Ensure output folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Generated {len(df)} rows of synthetic sales data.")
    print(f"📄 Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
