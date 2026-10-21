cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tinh dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In ca gia tri va kieu du lieu cua hai ket qua
print(f"Dien nang (kWh): {dien_nang_kwh}, Kieu du lieu: {type(dien_nang_kwh)}")
print(f"Chi phi: {chi_phi}, Kieu du lieu: {type(chi_phi)}")

# 15. Du doan ket qua truoc khi chay
# dien_nang_kwh = 250 * 90 / 60 / 1000 = 0.375 kWh
# chi_phi = 0.375 * 3000 = 1125.0

# 16. Thay so_phut bang 60 roi chay lai va so sanh
so_phut = 60
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh
print("\n--- Khi so_phut = 60 ---")
print("Dien nang moi:", dien_nang_kwh_moi)
print("Chi phi moi:", chi_phi_moi)
