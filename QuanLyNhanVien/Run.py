from ModuleQuanLyNhanVien import *
from ViewQuanLyNhanVien import *
from ControllerQuanLyNhanVien import *

if __name__ == "__main__":

    model = ModuleNhanVien()
    view = ViewQuanLyNhanVien()
    controller = ControllerNhanVien(model=model, view=view)

    # Show view
    view.mainloop()