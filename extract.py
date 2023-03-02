import csv
import pandas as pd

def get_agriculture_data(file):
    """
    Parameters:
        file (str): path to CSV file
        
    Returns:
        df (Dataframe): Dataframe with data from CSV file
    
    """
    df = pd.read_csv(file)
    return df
 

if __name__ == "__main__":
    df = get_agriculture_data('data/APY.csv')
    print(df.head(10))
