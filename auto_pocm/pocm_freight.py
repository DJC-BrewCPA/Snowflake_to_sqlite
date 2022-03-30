from pytest import importorskip
import sys
import pandas as pd
import numpy as np

sys.path.append(r"C:\Users\Y893263\Python_snowflake")

from snowflake_connect import snowflake_connection
from snowflake_queries import pocm_freight
import pocm_files



def get_sf():
    
    """Function gets 2022 POCM freight data"""

    sql_query = pocm_freight

    df = snowflake_connection(sql_query)
    #Add bool column for excel sumifs output
    df['Bool'] = np.where(df['AMOUNT'] < 0, 'False', 'True')
    return df

def create_excel_wbs(df, file_name):
    
    with pd.ExcelWriter(f"{file_name}.xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        
        df.to_excel(writer, sheet_name='data', index=False)



if __name__=='__main__':

    dir = pocm_files.dir
    file = pocm_files.file
    file_name = dir + '\\' + file
    print(file_name)

    df = get_sf()
    print('got data')
    _ = create_excel_wbs(df, file_name)
    print('complete')

    