import snowflake.connector


def snowflake_connection(sql_query: str):

    conn = snowflake.connector.connect(
        user='CHASE.CRIBBET@ANHEUSER-BUSCH.COM',
        # password = PASSWORD,
        account='abinbev_naz.east-us-2.azure',
        authenticator='externalbrowser'
    )

    cs = conn.cursor()
    try:
        cs.execute(sql_query)
        table = cs.fetch_pandas_all()
    finally:
        cs.close()
    conn.close()

    return table




if __name__ == "__main__":

    sql_q = """SELECT"""

    table = snowflake_connection(sql_q)

    print(table.head(20))
    print(table.columns)

    with open(r'c:\users\Y893263\Desktop\cols.txt', "w") as textfile:
        textfile.truncate(0)
        for ele in table.columns:
            textfile.write(ele + "\n")