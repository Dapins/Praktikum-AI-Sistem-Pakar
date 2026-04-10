# Praktikum 1-AI-Sistem-Pakar 
# Sistem Pakar Diagnosa Penyakit Gastro Usus 

## Deskripsi Sistem

Sistem ini merupakan **sistem pakar (expert system)** yang digunakan untuk membantu melakukan **diagnosa penyakit gastro usus** berdasarkan gejala yang dialami oleh pasien.

Aplikasi dibuat menggunakan bahasa pemrograman Python dengan antarmuka berbasis web menggunakan Streamlit, sehingga dapat dijalankan secara interaktif melalui browser tanpa instalasi tambahan di sisi pengguna.

Pendekatan yang digunakan adalah **rule-based system**, yaitu sistem yang bekerja berdasarkan kumpulan aturan (rules) yang telah didefinisikan sebelumnya oleh berdasarkan rule yang telah ada.

---

## Tujuan Penggunaan

Sistem ini bertujuan untuk:

* Membantu dalam **mengidentifikasi kemungkinan penyakit gastro usus**
* Memberikan **persentase tingkat kemungkinan diagnosa**

---

## Cara Kerja Sistem (Alur Logika)

Alur kerja sistem dapat dijelaskan sebagai berikut:

1. **Input Gejala**

   * Pengguna memilih gejala melalui antarmuka GUI (checkbox/multiselect)

2. **Pemrosesan Data**

   * Sistem membaca gejala yang dipilih
   * Gejala dibandingkan dengan knowledge base

3. **Proses Inferensi**

   * Setiap penyakit memiliki sejumlah gejala menengah
   * Setiap gejala menengah memiliki relasi ke gejala awal
   * Sistem menghitung kecocokan berdasarkan rule yang ada

4. **Perhitungan Persentase**

   * Persentase dihitung berdasarkan:

     * jumlah gejala yang cocok
     * bobot setiap gejala menengah

5. **Output**

   * Sistem menampilkan:

     * Ranking diagnosa
     * Persentase masing-masing penyakit
     * Gejala yang mendukung diagnosa

---

## Knowledge Base (Basis Pengetahuan)

Knowledge base dari sistem pakar yang berisi:

### 1. Data Diagnosa

Setiap diagnosa memiliki:

* Nama penyakit
* Daftar gejala menengah

Contoh:

```
Keracunan Salmonellae:
- Mencret
- Muntah
- Sakit perut
- Demam
- Septicaemia
- Makan daging
```

---

### 2. Gejala Menengah

Gejala menengah adalah penghubung antara:

* Diagnosa
* Gejala awal (input user)

Contoh:

```
Mencret → [Buang air besar, Berak encer, Lesu, Tidak selera makan]
```

---

### 3. Gejala Awal

Gejala awal adalah input yang dipilih oleh pengguna, misalnya:

* Buang air besar lebih dari 2 kali
* Mual dan muntah
* Pusing
* Memakan makanan tertentu

---

## Mekanisme Rule-Based

Sistem menggunakan pendekatan **hierarchical rule-based**, dengan struktur:

```text
Diagnosa
   ↓
Gejala Menengah
   ↓
Gejala Awal
```

### Cara Rule Bekerja:

1. Sistem memeriksa setiap diagnosa
2. Untuk setiap diagnosa:

   * Iterasi semua gejala menengah
3. Untuk setiap gejala menengah:

   * Dicek apakah gejala awal yang terkait dipilih user
4. Jika cocok:

   * Nilai ditambahkan ke skor diagnosa

---

## Perhitungan Persentase

Persentase dihitung menggunakan rumus:

* Setiap diagnosa memiliki bobot total = 100%
* Bobot dibagi rata ke jumlah gejala menengah

Contoh:
Jika ada 5 gejala menengah:

```
Bobot tiap gejala menengah = 100 / 5 = 20%
```

Kemudian:

```
Persentase = (jumlah gejala cocok / total gejala) × bobot
```

Total akhir adalah akumulasi seluruh gejala menengah.

## Kesimpulan

Sistem pakar ini mampu memberikan diagnosa awal penyakit gastro usus dengan pendekatan rule-based yang sistematis dan terstruktur. Dengan memanfaatkan hubungan antara gejala awal, gejala menengah, dan diagnosa, sistem dapat menghasilkan persentase kemungkinan penyakit secara logis dan transparan.
