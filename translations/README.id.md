> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action yang secara otomatis menerjemahkan `README.md` Anda ke berbagai bahasa menggunakan API Gemini. Action ini secara cerdas menyisipkan menu navigasi bahasa yang saling tertaut ke dalam semua file dan secara otomatis melakukan commit perubahan.

## 🚀 Fitur
* **Dukungan Multi-Bahasa:** Buat README untuk berbagai bahasa dalam satu kali proses.
* **Navigasi Otomatis:** Menyisipkan dan memelihara menu pengalih bahasa standar secara otomatis di bagian atas file Anda (dapat dinonaktifkan). AI akan menatanya secara otomatis!
* **Gaya Kustom:** Anda dapat memberikan parameter gaya menu kustom sehingga AI memformat pengalih bahasa persis seperti yang Anda inginkan.
* **Pelacakan Token:** Menampilkan output statistik penggunaan token Gemini.

## 🛠 Penggunaan

Buat file alur kerja (contoh: `.github/workflows/translate.yml`):

```yaml
name: Auto Translate README

on:
  push:
    paths:
      - 'README.md'
  workflow_dispatch:

jobs:
  translate:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Gemini README Translator
        id: translator
        uses: artryazanov/gemini-readme-translator@v1
        with:
          api_key: ${{ secrets.GEMINI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          languages: 'ru, zh-CN, es'
          add_language_menu: 'true'
          menu_style: '> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md)'

      - name: Print Translation Stats
        run: |
          echo "Process took ${{ steps.translator.outputs.duration_seconds }} seconds."
          echo "Total tokens used: ${{ steps.translator.outputs.total_tokens_used }}"
          echo "Input tokens: ${{ steps.translator.outputs.input_tokens_used }}"
          echo "Output tokens: ${{ steps.translator.outputs.output_tokens_used }}"

```

## 📥 Input

| Input | Wajib | Default | Deskripsi |
| --- | --- | --- | --- |
| `api_key` | Ya |  | Kunci API Google Gemini Anda. |
| `github_token` | Ya |  | Token GitHub standar (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ya |  | Bahasa target yang dipisahkan koma (contoh: `ru, es`). |
| `output_dir` | Tidak | | Direktori untuk menyimpan file yang diterjemahkan. Secara default menggunakan direktori file sumber. |
| `add_language_menu` | Tidak | `true` | Setel ke `false` untuk menonaktifkan pembuatan otomatis menu bahasa. |
| `menu_style` | Tidak | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Gaya referensi yang digunakan AI saat membuat menu bahasa baru. |
| `commit_message` | Tidak | `docs: auto-translate README via Gemini` | Teks yang digunakan untuk pesan git commit. |
| `model` | Tidak | `gemini-3.1-pro-preview` | Model Gemini yang akan digunakan. |
| `source_file` | Tidak | `README.md` | File dasar yang akan diterjemahkan. |

## 📤 Output

| Output | Deskripsi |
| --- | --- |
| `total_tokens_used` | Jumlah total token yang diproses. |
| `input_tokens_used` | Jumlah token dalam prompt input. |
| `output_tokens_used` | Jumlah token yang dihasilkan dalam respons. |
| `duration_seconds` | Total waktu pemrosesan dalam detik. |

## 🔑 Cara mendapatkan Kunci API Google Gemini

Untuk menggunakan action ini, Anda memerlukan kunci API gratis dari Google AI Studio:

1. Buka [Google AI Studio](https://aistudio.google.com/).
2. Masuk dengan akun Google Anda.
3. Di menu navigasi kiri, klik **Get API key**.
4. Klik tombol **Create API key**.
5. Salin kunci yang dihasilkan.
6. Buka repositori GitHub Anda -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klik **New repository secret**, beri nama `GEMINI_API_KEY`, tempel kunci Anda ke kolom Secret, lalu simpan.

## 🔑 Cara mengonfigurasi Token Standar GitHub

Action ini menggunakan `GITHUB_TOKEN` bawaan untuk melakukan push commit. Anda **tidak** perlu membuat Personal Access Token (PAT) secara manual, tetapi Anda **harus** memastikan bahwa token default memiliki izin yang benar:

1. Buka repositori Anda **Settings** -> **Actions** -> **General**.
2. Gulir ke bawah ke bagian **Workflow permissions**.
3. Pilih **Read and write permissions**.
4. Klik **Save**.
5. Di YAML alur kerja Anda, cukup teruskan `${{ secrets.GITHUB_TOKEN }}` ke input `github_token` (seperti yang ditunjukkan dalam contoh penggunaan).

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) untuk detailnya.