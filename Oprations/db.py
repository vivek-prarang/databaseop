
from dbconn import DBCon

class Model:
    def get_verticals(self):
        conn = DBCon().connect()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM verticalsname")
        verticals = cursor.fetchall()
        return verticals