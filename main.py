import pandas as pd
from split import split_excel
from compare import cross_reference_excel
from sort import sort_excel
from rename import rename_excel
import os

# print("Change 'asset.display_ipv4_address' to 'IP Address' in vulnerabilities-verified.csv")
# wait = input("press y when ready")
# if wait == 'y':
#     print("ok")
cross_reference_excel(r'vulnerabilities-verified.csv', r'IT Asset Inventory.xlsx', 'IP Address')
rename_excel()
sort_excel()
split_excel()

# we can change the column name in the csv file to match the column name in the excel file

# df = pd.read_csv('vulnerabilities-verified.csv')    
# df.rename(columns={'asset.display_ipv4_address':'IP Address'}, inplace=True)
# df.to_csv('vulnerabilities-verified.csv', index=False)  

# print("Create a folder for the reports in this current folder called 'Reports'")
# print("Move the file to be parsed to this folder")
# print("Move the file to be compared to this folder")
# print("Which column do you want to parse the first file by?")
# #ip address
# print("Which column do you want to cross reference by?")
# #ip address. Both columns in the excel files must have the same name


# #compare.py
# #retrieve returned excel file from cross_reference_excel in compare.py


# print("What do you want to name the report?")
# #outputName= input()

