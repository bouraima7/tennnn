import pandas as pd


def rename_excel():
    df = pd.read_excel('matched.xlsx')

    df.replace({'Christopher M. Sherman': 'John Constantine'}, inplace=True)
    df.replace({'Chris Sherman': 'John Constantine'}, inplace=True)


    df.to_excel('renamed.xlsx', index=False)
    print(f'Christopher M. Sherman has been replaced with John Constantine')


