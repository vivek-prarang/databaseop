import pymysql
class DBCon:
    def __init__(self):
        self.host = 'localhost'
        self.username='root'
        self.password=''
        self.database = 'plannerdb'
    def connect(self):
        try:
            conn = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database)
            return conn
        except:
            return None
        

