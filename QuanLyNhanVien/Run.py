from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *
from ControllerQuanLyNhanVien import *

if __name__ == "__main__":
    model = ModuleNhanVien()
    view = ViewQuanLyNhanVien()
    controller = ControllerNhanVien(model=model, view=view)  # View sẽ được cung cấp sau khi khởi tạo

    # Show view
    view.mainloop()