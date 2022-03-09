## Get data from Snowflake and store in SQlite

import snowflake_connect
import sqlite_connect
import snowflake_queries




def main():

    try: 
        ## get data from Snowflake
        df = snowflake_connect.snowflake_connection(sql_query=sql_query)

        ## return sqlite connection
        conn = sqlite_connect.create_connection(db_file=sqlite_db)

        ## store df from SF to sqlite
        df.to_sql(name='test',
                con=conn,
                if_exists='replace',
              index_label='id')

    finally:
        # close sqlite conn
        conn.close()


if __name__=='__main__':

    sql_query = snowflake_queries.sales_accrual_q
    sqlite_db = r"C:\Users\Y893263\sqlite\Regions_db\Region_1.db"

    _ = main()

   
    

