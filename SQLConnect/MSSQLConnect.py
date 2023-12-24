import pyodbc

class MSSQLConnect:
    def __init__(self,driver = 'ODBC Driver 17 for SQL Server',
                server = 'DESKTOP-V4L18NQ',
                database = 'qlnv5',
                username = 'admin',
                password = '123456'):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.error = 0
    def connect(self):
        try:
            str_sql = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(self.driver,
                                                                              self.server,
                                                                              self.database,
                                                                              self.username,
                                                                              self.password)
            self.connection = pyodbc.connect(str_sql)
            print("Connection successful")
        except Exception as e:
            print("Error in connection: ", e)

    def query(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def excute(self, sql):
            cursor = self.connection.cursor()
            cursor.execute(sql)
            cursor.commit()
    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection close")

# #Test
# conn = MSSQLConnect()
# conn.connect()
#
# sql_query = """SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan
#               FROM NhanVien NV INNER JOIN ChamCongTongHop CC
#               ON NV.MaNhanVien = CC.MaNhanVien"""
# results = conn.query(sql_query)
#
# print(results)
