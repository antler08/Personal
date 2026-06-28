import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    df = person.merge(address, how='left', on='personId')
    df = df.drop(columns=['personId', 'addressId'])

    #print(df)
    return df
