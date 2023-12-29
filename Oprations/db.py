
from dbconn import DBCon

class Model:
    def __init__(self):
        self.conn = DBCon().connect
        self.cursor = self.conn.cursor()
    def get_verticals(self):
        self.cursor.execute("SELECT * FROM verticalsname")
        verticals = self.cursor.fetchall()
        return verticals