from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# 24. Du doan ket qua phep tru:
# ket_thuc - bat_dau = 15:05 - 13:15 = 1 gio 50 phut (hien thi: 1:50:00)

# 25. Giai thich su khac nhau:
# - datetime: kieu du lieu mieu ta mot mốc thoi gian cu the (ngay, thang, nam, gio, phut, giay).
# - str: kieu chuoi ky tu (van ban) bieu dien thoi gian de in ra hoac hien thi.
# - timedelta: kieu du lieu mieu ta khoang thoi gian (chênh lech) giua hai moc datetime.
