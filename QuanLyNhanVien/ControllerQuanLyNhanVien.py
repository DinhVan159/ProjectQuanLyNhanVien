from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *

class ControllerNhanVien:
    def __init__(self, model: ModuleNhanVien, view: ViewQuanLyNhanVien):
        self.model = model
        self.view = view

        self.view.btnLoadNV.config(command=self.loadNV)
        self.view.btnTimKiem.config(command=self.timNV)
        self.view.btnThemNV.config(command=self.themNV)
    def loadNV(self):
        self.model.loadNV()
        self.view.clearTreeview()
        self.view.showNV(self.model.dsNV)
        #Test hiển thị
        # for nv in self.model.dsNV:
        #     print("Test", nv)
    def timNV(self):
        self.model.timNV(self.view.maNV.get())
        self.view.clearTreeview()
        self.view.showNV(self.model.dsNV)

    def themNV(self):
        dataNV = [self.view.maNV.get(), self.view.hoTen.get(), self.view.luongCB.get(), "Văn Phòng",
                self.view.soNgayLam.get(), self.view.soSanPham.get()]
        if dataNV != ['', '', '', 'Văn Phòng', '', '']:
            self.model.themNV(dataNV)
            self.view.clearTreeview()
            # self.model.loadNV()
            self.view.showNV(self.model.dsNV)








