# Pertemuan-04-Validasi-2225250095
# Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input

**Nama:** Sekar Wahyuningrum
**NIM:** 2225250095
**Kelas:** 3E

## Tujuan

Praktikum ini bertujuan untuk membangun program yang menerapkan seleksi multi-kondisi menggunakan struktur `if-elif-else` serta melakukan validasi terhadap input pengguna.

Program yang dibuat digunakan untuk:

1. Memvalidasi tiga nilai sudut segitiga.
2. Memastikan setiap sudut lebih dari 0 derajat.
3. Memastikan jumlah ketiga sudut adalah 180 derajat.
4. Mengklasifikasikan segitiga berdasarkan sudut terbesarnya menjadi segitiga lancip, siku-siku, atau tumpul.

## Cara Menjalankan

Pastikan Python 3 sudah terpasang pada komputer. Jalankan program melalui terminal dengan perintah:

```bash
python3 praktik/validasi_klasifikasi_nilai.py
```

Kemudian masukkan nilai untuk sudut A, B, dan C ketika diminta oleh program.

Contoh:

```text
Sudut A: 60
Sudut B: 60
Sudut C: 60
Segitiga lancip
```

## Tabel Keputusan

| Kategori                                | Syarat                                                       | Contoh Masukan          | Keluaran                                                  |
| --------------------------------------- | ------------------------------------------------------------ | ----------------------- | --------------------------------------------------------- |
| Input ditolak — sudut tidak valid       | Salah satu atau lebih sudut `<= 0`                           | A = 0, B = 90, C = 90   | Masukan ditolak: setiap sudut harus lebih dari 0 derajat. |
| Input ditolak — jumlah sudut tidak 180° | Semua sudut `> 0`, tetapi `A + B + C != 180`                 | A = 60, B = 60, C = 70  | Masukan ditolak: jumlah ketiga sudut harus 180 derajat.   |
| Segitiga lancip                         | Semua sudut `> 0`, jumlah = 180°, dan sudut terbesar `< 90°` | A = 60, B = 60, C = 60  | Segitiga lancip                                           |
| Segitiga siku-siku                      | Semua sudut `> 0`, jumlah = 180°, dan salah satu sudut = 90° | A = 90, B = 60, C = 30  | Segitiga siku-siku                                        |
| Segitiga tumpul                         | Semua sudut `> 0`, jumlah = 180°, dan sudut terbesar `> 90°` | A = 120, B = 30, C = 30 | Segitiga tumpul                                           |

## Hasil Pengujian

| No. | Masukan (A, B, C) | Keluaran yang Diharapkan                       | Keluaran Aktual                                | Status   |
| --- | ----------------- | ---------------------------------------------- | ---------------------------------------------- | -------- |
| 1   | 60, 60, 60        | Segitiga lancip                                | Segitiga lancip                                | Berhasil |
| 2   | 90, 60, 30        | Segitiga siku-siku                             | Segitiga siku-siku                             | Berhasil |
| 3   | 120, 30, 30       | Segitiga tumpul                                | Segitiga tumpul                                | Berhasil |
| 4   | 0, 90, 90         | Masukan ditolak karena sudut harus > 0         | Masukan ditolak karena sudut harus > 0         | Berhasil |
| 5   | -10, 100, 90      | Masukan ditolak karena sudut harus > 0         | Masukan ditolak karena sudut harus > 0         | Berhasil |
| 6   | 60, 60, 70        | Masukan ditolak karena jumlah sudut bukan 180° | Masukan ditolak karena jumlah sudut bukan 180° | Berhasil |
| 7   | 45, 45, 90        | Segitiga siku-siku                             | Segitiga siku-siku                             | Berhasil |

## Refleksi

Salah satu masukan tidak valid yang perlu diperhatikan adalah ketika pengguna memasukkan salah satu sudut dengan nilai **0 atau negatif**. Jika hanya memeriksa jumlah ketiga sudut sama dengan 180°, beberapa input yang tidak memenuhi syarat sebagai sudut segitiga dapat terlewat.

Contohnya:

```text
Sudut A: 0
Sudut B: 90
Sudut C: 90
```

Jumlah ketiga sudut tersebut memang 180°, tetapi input tersebut tidak valid karena sudut A bernilai 0°.

Untuk menangani masalah tersebut, program menambahkan kondisi:

```python
if a <= 0 or b <= 0 or c <= 0:
    print("Masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
```

Dengan validasi tersebut, program dapat menolak sudut yang bernilai nol atau negatif sebelum melakukan proses klasifikasi.

Selain itu, program menggunakan `if-elif-else` untuk memastikan hanya satu kategori yang diberikan berdasarkan kondisi yang terpenuhi.
