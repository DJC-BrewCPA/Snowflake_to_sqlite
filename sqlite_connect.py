import sqlite3
from sqlite3 import Error


## Create sqlite connection

def create_connection(db_file):
    """Create db connection to SQlite db
    
    Returns: conn --> used in to_sql method for Snowflake transfer"""

    conn = None

    try: 
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

if __name__ == "__main__":
    region_1 = r"C:\Users\Y893263\sqlite\Regions_db\Region_1.db"

