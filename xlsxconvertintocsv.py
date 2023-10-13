import pandas as pd

#import pip install openpyxl
#import pip install pandas


# Read the Excel file
df = pd.read_excel(r'C:\Users\Dhruv\Desktop\CsvFile\New_PinCodes.xlsx')  # Replace with the actual Excel file name

# Save as CSV
df.to_csv(r'C:\Users\Dhruv\Desktop\NewCSV\New_Pincodes.csv', index=False)
