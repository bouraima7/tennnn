import pandas as pd
import os

def sort_excel():
    df = pd.read_excel('renamed.xlsx')

    desired_order = ['POC 1', 'POC 2', 'severity', 'Name', 'IP Address', 'definition.name', 'definition.description', 'definition.solution', 'output']
    df = df[desired_order]



    #  order of severity 
    severity_order = ['Critical', 'High', 'Medium', 'Low']

    # Convert the 'severity' column to categorical data type with the desired order
    df['severity'] = pd.Categorical(df['severity'], categories=severity_order, ordered=True)

    # Sort the DataFrame by the 'severity' column
    df = df.sort_values(by='severity', ascending= True)
    
    #df.sort_values(by=['Critical','High', 'Medium', 'Low'], ascending= True)

    df.to_excel('sorted.xlsx', index=False)
    print(f"Data exported successfully to sorted.xlsx")