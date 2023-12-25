create database qlnv5;

CREATE TABLE NhanVien (
    MaNhanVien VARCHAR(255) PRIMARY KEY,
    HoTen NVARCHAR(255) NOT NULL,
    LuongCoBan DECIMAL(10, 2) NOT NULL,
	LuongHT DECIMAL (10, 2) NOT NULL
);

CREATE TABLE ChamCongTongHop (
    MaNhanVien VARCHAR(255),
    LoaiNhanVien NVARCHAR(255),
    SoNgayLam INT,
    SoSanPham INT,
    FOREIGN KEY (MaNhanVien) REFERENCES NhanVien(MaNhanVien)
);

CREATE TABLE ThongTinDangNhap (
    TenDangNhap VARCHAR(255) PRIMARY KEY,
    MatKhau VARCHAR(255) NOT NULL
);

INSERT INTO ThongTinDangNhap (TenDangNhap, MatKhau) VALUES ('admin', '1'), ('admin1', '1');

INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan, LuongHT) VALUES
('NV01', N'Nguy?n V?n An', 10000000, 0),
('NV02', N'Tr?n Th? B?o', 12000000, 0),
('NV03', N'L� V?n C?nh', 11000000, 0),
('NV04', N'Ph?m Th? ?�o', 11500000, 0),
('NV05', N'Ho�ng V?n Em', 10500000, 0),
('NV06', N'V? Th? Gia', 11800000, 0),
('NV07', N'?? Minh Hi?u', 10200000, 0),
('NV08', N'B�i Ng?c Ki�n', 12300000, 0),
('NV09', N'?inh Ti?n Lu�n', 11100000, 0),
('NV10', N'Mai Ph??ng Mai', 11900000, 0),
('NV11', N'Ng� Quang Nam', 11400000, 0),
('NV12', N'L� Th? Oanh', 10800000, 0),
('NV13', N'Phan V?n Ph�', 10600000, 0),
('NV14', N'Tr?n Qu?c Qu�n', 11200000, 0),
('NV15', N'Ho�ng ?�nh S?n', 10300000, 0),
('NV16', N'Nguy?n Minh T�m', 11700000, 0),
('NV17', N'V? Th? Uy�n', 10900000, 0),
('NV18', N'Ph?m V?n V?', 10700000, 0),
('NV19', N'??ng Th? Xu�n', 11300000, 0),
('NV20', N'B�i Thanh Y�n', 10400000, 0);


INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham) VALUES
('NV01', N'B�n H�ng', 22, 150),
('NV02', N'V?n Ph�ng', 20, 0),
('NV03', N'Kh�ng Lo?i', 18, 0),
('NV04', N'B�n H�ng', 25, 165),
('NV05', N'V?n Ph�ng', 21, 0),
('NV06', N'B�n H�ng', 23, 140),
('NV07', N'Kh�ng Lo?i', 17, 0),
('NV08', N'V?n Ph�ng', 19, 0),
('NV09', N'B�n H�ng', 26, 180),
('NV10', N'Kh�ng Lo?i', 20, 0),
('NV11', N'B�n H�ng', 24, 130),
('NV12', N'V?n Ph�ng', 22, 0),
('NV13', N'Kh�ng Lo?i', 21, 0),
('NV14', N'B�n H�ng', 27, 190),
('NV15', N'V?n Ph�ng', 23, 0),
('NV16', N'Kh�ng Lo?i', 19, 0),
('NV17', N'B�n H�ng', 28, 200),
('NV18', N'V?n Ph�ng', 18, 0),
('NV19', N'Kh�ng Lo?i', 20, 0),
('NV20', N'B�n H�ng', 22, 160);