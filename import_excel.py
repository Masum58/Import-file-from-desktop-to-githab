import pandas as pd
import os
from pathlib import Path

def import_excel_from_desktop():
    # Get the path to the desktop
    desktop_path = str(Path.home() / "Desktop")
    
    # List all Excel files on the desktop
    excel_files = [f for f in os.listdir(desktop_path) if f.endswith(('.xlsx', '.xls'))]
    
    if not excel_files:
        print("No Excel files found on the desktop.")
        return None
    
    print("Available Excel files on desktop:")
    for i, file in enumerate(excel_files, 1):
        print(f"{i}. {file}")
    
    # Ask user to select a file
    while True:
        try:
            choice = int(input("Enter the number of the file you want to import: "))
            if 1 <= choice <= len(excel_files):
                selected_file = excel_files[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Read the selected Excel file
    file_path = os.path.join(desktop_path, selected_file)
    try:
        df = pd.read_excel(file_path)
        print(f"\nSuccessfully imported {selected_file}")
        print(f"Shape of the dataframe: {df.shape}")
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

if __name__ == "__main__":
    df = import_excel_from_desktop()
    if df is not None:
        print("\nFirst few rows of the imported data:")
        print(df.head()) 