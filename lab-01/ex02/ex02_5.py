so_gio_lam = float(input("nhập số giờ làm mỗi tuần:"))
luong_gio = float(input("nhập số giờ làm"))
gio_tieu_chuan = 44 # số giờ làm mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio *1.5
print(f"số tiền thực lĩnh của nhân viên:{thuc_linh}")