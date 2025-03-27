so_gio_lam = float(input("Nhập số giờ làm việc mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ  làm tiêu chuẩn: "))
#số giờ làm việc tiêu chuẩn mỗi tuần
gio_tieu_chuan = 44 
#số giờ làm vượt chuẩn mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
#tính tổng thu nhập
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print("Số tiền thực lĩnh của nhân viên: ", thuc_linh)