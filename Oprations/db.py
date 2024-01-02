
from dbconn import DBCon

class Model:
    def get_verticals(self):
        conn = DBCon().connect()
        try:
            with conn.cursor() as cursor:
                # Execute your SQL query
                sql = 'SELECT * FROM verticalsname'
                cursor.execute(sql)

            # Fetch all the data
                verticals = cursor.get()

        finally:
            conn.close()
        return verticals
        