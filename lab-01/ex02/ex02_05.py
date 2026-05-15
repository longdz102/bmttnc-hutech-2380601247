so_gio_lam = float(input("Nhap so gio lam moi tuan: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44 # so gio lam chuan moi tuan
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan) # so gio lam vuot chuan moi tuan
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5 # tinh tong thu nhap
print(f" so tien thuc linh cua nhan vien: {thuc_linh}")