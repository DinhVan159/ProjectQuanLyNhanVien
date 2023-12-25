from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *
from ControllerQuanLyNhanVien import *
from SQLConnect.MSSQLConnect import MSSQLConnect

from tkinter import font as tkFont
from tkinter import *
from  tkinter import messagebox
import tkinter as tk


conx = MSSQLConnect()
def ShowQLNV():
    root.destroy()
    model = ModuleNhanVien()
    view = ViewQuanLyNhanVien()
    controller = ControllerNhanVien(model=model, view=view)
    # Show view
    view.mainloop()

def DangNhap():
    username = user.get()
    password = code.get()
    if (username=="") or (password==""):
        messagebox.showwarning("Thông báo","Vui lòng điền tên đăng nhập hoặc mật khẩu")
    else:
        dsTT = []
        conx.connect()
        sql_query = """
                        SELECT *
                        FROM ThongTinDangNhap
                    """
        ds = conx.query(sql_query)
        dsTT.extend(ds)
        conx.close()
        for userpass in dsTT:
            if (userpass[0] == username) & (userpass[1] == password):
                tTDN = userpass[0]
                ShowQLNV()

def DangKi():
    username = user.get()
    password = code.get()
    if (username == "") or (password == ""):
        messagebox.showwarning("Thông báo", "Vui lòng điền tên đăng nhập hoặc mật khẩu")
    else:
        dsTT = []
        conx.connect()
        sql_query = """
                    SELECT *
                    FROM ThongTinDangNhap
                    WHERE TenDangNhap = '"""+ username +"""'
                    """
        ds = conx.query(sql_query)
        dsTT.extend(ds)
        conx.close()
        if dsTT != []:
            messagebox.showwarning("Thông báo", "Tên đăng nhập đã được sử dụng")
        else:
            conx.connect()
            sql_query1 = """INSERT INTO ThongTinDangNhap (TenDangNhap, MatKhau) VALUES ('""" + username + """','""" + password + """');"""
            conx.excute(sql_query1)
            messagebox.showinfo("Thông báo", "Đăng kí thành công")
#Tạo form Đăng nhập
root=Tk()
root.title("Đăng Nhập")
root.geometry("400x200")

#Tạo Label Title
tk.Label(root, text="ĐĂNG NHẬP",
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=150, y=20)

#Tạo Label và Entry User
tk.Label(root, text="Tài khoản:").place(x=60, y=60)
user = tk.Entry(root, width=30)
user.place(x=140, y=60)

#Tạo Label và Entry Mat khau
tk.Label(root, text="Mật khẩu:").place(x=60, y=90)
code = tk.Entry(root, width=30, show="*")
code.place(x=140, y=90)

#Tạo button Đăng nhập
btnDangnhap = tk.Button(root, text="Đăng nhâp", command=DangNhap,
                                   background='#CCFFFF',
                                   width=8)
btnDangnhap.place(x=140, y=120)

#Tạo button Đăng kí
btnDangki = tk.Button(root, text="Đăng kí", command=DangKi,
                                   background='#CCFFFF',
                                   width=8)
btnDangki.place(x=260, y=120)
root.mainloop()


