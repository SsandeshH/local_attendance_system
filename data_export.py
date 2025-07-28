import pandas as pd
from datetime import datetime
import os

today = datetime.now().strftime("%d-%m-%Y")  # e.g., "28-07-2025"

def export_data(user_details, filename):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame.from_dict(user_details, orient='index')

    if not df.empty:
        file_path = f"data/{filename}_{today}.xlsx"
        df.to_excel(file_path, index=False)
        return f"Data exported successfully to {file_path}"
    else:
        return "No data to export."
