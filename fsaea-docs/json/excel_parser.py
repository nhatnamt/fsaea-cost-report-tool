import json
import os

import numpy as np
import pandas as pd

file_path = os.path.join(os.getcwd(), 'fsaea-docs', 'BOM Catalog.xlsx')

# Load the Excel file
excel_file = pd.ExcelFile(file_path)
# Get the sheet names
sheet_names = excel_file.sheet_names[1:]  # skip first page

# Iterate over each sheet
for sheet_name in sheet_names:
    # Load the sheet into a DataFrame
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    # Drop the first column
    sheet = sheet.iloc[:, 1:]
    # Replace NaN values with null
    sheet = sheet.where(pd.notnull(sheet), "None")

    # Specify the output JSON file path

    json_file = 'server/db/catalog/' + f'{sheet_name.lower()}.json'
    # List to store JSON objects
    json_objects = []

    # Loop through each row of the DataFrame
    for _, row in sheet.iterrows():

        row_dict = row.to_dict()
        formatted_dict = {key.replace('[', '').replace(']', ''): value for key, value in row_dict.items()}

        # remove [] in key, remove none with null and remove needs calc
        for key, value in formatted_dict.items():
            if isinstance(value, str):
                formatted_dict[key] = str(value).replace('[', '').replace(']', '')
            # camel case all keys
            formatted_dict[key.replace(' ', '')] = formatted_dict.pop(key)
            if value == "Yes" or value == "No":
                formatted_dict[key] = value == "Yes"
            if value == 'None':
                formatted_dict[key] = None
            if key == 'Formula':
                if formatted_dict[key] == None:
                    formatted_dict[key] = formatted_dict['Cost']
                else:
                    formatted_dict[key] = formatted_dict[key].replace('^', '**').replace('=', '')

        # Delete cost if has formula
        if 'Formula' in formatted_dict:
            del formatted_dict['Cost']

        json_objects.append(formatted_dict)

    # Write JSON objects to a JSON file
    with open(json_file, 'w') as json_file:
        json.dump(json_objects, json_file, indent=4)

    print("JSON file has been created successfully.")
