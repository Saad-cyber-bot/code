import pandas as pd
import tkinter as tk
from pandastable import Table

# Load the Excel file
df = pd.read_excel(r"C:\Users\logent\Desktop\XL\Nytt Microsoft Excel-regneark (2).xlsx", engine="openpyxl")

# Remove special characters from the 'DescriptionOriginal' column
df['DescriptionOriginal'] = df['DescriptionOriginal'].str.replace(r'[^A-Za-z0-9\s]', '', regex=True)

# Save the cleaned DataFrame back to the same Excel file
df.to_excel(r"C:\Users\logent\Desktop\XL\Nytt Microsoft Excel-regneark (2).xlsx", index=False, engine="openpyxl")


# Create an interactive GUI to display the DataFrame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Display the cleaned DataFrame in the GUI window
pt = Table(frame, dataframe=df)
pt.show()

# Start the Tkinter main loop to display the GUI
root.mainloop()
