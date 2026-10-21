# 17. Dung input() de nhan 4 gia tri va in type() ngay sau khi nhap
ma_may = input("Nhap ma may: ")
print("Kieu cua ma_may:", type(ma_may))

cong_suat_str = input("Nhap cong suat W: ")
print("Kieu cua cong_suat_str:", type(cong_suat_str))

so_phut_str = input("Nhap so phut: ")
print("Kieu cua so_phut_str:", type(so_phut_str))

don_gia_str = input("Nhap don gia: ")
print("Kieu cua don_gia_str:", type(don_gia_str))

# 18. Chuyen cong suat sang float, so phut sang int va don gia sang float
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# 19. Tinh lai dien nang va chi phi sau khi chuyen kieu (cong thuc giong Bai 4)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"\nDien nang: {dien_nang_kwh} kWh")
print(f"Chi phi: {chi_phi} VND")
