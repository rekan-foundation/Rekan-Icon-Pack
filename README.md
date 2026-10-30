# Rekan Icon Pack

Koleksi icon dan footage gratis dari **Rekan Foundation** untuk lembaga sosial, kreator konten, dan developer. Pakai untuk presentasi, website, aplikasi, atau video, termasuk proyek komersial.

## Daftar paket

<!-- PACKS:START -->
### Icon

| Paket | Jumlah | Galeri |
|---|---|---|
| Flat Color 512 | 300 | [lihat](icons/pack-01-flat-color-512/README.md) |
| Nusa Animals | 186 | [lihat](icons/pack-02-nusa-animals/README.md) |
| Nusa Buildings Construction | 417 | [lihat](icons/pack-03-nusa-buildings-construction/README.md) |
| Nusa Business Office | 571 | [lihat](icons/pack-04-nusa-business-office/README.md) |
| Nusa Celebration Culture | 431 | [lihat](icons/pack-05-nusa-celebration-culture/README.md) |
| Nusa Design Editing | 443 | [lihat](icons/pack-06-nusa-design-editing/README.md) |
| Nusa Education Science | 298 | [lihat](icons/pack-07-nusa-education-science/README.md) |
| Nusa Fashion Beauty | 744 | [lihat](icons/pack-08-nusa-fashion-beauty/README.md) |
| Nusa Files Documents | 572 | [lihat](icons/pack-09-nusa-files-documents/README.md) |
| Nusa Finance Shopping | 627 | [lihat](icons/pack-10-nusa-finance-shopping/README.md) |
| Nusa Food Drink | 890 | [lihat](icons/pack-11-nusa-food-drink/README.md) |
| Nusa Games Entertainment Toys | 360 | [lihat](icons/pack-12-nusa-games-entertainment-toys/README.md) |
| Nusa Health Medical | 423 | [lihat](icons/pack-13-nusa-health-medical/README.md) |
| Nusa Home Furniture | 463 | [lihat](icons/pack-14-nusa-home-furniture/README.md) |
| Nusa Industry Tools | 182 | [lihat](icons/pack-15-nusa-industry-tools/README.md) |
| Nusa Interface Navigation | 801 | [lihat](icons/pack-16-nusa-interface-navigation/README.md) |
| Nusa Law Security | 279 | [lihat](icons/pack-17-nusa-law-security/README.md) |
| Nusa Multimedia | 696 | [lihat](icons/pack-18-nusa-multimedia/README.md) |
| Nusa Nature Weather Environment | 658 | [lihat](icons/pack-19-nusa-nature-weather-environment/README.md) |
| Nusa People Emotions Gestures | 377 | [lihat](icons/pack-20-nusa-people-emotions-gestures/README.md) |
| Nusa Shapes Symbols | 183 | [lihat](icons/pack-21-nusa-shapes-symbols/README.md) |
| Nusa Sports Activities | 349 | [lihat](icons/pack-22-nusa-sports-activities/README.md) |
| Nusa Technology Devices | 810 | [lihat](icons/pack-23-nusa-technology-devices/README.md) |
| Nusa Transport Travel | 455 | [lihat](icons/pack-24-nusa-transport-travel/README.md) |
| Nusa Web Seo Social Media | 616 | [lihat](icons/pack-25-nusa-web-seo-social-media/README.md) |

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

Spasi pada nama file ditulis `%20` di URL:

```html
<img src="https://cdn.jsdelivr.net/gh/rekan-foundation/Rekan-Icon-Pack@main/icons/pack-02-nusa-animals/NAMA_FILE" width="64" alt="">
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
2. Masukkan file SVG/PNG. Paket Nusa memakai pola `Nusa_Nama Icon Gaya.svg`, misalnya `Nusa_Alarm Clock Flat.svg`; paket lain memakai huruf kecil dengan tanda hubung, misalnya `alarm-clock.svg`.
3. Tambahkan `pack.json` berisi `title`, `description`, dan `size`.
4. Jalankan `python scripts/build_index.py` untuk memperbarui galeri dan manifest.
5. Commit dan push: `git add . && git commit -m "feat(icons): tambah pack-NN" && git push`.

## Lisensi

[CC BY 4.0](LICENSE). Bebas dipakai, diubah, dan dibagikan, termasuk untuk komersial, dengan mencantumkan kredit:

> Icon oleh Rekan Foundation — github.com/rekan-foundation/Rekan-Icon-Pack

Dilarang menjual ulang icon ini sebagai paket icon atau mengklaimnya sebagai karya sendiri.
