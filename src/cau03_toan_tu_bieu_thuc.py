tong_phut = 135
cong_suat_w = 250

# 9. Dung // va % de tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_du)

# 10. Tao bien su_dung_lau nhan True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Su dung lau (> 60 phut):", su_dung_lau)

# 11. Tao bien du_lieu_hop_le nhan True khi cong_suat_w > 0 va tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

# 12. Du doan roi kiem chung hai bieu thuc:
# - Bieu thuc 1: 100 + 20 * 3 => Nhan truoc cong sau: 20*3=60; 100+60 = 160
# - Bieu thuc 2: (100 + 20) * 3 => Trong ngoac truoc: (100+20)=120; 120*3 = 360
bt1 = 100 + 20 * 3
bt2 = (100 + 20) * 3
print("Ket qua bieu thuc 1 (100 + 20 * 3):", bt1)
print("Ket qua bieu thuc 2 ((100 + 20) * 3):", bt2)

