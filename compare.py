import pandas as pd

#Compares vulnerbailities-verified.csv to IT Asset Inventory.xlsx
#Makes matched.xlsx with the matched data

# change the column name asset.display_ipv4 in the csv file to 'IP Address' so it 
# can match the column name in the excel file

def cross_reference_excel(f1, f2, search):
    # Read the Excel files
    df1 = pd.read_csv(f1)
    df2 = pd.read_excel(f2)

    # Merge the DataFrames
    matched_df = pd.merge(df1, df2, on=search, how='inner')

    #Print the matched data
    # for index, row in matched_df.iterrows():
    #     print(f"Row {index}: {row}")

    matched_df.to_excel('matched.xlsx', index=False)

    print(f"Data exported successfully to matched.xlsx")

    

f1 = r'vulnerabilities-verified.csv'
f2 = r'IT Asset Inventory.xlsx'
search = 'IP Address'
    
#cross_reference_excel(f1, f2, search)

