import pandas as pd

# Load the spreadsheet
def extract_sales_data(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading spreadsheet: {e}")






'''# Test code

# Main program
def main():
    file_path = "Sample Sales Data- Interns task.xlsx"  # Replace with your file path
    obtained_data = extract_sales_data(file_path)
    print(obtained_data)
    

if __name__ == "__main__":
    main()'''
