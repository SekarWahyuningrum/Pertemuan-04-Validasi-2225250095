# Pertemuan-04-Validasi-2225250095


**Nama:** Sekar Wahyuningrum

**NIM:** 2225250095

**Kelas:** 3E


## Tujuan

Membangun program validasi dan klasifikasi dengan menggunakan struktur `if-elif-else`.

Program yang dibuat menerapkan:

* Seleksi multi-kondisi.
* Validasi tipe data.
* Validasi rentang nilai.
* Klasifikasi berdasarkan beberapa kondisi.
* Pengujian program menggunakan beberapa test case.

## Struktur Folder

```text
pertemuan-04-validasi-2225250120/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_predikat_nilai.py
│   ├── 02_kategori_bilangan.py
│   ├── 03_validasi_rentang.py
│   ├── 04_validasi_tipe.py
│   └── 05_klasifikasi_segitiga_sudut.py
│
└── praktik/
    └── validasi_klasifikasi_nilai.py
```

## Cara Menjalankan

Untuk menjalankan program Praktik 1, gunakan perintah:

```bash
python3 praktik/validasi_klasifikasi_nilai.py
```

Jika menggunakan Windows dan `python3` tidak dapat digunakan, dapat menggunakan:

```bash
python praktik/validasi_klasifikasi_nilai.py
```

## Tabel Keputusan

| Predikat | Kondisi Nilai Akhir |
| -------- | ------------------- |
| A        | Nilai akhir >= 85   |
| B        | Nilai akhir >= 70   |
| C        | Nilai akhir >= 60   |
| D        | Nilai akhir >= 50   |
| E        | Nilai akhir < 50    |

Nilai akhir dihitung dengan rumus:

```text
Nilai Akhir = 0.6 × Nilai Ujian + 0.4 × Nilai Tugas
```

Selain nilai akhir, program juga memvalidasi kehadiran.

* Kehadiran < 80% → Tidak memenuhi syarat kehadiran.
* Kehadiran >= 80% → Dilanjutkan ke proses klasifikasi nilai.

## Hasil Pengujian

| No | Nilai Ujian | Nilai Tugas | Kehadiran | Nilai Akhir | Predikat | Status                          |
| -- | ----------: | ----------: | --------: | ----------: | -------- | ------------------------------- |
| 1  |          90 |          80 |        95 |       86.00 | A        | Lulus                           |
| 2  |          75 |          70 |        85 |       73.00 | B        | Lulus                           |
| 3  |          60 |          60 |        80 |       60.00 | C        | Lulus                           |
| 4  |          55 |          50 |        90 |       53.00 | D        | Belum lulus                     |
| 5  |          40 |          30 |       100 |       36.00 | E        | Belum lulus                     |
| 6  |          90 |          90 |        75 |       90.00 | -        | Tidak memenuhi syarat kehadiran |

### Pengujian Input Tidak Valid

| No | Input       | Hasil                                                    |
| -- | ----------- | -------------------------------------------------------- |
| 7  | 105, 80, 90 | Masukan ditolak karena nilai ujian di luar rentang 0–100 |
| 8  | 80, -5, 90  | Masukan ditolak karena nilai tugas di luar rentang 0–100 |
| 9  | 80, 80, abc | Masukan ditolak karena data harus berupa angka           |

## Refleksi

Dalam pembuatan program ini, validasi input diperlukan agar program dapat menangani data yang tidak sesuai. Salah satu contoh adalah ketika pengguna memasukkan teks seperti `abc` pada bagian nilai. Program menggunakan `try-except` untuk menangani kesalahan tersebut sehingga program tidak langsung berhenti dan dapat memberikan pesan penolakan kepada pengguna.

Selain itu, validasi rentang memastikan bahwa nilai ujian, tugas, dan kehadiran berada pada rentang 0 sampai 100. Setelah data dinyatakan valid, program melakukan perhitungan nilai akhir dan klasifikasi menggunakan struktur `if-elif-else`.

## Kesimpulan

Program Praktik 1 menerapkan seleksi multi-kondisi dan validasi input dalam Python. Program dapat menerima input, memvalidasi tipe dan rentang data, menghitung nilai akhir, memeriksa persyaratan kehadiran, serta menentukan predikat dan status kelulusan berdasarkan kondisi yang telah ditentukan.
