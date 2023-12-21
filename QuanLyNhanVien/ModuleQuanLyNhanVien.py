from ProjectQuanLyNhanVien.SQLConnect.MSSQLConnect import MSSQLConnect

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

    def close(self):
        self.conn.close()