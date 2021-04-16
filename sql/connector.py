from mysql.connector import connect, Error, MySQLConnection


def get_connection(host: str, user: str, password: str, db_name: str) -> MySQLConnection or None:
    try:
        return connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
    except Error as e:
        print(e)
        return None
