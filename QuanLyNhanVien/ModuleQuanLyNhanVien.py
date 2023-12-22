from SQLConnect.MSSQLConnect import MSSQLConnect

class ModuleNhanVien:
    def __init__(self):
        self.dsNV = []
        self.conn = MSSQLConnect()

    def loadNV(self):
        self.conn.connect()
        sql_query = """
                    SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan
                    FROM NhanVien NV INNER JOIN ChamCongTongHop CC
                    ON NV.MaNhanVien = CC.MaNhanVien
                    """
        ds = self.conn.query(sql_query)
        self.dsNV.extend(ds)
        self.conn.close()
    def timNV(self, maNV):
        self.conn.connect()
        sql_query = """
                    SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan
                    FROM NhanVien NV INNER JOIN ChamCongTongHop CC
                    ON NV.MaNhanVien = CC.MaNhanVien
                    WHERE NV.MaNhanVien = '"""+ maNV +"""'
                    """
        ds = self.conn.query(sql_query)
        print(type(sql_query))
        self.dsNV.extend(ds)
        self.conn.close()

    def themNV(self, dataNV):
        self.conn.connect()
        sql_query1 = """INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan) VALUES('"""+dataNV[0]+"""',N'"""+dataNV[1]+"""',"""+dataNV[2]+""");"""
        sql_query2 = """INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham) VALUES('""" +dataNV[0]+ """',N'""" + dataNV[3] + """',""" + dataNV[4] + ""","""+ dataNV[5] + """);"""
        sql_query3 = """
                    SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan
                    FROM NhanVien NV INNER JOIN ChamCongTongHop CC
                    ON NV.MaNhanVien = CC.MaNhanVien
                    """
        sql_query = sql_query1+sql_query2+sql_query3
        print(sql_query)
        print(type(sql_query))
        ds = self.conn.query(sql_query)

        self.dsNV.extend(ds)
        self.conn.close()
    def close(self):
        self.conn.close()