import pandas as pd
from pathlib import Path

#Constants 
INVENTORY_DIR = Path("test files") # to be updated to NAS location for production
PRODUCTS_FILE = INVENTORY_DIR / "Products.xlsx" # Needs to be changed to what ever file name mum picked

def load_products_excel():
    pass