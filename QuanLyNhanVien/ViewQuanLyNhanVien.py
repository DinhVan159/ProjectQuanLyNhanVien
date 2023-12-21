import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkcalendar import DateEntry #pip install tkcalendar

class ViewQuanLyNhanVien(tk.Tk):
    def __init__(self):
        super().__init__()
        #Tạo Title
        self.title("QUẢN LÝ THÔNG TIN NHÂN VIÊN")
        self.geometry("1200x600")

        # Tạo Label Title
        tk.Label(self, text="QUẢN LÝ THÔNG TIN NHÂN VIÊN", fg='BLUE',
                 font=tkFont.Font(family="Helvetica", size=20, weight="bold")
                ).place(x=380, y=30)

        # Tạo Label và Entry Mã Nhân Viên
        tk.Label(self, text="Mã Nhân Viên:").place(x=900, y=100)
        self.maNV = tk.Entry(self)
        self.maNV.place(x=1050, y=100)

        # Tạo Label và Entry Họ Tên
        tk.Label(self, text="Họ Tên:").place(x=900, y=130)
        self.hoTen = tk.Entry(self)
        self.hoTen.place(x=1050, y=130)

        # Tạo Label và Entry Lương Cơ Bản
        tk.Label(self, text="Lương Cơ Bản:").place(x=900, y=160)
        self.luongCB = tk.Entry(self)
        self.luongCB.place(x=1050, y=160)

        # Tạo Label và Checkbtn Loại Nhân Viên
        tk.Label(self, text="Loại nhân viên:").place(x=900, y=190)
        self.nvVP = tk.BooleanVar()
        tk.Checkbutton(self, text="Nhân viên văn phòng", variable=self.nvVP).place(x=1050, y=190)

        self.nvBH = tk.BooleanVar()
        tk.Checkbutton(self, text="Nhân viên bán hàng", variable=self.nvBH).place(x=1050, y=220)

        self.nvKL = tk.BooleanVar()
        tk.Checkbutton(self, text="Không loại", variable=self.nvKL).place(x=1050, y=250)

        # Tạo Label và Entry Lương Hàng Tháng
        tk.Label(self, text="Lương Hằng Tháng:").place(x=900, y=280)
        self.luongHT = tk.Entry(self, state='readonly')
        self.luongHT.place(x=1050, y=280)

        # Tạo TreeView
        self.tvNV = ttk.Treeview(self, height=20, padding="10px")

        # Tạo các cột trong TreeView
        self.tvNV['columns'] = ('MaNV', 'HoTen', 'LoaiNV', 'LuongCB', 'LuongThang')

        # Đặt tên cho từng cột
        self.tvNV.column("#0", width=50, anchor='center')
        self.tvNV.column("MaNV", width=100, anchor='e')
        self.tvNV.column("HoTen", width=200, anchor='e')
        self.tvNV.column("LoaiNV", width=150, anchor='e')
        self.tvNV.column("LuongCB", width=150, anchor='e')
        self.tvNV.column("LuongThang", width=150, anchor='e')

        # Đặt tên tiêu đề cho từng cột
        self.tvNV.heading("#0", text="STT")
        self.tvNV.heading("MaNV", text="Mã Nhân Viên")
        self.tvNV.heading("HoTen", text="Họ Tên")
        self.tvNV.heading("LoaiNV", text="Loại Nhân Viên")
        self.tvNV.heading("LuongCB", text="Lương Cơ Bản")
        self.tvNV.heading("LuongThang", text="Lương Hàng Tháng")

        # Đặt vị trí
        self.tvNV.place(x=20, y=100)

        # Buttons
        self.btnTimKiem = tk.Button(self, text="Tìm kiếm",
                                  width=8,
                                  background='#CCFFFF')
        self.btnTimKiem.place(x=1060, y=400)

        self.btnLoadNV = tk.Button(self, text="Load NV",
                                    width=8,
                                    background='#CCFFFF')
        self.btnLoadNV.place(x=960, y=400)

        self.btnThemNV = tk.Button(self, text="Thêm", width=8)
        self.btnThemNV.place(x=910, y=450)

        self.xoaNV = tk.Button(self, text="Xóa", width=8)
        self.xoaNV.place(x=1010, y=450)

        self.capnhatNV = tk.Button(self, text="Cập nhật", width=8)
        self.capnhatNV.place(x=1110, y=450)

    def showNV(self, ds: list):
        for index, nv in enumerate(ds):
            self.tvNV.insert("",tk.END,text=index+1, values=tuple(nv), )

    def insertNV(self, index, nv:list):
        nv.insert(0, index)
        self.tvNV.insert(parent="", index=tk.END, values = nv)

    def clearTreeview(self):
        for item in self.tvNV.get_children():
            self.tvNV.delete(item)

# if __name__ == '__main__':
#     ui = ViewQuanLyNhanVien()
#     ui.mainloop()