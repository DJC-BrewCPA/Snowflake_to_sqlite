import sqlite3
from sqlite3 import Error


## Create sqlite connection

def create_connection(db_file):
    """Create db connection to SQlite db"""

    conn = None

    try: 
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_connection(r"C:\Users\Y893263\sqlite\Regions_db\Region_1.db")