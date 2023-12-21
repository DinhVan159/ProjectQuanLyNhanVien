from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *

class ControllerNhanVien:
    def __init__(self, model: ModuleNhanVien, view: ViewQuanLyNhanVien):
        self.model = model
        self.view = view

        self.view.btnLoadNV.config(command=self.loadNV)

    def loadNV(self):
        self.model.loadNV()
        self.view.clearTreeview()
        self.view.showNV(self.model.dsNV)
        #Test hiển thị
        # for nv in self.model.dsNV:
        #     print("Test", nv)


    # def showNV(self):
