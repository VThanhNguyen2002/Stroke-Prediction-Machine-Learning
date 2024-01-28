---------------------------DATABASE---------------------------
CREATE DATABASE dulieudotquy
GO

USE dulieudotquy
GO

---------------------------TABLE---------------------------
CREATE TABLE ThongTinBacSi
(
	ID_BS char(10) not null,
	Ten_BS nvarchar(30),
	ChuyenKhoa nvarchar(30),
	GioiTinh nvarchar(3),
	Phong int,
	SoDienThoai int,
	Primary key(ID_BS)
)

CREATE TABLE ThongTinBenhNhan
(
	ID_BN char(10) not null,
	Ten_BN nvarchar(30),
	GioiTinh nvarchar(3),
	Tuoi int,
	DiaChi nvarchar(30),
	Primary key(ID_BN)
)

CREATE TABLE ThongTinKhamBenh (
	Gender nvarchar(255),
	Age INT,
	Hypertension INT not null,
	HeartDisease INT not null,
	EverMarried NVARCHAR(255) not null,
	WorkType NVARCHAR(255),
	ResidenceType NVARCHAR(255),
	AvgGlucoseLevel FLOAT not null,
	BMI FLOAT not null,
	SmokingStatus NVARCHAR(255),
	Result NVARCHAR(255),
	Primary key(BMI, AvgGlucoseLevel)
)

---------------------------SELECT---------------------------
SELECT * FROM ThongTinBacSi

SELECT * FROM ThongTinBenhNhan

SELECT * FROM ThongTinKhamBenh
TRUNCATE TABLE ThongTinKhamBenh


---------------------------INSERT_INTO---------------------------
-- ThongTinBacSi
INSERT INTO ThongTinBacSi VALUES ('BS01',N'Nguyễn Văn Thanh',N'Khoa Tim Mạch','Nam','205','0123456789')
INSERT INTO ThongTinBacSi VALUES ('BS02',N'Đoàn Duy Mạnh',N'Khoa Tim Mạch','Nam','204','0123456780')
INSERT INTO ThongTinBacSi VALUES ('BS03',N'Lê Thị Hoa',N'Khoa Tim Mạch',N'Nữ','203','0123456781')

-- ThongTinBenhNhan
INSERT INTO ThongTinBenhNhan VALUES ('BN01',N'Vũ Nguyễn Anh Duy','Nam','30',N'123 Trường Chinh')
INSERT INTO ThongTinBenhNhan VALUES ('BN02',N'Nguyễn Hoài Nam','Nam','48',N'456 Trường Chinh')
INSERT INTO ThongTinBenhNhan VALUES ('BN03',N'Trần Minh Anh',N'Nữ','67',N'789 Trường Chinh')
INSERT INTO ThongTinBenhNhan VALUES ('BN04',N'Nguyễn Thanh Tâm',N'Nữ','50',N'123 Cộng Hoà')
INSERT INTO ThongTinBenhNhan VALUES ('BN05',N'Phạm Duy Thái','Nam','25',N'456 Cộng Hoà')
