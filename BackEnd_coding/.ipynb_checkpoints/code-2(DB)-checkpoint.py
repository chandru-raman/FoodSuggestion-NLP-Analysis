import mysql.connector
import pandas as pd
import tkinter as tk
from tkinter import filedialog
connection = mysql.connector.connect(
    host='localhost',       
    user='root',      
    password='12345678', 
    database='community_conversation'  
)
cursor = connection.cursor()
cursor.execute("SELECT bmi_value,age FROM bmi_data")  
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description] 
df = pd.DataFrame(rows, columns=columns)
root = tk.Tk()
root.withdraw()  
output_file_path = filedialog.asksaveasfilename(
    defaultextension=".csv", 
    filetypes=[("CSV files", "*.csv")],  
    title="Save CSV File"
)
if output_file_path:
    df.to_csv(output_file_path, index=False) 
    print(f"Data has been successfully exported to {output_file_path}")
else:
    print("No file was selected. The export was canceled.")
cursor.close()
connection.close()
