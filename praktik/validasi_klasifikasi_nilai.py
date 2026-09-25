if a <= 0 or b <= 0 or c <= 0:
    print("Masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
elif abs(a + b + c - 180) > 1e-9:
    print("Masukan ditolak: jumlah ketiga sudut harus 180 derajat.")
else:
    terbesar = max(a, b, c)

    if terbesar > 90:
        print("Segitiga tumpul")
    elif abs(terbesar - 90) < 1e-9:
        print("Segitiga siku-siku")
    else:
        print("Segitiga lancip")
