import pandas as pd
from datetime import datetime

today = datetime.now().strftime("%d-%m-%Y")  # "15-11-2023"

def export_data(user_details):
    df = pd.DataFrame.from_dict(user_details, orient='index')

    if not df.empty:
        file_name = f"attendance_{today}.xlsx"
        df.to_excel(file_name, index=False)
        return f"Data exported successfully to {file_name}"
    else:
        return "No data to export."