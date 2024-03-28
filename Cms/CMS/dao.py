import pyodbc

def connect_to_sql_server():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=ABISHEK_ARVIND\SQLEXPRESS01;'
                              'Database=Courier;'
                              'Trusted_Connection=yes;')
        print("Connected Successfully")
        return conn
    except pyodbc.Error as ex:
        print(f"Error: {ex}")


def close_connection(conn):
    conn.close()
    print("Connection closed.")
