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


INSERT INTO NhanVien (MaNhanVien, HoTen, LuongCoBan, LuongHT) VALUES
('NV01', N'Nguy?n V?n An', 10000000, 0),
('NV02', N'Tr?n Th? B?o', 12000000, 0),
('NV03', N'Lê V?n C?nh', 11000000, 0),
('NV04', N'Ph?m Th? ?ào', 11500000, 0),
('NV05', N'Hoàng V?n Em', 10500000, 0),
('NV06', N'V? Th? Gia', 11800000, 0),
('NV07', N'?? Minh Hi?u', 10200000, 0),
('NV08', N'Bùi Ng?c Kiên', 12300000, 0),
('NV09', N'?inh Ti?n Luân', 11100000, 0),
('NV10', N'Mai Ph??ng Mai', 11900000, 0),
('NV11', N'Ngô Quang Nam', 11400000, 0),
('NV12', N'Lê Th? Oanh', 10800000, 0),
('NV13', N'Phan V?n Phú', 10600000, 0),
('NV14', N'Tr?n Qu?c Quân', 11200000, 0),
('NV15', N'Hoàng ?ình S?n', 10300000, 0),
('NV16', N'Nguy?n Minh Tâm', 11700000, 0),
('NV17', N'V? Th? Uyên', 10900000, 0),
('NV18', N'Ph?m V?n V?', 10700000, 0),
('NV19', N'??ng Th? Xuân', 11300000, 0),
('NV20', N'Bùi Thanh Yên', 10400000, 0);


INSERT INTO ChamCongTongHop (MaNhanVien, LoaiNhanVien, SoNgayLam, SoSanPham) VALUES
('NV01', N'Bán Hàng', 22, 150),
('NV02', N'V?n Phòng', 20, 0),
('NV03', N'Không Lo?i', 18, 0),
('NV04', N'Bán Hàng', 25, 165),
('NV05', N'V?n Phòng', 21, 0),
('NV06', N'Bán Hàng', 23, 140),
('NV07', N'Không Lo?i', 17, 0),
('NV08', N'V?n Phòng', 19, 0),
('NV09', N'Bán Hàng', 26, 180),
('NV10', N'Không Lo?i', 20, 0),
('NV11', N'Bán Hàng', 24, 130),
('NV12', N'V?n Phòng', 22, 0),
('NV13', N'Không Lo?i', 21, 0),
('NV14', N'Bán Hàng', 27, 190),
('NV15', N'V?n Phòng', 23, 0),
('NV16', N'Không Lo?i', 19, 0),
('NV17', N'Bán Hàng', 28, 200),
('NV18', N'V?n Phòng', 18, 0),
('NV19', N'Không Lo?i', 20, 0),
('NV20', N'Bán Hàng', 22, 160);