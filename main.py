## Get data from Snowflake and store in SQlite

import snowflake_connect
import sqlite_connect
import snowflake_queries


sql_query = """SELECT *
            FROM ABI_WH.EDW.GL_LN_ITEM
            LIMIT 20"""

sqlite_db = r"C:\Users\Y893263\sqlite\Regions_db\Region_1.db"

if __name__=='__main__':
    
    ## get data from Snowflake
    df = snowflake_connect.snowflake_connection(sql_query=sql_query)

    ## return sqlite connection
    conn = sqlite_connect.create_connection(db_file=sqlite_db)

    ## store df from SF to sqlite
    df.to_sql(name='test',
              con=conn,
              if_exists='replace',
              index_label='id')

    # close sqlite conn
    conn.close()
    

