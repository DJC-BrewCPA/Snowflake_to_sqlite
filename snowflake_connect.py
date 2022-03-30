import snowflake.connector
import snowflake_login


def snowflake_connection(sql_query: str):

    conn = snowflake.connector.connect(
        user=snowflake_login.user,
        # password = PASSWORD,
        account=snowflake_login.account,
        authenticator=snowflake_login.authenticator
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

    pass
    # sql_q = """SELECT *

    # table = snowflake_connection(sql_q)

    # print(table.head(20))
    # print(table.columns)

    # with open(r'c:\users\Y893263\Desktop\cols.txt', "w") as textfile:
    #     textfile.truncate(0)
    #     for ele in table.columns:
    #         textfile.write(ele + "\n")