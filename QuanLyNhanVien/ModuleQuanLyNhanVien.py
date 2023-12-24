from SQLConnect.MSSQLConnect import MSSQLConnect

class ModuleNhanVien:
    def __init__(self):
        self.dsNV = []
        self.conn = MSSQLConnect()

    def setdsNVnull(self):
        self.dsNV = []
    def loadNV(self):
        self.conn.connect()
        sql_query = """
                    SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan, CC.SoNgayLam, CC.SoSanPham, NV.LuongHT
                    FROM NhanVien NV INNER JOIN ChamCongTongHop CC
                    ON NV.MaNhanVien = CC.MaNhanVien
                    """
        #######
        ds = self.conn.query(sql_query)
        print("ds",ds)

        self.dsNV.extend(ds)
        print("dsNV", self.dsNV)
        #######
        self.conn.close()
    def timNV(self, maNV):
        self.conn.connect()
        sql_query = """
                    SELECT NV.MaNhanVien, NV.HoTen, CC.LoaiNhanVien, NV.LuongCoBan, CC.SoNgayLam, CC.SoSanPham, NV.LuongHT
                    FROM NhanVien NV INNER JOIN ChamCongTongHop CC
                    ON NV.MaNhanVien = CC.MaNhanVien
                    WHERE NV.MaNhanVien = '"""+ maNV +"""'
                    """
        ds = self.conn.query(sql_query)
        self.dsNV.extend(ds)
        self.conn.close()

    def themNV(self, dataNV):
        self.conn.connect()
        sql_query1 = """INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan, LuongHT) VALUES('"""+dataNV[0]+"""',N'"""+dataNV[1]+"""',"""+dataNV[2]+""", 0);"""
        sql_query2 = """INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham) VALUES('""" +dataNV[0]+ """',N'""" + dataNV[3] + """',""" + dataNV[4] + ""","""+ dataNV[5] + """);"""
        sql_query = sql_query1+sql_query2
        self.conn.excute(sql_query)
        self.conn.close()

    def xoaNV(self, dataNV):
        self.conn.connect()
        sql_query1 = """DELETE FROM ChamCongTongHop WHERE MaNhanVien = '""" + str(dataNV[0]) + """'"""
        sql_query2 = """DELETE FROM NhanVien WHERE MaNhanVien = '""" + str(dataNV[0]) + """'"""
        sql_query = sql_query1 + sql_query2
        self.conn.excute(sql_query)
        self.conn.close()

    def capnhatNV(self, dataNV):
        self.conn.connect()
        print(dataNV)
        sql_query1 = """UPDATE ChamCongTongHop SET LoaiNhanVien = N'""" + dataNV[3] + """', SoNgayLam = """ + str(dataNV[4]) + """, SoSanPham = """ + str(dataNV[5]) + """ WHERE MaNhanVien = '""" + dataNV[0] +"""' """
        sql_query2 = """UPDATE NhanVien SET HoTen = N'""" + dataNV[1] + """', LuongCoBan = """ + dataNV[2] + """ WHERE MaNhanVien = '""" + dataNV[0] + """'"""
        sql_query = sql_query1 + sql_query2

        print(sql_query)
        self.conn.excute(sql_query)
        self.conn.close()

    def tinhluongHT(self, datatinhluongNV, luongTH):
        self.conn.connect()
        sql_query = """UPDATE NhanVien SET LuongHT = """ + str(luongTH) +  """ WHERE MaNhanVien = '""" + datatinhluongNV[0] + """'"""

        print(sql_query)
        self.conn.excute(sql_query)
        self.conn.close()
    def close(self):
        self.conn.close()