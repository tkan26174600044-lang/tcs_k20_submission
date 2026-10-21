# Đoan ma nguyen trang va da duoc sua loi
ma_may = input("Nhap ma may: ")
# Loi 1: cong_suat_w la chuoi (str), khong the nhan/chia voi so.
# Sua: ep kieu float(input(...))
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

# Loi 2: Cú phap f-string sai print(f'Máy: {ma_may}') va thieu ngoac dong o print dien nang
# Sua: viet dung f-string va ngoac
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")

# 23. Comment mo ta cac loi da phat hien:
# Loi 1: TypeError - bien cong_suat_w chua duoc chuyen sang kieu so (float) nen khong the thuc hien phep tinh.
# Loi 2: SyntaxError - cu phap f-string o dong print(f'May: {ma_may}') va thieu ngoac dong o dong cuoi.

