# DocRank: Aplikasi Temu Balik Informasi dengan BM25

**DocRank** adalah aplikasi berbasis web yang dirancang untuk melakukan temu balik informasi (information retrieval) pada dokumen bertema **pengobatan dan kesehatan herbal**. Aplikasi ini menggunakan metode **BM25** untuk menghitung relevansi dokumen terhadap query pengguna.

## Fitur Utama
1. **Proses Ekstraksi dan Preprocessing Dokumen**
   - Mendukung berbagai format dokumen: `.txt`, `.docx`, dan `.pdf`.
   - Tokenizing, stop word removal, dan stemming untuk menghasilkan kata dasar.

2. **Sistem Pencarian yang Efisien**
   - Menggunakan metode **BM25** untuk menghitung skor relevansi dokumen.
   - Menampilkan daftar dokumen yang relevan berdasarkan query pengguna.

3. **Antarmuka Pengguna Sederhana**
   - User-friendly interface untuk memudahkan pengguna melakukan pencarian.

## Teknologi yang Digunakan
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, dan JavaScript
- **Metode Information Retrieval**: BM25

## Instalasi Library yang Dibutuhkan
Untuk menjalankan aplikasi ini, Anda perlu menginstal library berikut. Jalankan perintah berikut di terminal atau command prompt Anda:
```bash
pip install flask
pip install sastrawi
pip install PyPDF2
pip install python-docx
pip install rank-bm25
```

## Cara Menjalankan
1. **Clone Repository**
   ```bash
   git clone https://github.com/bangaji313/DocRank-IR-Project.git
   ```
   **Masuk ke Folder Proyek**
   ```bash
   cd DocRank-IR-Project
   ```
2. **Jalankan Aplikasi**
   ```bash
   python app.py
   ```

## Cara Menggunakan
1. **Unggah Dokumen**
   Pastikan semua dokumen berada di folder DATASET dengan subfolder PDF, DOCX, dan TXT.
2. **Ekstrak Konten ke JSON**
   - Jalankan file `ekstrak-to-json.py` untuk mengekstrak konten dokumen dan melakukan preprocessing
   - Proses ini akan menghasilkan file `processed_documents-2.json` di dalam folder proyek.
3. **Lakukan Pencarian**
   - Masukkan query pencarian di halaman utama aplikasi.
   - Klik tombol "Cari" untuk melihat hasil pencarian.
   - Aplikasi akan menampilkan daftar dokumen yang relevan dengan skor relevansi.

## Rencana Pengembangan ke Depan
- Dukungan untuk pencarian berbasis gambar atau suara.
- Implementasi pencarian berbasis semantik untuk hasil yang lebih mendalam.

## Kontribusi
1. **Fork Repository**
   Klik tombol "Fork" di bagian atas repository ini untuk membuat salinan ke akun GitHub Anda.
2. **Clone Fork**
   ```bash
   git clone https://github.com/your-username/DocRank-IR-Project.git
   ```
3. **Buat Branch Baru**
   Buat branch untuk fitur atau perbaikan yang ingin Anda tambahkan
   ```bash
   git checkout -b nama-fitur-atau-perbaikan
   ```
4. **Commit Perubahan Anda**
   ```bash
   git commit -m "Menambahkan fitur atau perbaikan tertentu"
   ```
5. **Push Ke Branch Anda**
   ```bash
   git push origin nama-fitur-atau-perbaikan
   ```
6. **Ajukan PULL Request**
   Kunjungi halaman repository asli dan ajukan pull request untuk menggabungkan perubahan Anda.

## Terima kasih telah menggunakan dan mendukung proyek DocRank!
