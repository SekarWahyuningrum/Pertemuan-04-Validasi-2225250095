sudut = float(input("Masukkan sudut (0-180): "))

if sudut <= 0 or sudut >= 180:
    print("Sudut tidak valid")
elif sudut < 90:
    print("Sudut lancip")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut tumpul")