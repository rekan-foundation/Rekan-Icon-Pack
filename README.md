# Rekan Icon Pack

Koleksi icon dan footage gratis dari **Rekan Foundation** untuk lembaga sosial, kreator konten, dan developer. Pakai untuk presentasi, website, aplikasi, atau video, termasuk proyek komersial.

## Daftar paket

<!-- PACKS:START -->
### Icon

| Paket | Jumlah | Galeri |
|---|---|---|
| Flat Color 512 | 300 | [lihat](icons/pack-01-flat-color-512/README.md) |

### Footage

Belum ada. Lihat [footage/README.md](footage/README.md) untuk cara menambah.
<!-- PACKS:END -->

## Cara pakai

**Unduh semua:** klik tombol hijau **Code → Download ZIP** di atas.

**Unduh satu icon:** buka file SVG-nya, lalu klik tombol **Download raw file**.

**Tautkan langsung di web** (lewat CDN jsDelivr):

```html
<img src="https://cdn.jsdelivr.net/gh/rekan-foundation/Rekan-Icon-Pack@main/icons/pack-01-flat-color-512/idea.svg" width="64" alt="Ide">
```

Daftar lengkap file ada di [`manifest.json`](manifest.json).

## Struktur repo

```
icons/
  pack-01-flat-color-512/   ← satu folder per paket
    pack.json               ← judul, deskripsi, ukuran
    README.md               ← galeri (dibuat otomatis)
    *.svg
footage/                    ← video, lihat footage/README.md
scripts/build_index.py      ← memperbarui galeri & manifest
```

## Menambah paket baru

1. Buat folder `icons/pack-NN-nama-paket/` (nomor urut berikutnya).
2. Masukkan file SVG/PNG. Nama file huruf kecil dengan tanda hubung, misalnya `alarm-clock.svg`.
3. Tambahkan `pack.json` berisi `title`, `description`, dan `size`.
4. Jalankan `python scripts/build_index.py` untuk memperbarui galeri dan manifest.
5. Commit dan push: `git add . && git commit -m "feat(icons): tambah pack-NN" && git push`.

## Lisensi

[CC BY 4.0](LICENSE). Bebas dipakai, diubah, dan dibagikan, termasuk untuk komersial, dengan mencantumkan kredit:

> Icon oleh Rekan Foundation — github.com/rekan-foundation/Rekan-Icon-Pack

Dilarang menjual ulang icon ini sebagai paket icon atau mengklaimnya sebagai karya sendiri.
