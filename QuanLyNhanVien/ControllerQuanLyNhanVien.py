from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *

class ControllerNhanVien:
    def __init__(self, model: ModuleNhanVien, view: ViewQuanLyNhanVien):
        self.model = model
        self.view = view
        self.loaiNV = 'Văn phòng'

        self.view.btnLoadNV.config(command=self.loadNV)
        self.view.btnTimKiem.config(command=self.timNV)
        self.view.btnThemNV.config(command=self.themNV)
        self.view.btnXoaNV.config(command=self.xoaNV)

    def loadNV(self):
        self.model.setdsNVnull()
        self.view.clearTreeview()
        self.model.loadNV()
        self.view.showNV(self.model.dsNV)
        #Test hiển thị
        # for nv in self.model.dsNV:
        #     print("Test", nv)
    def timNV(self):
        self.model.setdsNVnull()
        self.model.timNV(self.view.maNV.get())
        self.view.clearTreeview()
        self.view.showNV(self.model.dsNV)

    def themNV(self):
        self.model.setdsNVnull()
        thucThi = 0

        if self.view.loaiNV.get() != 'Chọn nhân viên':
            self.loaiNV = self.view.loaiNV.get()

        dataNV = [self.view.maNV.get(), self.view.hoTen.get(), self.view.luongCB.get(), self.loaiNV,
                self.view.soNgayLam.get(), self.view.soSanPham.get()]

        self.model.timNV(self.view.maNV.get())

        for i in dataNV:
            if i == '':
                thucThi = 1

        if (thucThi == 0) & (self.model.dsNV == []):
            self.model.themNV(dataNV)
            self.view.clearTreeview()
            self.model.loadNV()
            self.view.showNV(self.model.dsNV)
            print("Them thanh cong nhan vien")
        else:
            print("Them khong thanh cong nhan vien")

    def xoaNV(self):
        self.model.setdsNVnull()
        self.model.xoaNV(self.view.ojSelected)
        self.view.clearTreeview()
        self.model.loadNV()
        self.view.showNV(self.model.dsNV)
        print("Xoa thanh cong nhan vien")

