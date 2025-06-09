import mysql.connector
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Step 1: Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',       # For example: 'localhost'
    user='root',       # Your MySQL username
    password='12345678',  # Your MySQL password
    database='community_conversation'  # Your MySQL database name
)

# Step 2: Create a cursor to interact with the database
cursor = connection.cursor()

# Step 3: Execute the SQL query
cursor.execute("SELECT s_no,de_date,email_id FROM login_information")  # Replace with your table name

# Step 4: Fetch all rows from the query result
rows = cursor.fetchall()

# Step 5: Convert rows to a pandas DataFrame
columns = [column[0] for column in cursor.description]  # Get column names from the query result
df = pd.DataFrame(rows, columns=columns)

# Step 6: Open a file dialog to choose where to save the CSV file
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file dialog to choose a location and filename
output_file_path = filedialog.asksaveasfilename(
    defaultextension=".csv",  # Default file extension
    filetypes=[("CSV files", "*.csv")],  # File type filter
    title="Save CSV File"
)

# Step 7: Check if a path was selected
if output_file_path:
    # Step 8: Export DataFrame to CSV at the chosen location
    df.to_csv(output_file_path, index=False)  # Save to the selected path
    print(f"Data has been successfully exported to {output_file_path}")
else:
    print("No file was selected. The export was canceled.")

# Step 9: Close the cursor and connection
cursor.close()
connection.close()
