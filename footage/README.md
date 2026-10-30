# Footage

Folder ini untuk paket video. Buat satu subfolder per paket, misalnya `footage/pack-01-aktivitas-sosial/`.

## Batas ukuran GitHub

- File di atas **50 MB** memunculkan peringatan, dan file di atas **100 MB** ditolak saat push.
- Total repo sebaiknya di bawah 1–5 GB supaya tetap cepat di-clone.

## Cara menyimpan footage

| Ukuran file | Simpan di |
|---|---|
| Di bawah 50 MB (klip pendek, preview) | Langsung di folder `footage/pack-NN-nama/` |
| Di atas 50 MB (master, 4K) | **GitHub Releases**: buat release baru, unggah file sebagai *asset* (maks 2 GB per file), lalu taruh tautannya di `footage/pack-NN-nama/README.md` |

Releases gratis dan tidak dihitung ke ukuran repo, jadi cocok untuk footage resolusi penuh. Simpan juga thumbnail (JPG/GIF kecil) di folder paket supaya pengunjung bisa melihat isinya sebelum mengunduh.
