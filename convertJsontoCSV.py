import json
import csv

# Opening JSON file and loading the data
with open(r"C:\Users\Dhruv\Desktop\CsvFile\address.json", encoding='utf-8', errors='ignore') as json_file:
    data = json.load(json_file)

list1 = []
active = True

for phone_number, details in data.items():
    if len(phone_number) == 13 and 'Address' in details:
        e_address_parts = details['Address'].get('e_address', '').split(';')
        alt_number = details['Address'].get('alt_number', '')
        email = details['Address'].get('email', '')

        # Get individual parts of e_address
        Name = e_address_parts[0].strip() if e_address_parts else ''
        House = e_address_parts[1].strip() if len(e_address_parts) > 1 else ''
        Area = e_address_parts[2].strip() if len(e_address_parts) > 2 else ''
        LandMark = e_address_parts[3].strip() if len(e_address_parts) > 3 else ''
        City = e_address_parts[4].strip() if len(e_address_parts) > 4 else ''
        PinCode = e_address_parts[5].strip() if len(e_address_parts) > 5 else ''
        State = e_address_parts[6].strip() if len(e_address_parts) > 6 else ''

        if Name and House:  # Condition 1
            row = [phone_number, alt_number, Name, House, Area, LandMark, City, PinCode, State, email,active]  # Include 'phone_number'

            # Check if any field in the row is not empty
            if any(field for field in row):
                list1.append(row)

# now we will open a file for writing
data_file = open(r'C:\Users\Dhruv\Desktop\CsvFile\Address.csv', 'w', encoding='utf-8', newline='')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing headers to the CSV file
count = 0

# Writing headers of CSV file
header = ['phone_number', 'alt_number', 'name', 'house', 'area', 'landmark', 'town', 'zip_code', 'state', 'email','active']  # Include 'phone_number' in header
csv_writer.writerow(header)

# Writing data of CSV file
for emp in list1:
    csv_writer.writerow(emp)

data_file.close()
