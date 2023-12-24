import tkinter as tk
from tkinter import font as tkFont
import tkinter.ttk as ttk
from tkinter import *
from ttkthemes import ThemedTk #pip install ttkthemes
from tkcalendar import DateEntry #pip install tkcalendar
from  tkinter import messagebox

class ViewQuanLyNhanVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        #Tạo Title
        self.title("QUẢN LÝ THÔNG TIN NHÂN VIÊN")
        self.geometry("1200x600")

        # Tạo Label Title
        tk.Label(self, text="QUẢN LÝ THÔNG TIN NHÂN VIÊN", fg='BLUE',
                 font=tkFont.Font(family="Helvetica", size=20, weight="bold")
                ).place(x=380, y=30)

        # Tạo Label và Entry Mã Nhân Viên
        tk.Label(self, text="Mã Nhân Viên:").place(x=900, y=100)
        self.htmaNV = StringVar()
        self.maNV = tk.Entry(self, textvariable=self.htmaNV)
        self.maNV.place(x=1050, y=100)

        # Tạo Label và Entry Họ Tên
        tk.Label(self, text="Họ Tên:").place(x=900, y=130)
        self.hthoTen = StringVar()
        self.hoTen = tk.Entry(self, textvariable=self.hthoTen)
        self.hoTen.place(x=1050, y=130)

        # Tạo Label và Entry Lương Cơ Bản
        tk.Label(self, text="Lương Cơ Bản:").place(x=900, y=160)
        self.htluongCB = StringVar()
        self.luongCB = tk.Entry(self, textvariable=self.htluongCB)
        self.luongCB.place(x=1050, y=160)

        # # Tạo Label và Checkbtn Loại Nhân Viên
        # tk.Label(self, text="Loại nhân viên:").place(x=900, y=190)
        # self.nvVP = tk.StringVar()
        # tk.Checkbutton(self, text="Nhân viên văn phòng", variable=self.nvVP, onvalue="Văn Phòng", offvalue="").place(x=1050, y=190)
        #
        # self.nvBH = tk.StringVar()
        # tk.Checkbutton(self, text="Nhân viên bán hàng", variable=self.nvBH, onvalue="Bán Hàng", offvalue="").place(x=1050, y=220)
        #
        # self.nvKL = tk.StringVar()
        # tk.Checkbutton(self, text="Không loại", variable=self.nvKL, onvalue="Không Loại", offvalue="").place(x=1050, y=250)

        # Tạo Label và Combobox Loại Nhân Viên
        tk.Label(self, text="Loại nhân viên:").place(x=900, y=190)

        self.loaiNV = tk.StringVar()
        self.options = ('Chọn nhân viên','Văn Phòng', 'Bán Hàng', 'Không Loại')
        self.loaiNV.set(self.options[0])

        self.cbx = ttk.Combobox(self,textvariable=self.loaiNV, values=self.options, state='readonly', width=17).place(x=1050, y=190)

        # Tạo Label và Entry Lương Hàng Tháng
        tk.Label(self, text="Lương Hằng Tháng:").place(x=900, y=220)
        self.luongHT = tk.Entry(self, state='readonly')
        self.luongHT.place(x=1050, y=220)

        # Tạo Label và Entry Số Ngày Làm
        tk.Label(self, text="Số Ngày Làm:").place(x=900, y=250)
        self.htsoNgayLam = tk.StringVar()
        self.soNgayLam = tk.Entry(self, textvariable=self.htsoNgayLam)
        self.soNgayLam.place(x=1050, y=250)

        # Tạo Label và Entry Số Sản Phẩm
        tk.Label(self, text="Số Sản Phẩm:").place(x=900, y=280)
        self.htsoSanPham = tk.StringVar()
        self.soSanPham = tk.Entry(self, textvariable=self.htsoSanPham)
        self.soSanPham.place(x=1050, y=280)

        # Tạo TreeView
        self.tvNV = ttk.Treeview(self, height=20, padding="10px")

        # Tạo các cột trong TreeView
        self.tvNV['columns'] = ('MaNV', 'HoTen', 'LoaiNV', 'LuongCB', 'soNgayLam', 'soSanPham', 'LuongThang')

        # Đặt tên cho từng cột
        self.tvNV.column("#0", width=50, anchor='center')
        self.tvNV.column("MaNV", width=100, anchor='e')
        self.tvNV.column("HoTen", width=150, anchor='e')
        self.tvNV.column("LoaiNV", width=100, anchor='e')
        self.tvNV.column("LuongCB", width=100, anchor='e')
        self.tvNV.column("soNgayLam", width=100, anchor='e')
        self.tvNV.column("soSanPham", width=100, anchor='e')
        self.tvNV.column("LuongThang", width=120, anchor='e')

        # Đặt tên tiêu đề cho từng cột
        self.tvNV.heading("#0", text="STT")
        self.tvNV.heading("MaNV", text="Mã Nhân Viên")
        self.tvNV.heading("HoTen", text="Họ Tên")
        self.tvNV.heading("LoaiNV", text="Loại Nhân Viên")
        self.tvNV.heading("LuongCB", text="Lương Cơ Bản")
        self.tvNV.heading("soNgayLam", text="Số Ngày Làm")
        self.tvNV.heading("soSanPham", text="Số Sản Phẩm")
        self.tvNV.heading("LuongThang", text="Lương Hàng Tháng")

        # Đặt vị trí
        self.tvNV.place(x=20, y=100)

        self.tvNV.bind("<<TreeviewSelect>>", self.selectionNV)
        # Buttons
        self.btnTimKiem = tk.Button(self, text="Tìm kiếm",
                                  width=8,
                                  background='#CCFFFF')
        self.btnTimKiem.place(x=1060, y=400)

        self.btnLoadNV = tk.Button(self, text="Load NV",
                                    width=8,
                                    background='#CCFFFF')
        self.btnLoadNV.place(x=960, y=400)

        self.btnThemNV = tk.Button(self, text="Thêm",
                                        background='#CCFFFF',
                                        width=8)
        self.btnThemNV.place(x=910, y=450)

        self.btnXoaNV = tk.Button(self, text="Xóa",
                                        background='#fc3003',
                                        width=8)
        self.btnXoaNV.place(x=1110, y=450)

        self.btnCapnhatNV = tk.Button(self, text="Cập nhật",
                                            background='#CCFFFF',
                                            width=8)
        self.btnCapnhatNV.place(x=1010, y=450)

    # def showNV(self, ds: list):
    #     for index, nv in enumerate(ds):
    #         self.tvNV.insert("",tk.END, text=index+1, values=tuple(nv))

    def showNV(self, ds: list):
        for index, nv in enumerate(ds):
            self.tvNV.insert("",tk.END, text=index+1, values=tuple(nv))

    def selectionNV(self, event):
        print("selected items:")
        self.ojSelected = self.tvNV.item(self.tvNV.selection())['values']
        print(self.ojSelected)

        #Hiển thị lên Entry
        self.htmaNV.set(self.ojSelected[0])
        self.hthoTen.set(self.ojSelected[1])
        self.htluongCB.set(self.ojSelected[3])
        self.loaiNV.set(self.ojSelected[2])
        self.htsoNgayLam.set(self.ojSelected[4])
        self.htsoSanPham.set(self.ojSelected[5])

    def clearTreeview(self):
        for item in self.tvNV.get_children():
            self.tvNV.delete(item)

    def messageWR(self, ms):
        messagebox.showwarning("Thông báo", ms)