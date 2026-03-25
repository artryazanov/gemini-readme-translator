> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action koja automatski prevodi vaš `README.md` na više jezika koristeći Gemini API. Pametno ubacuje međusobno povezan navigacioni meni za jezike u sve datoteke i automatski komituje promene.

## 🚀 Funkcionalnosti
* **Višejezična podrška:** Generiše README datoteke za više jezika u jednom pokretanju.
* **Auto-navigacija:** Automatski ubacuje i održava standardni meni za promenu jezika na vrhu vaših datoteka (može se isključiti). Veštačka inteligencija (AI) ga automatski stilizuje!
* **Prilagođeno stilizovanje:** Možete proslediti parametar za prilagođeni stil menija kako bi AI formatirao meni za izbor jezika tačno onako kako želite.
* **Praćenje tokena:** Prikazuje statistiku korišćenja Gemini tokena.

## 🛠 Korišćenje

Kreirajte workflow datoteku (npr. `.github/workflows/translate.yml`):

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

## 📥 Ulazni parametri

| Ulazni parametar | Obavezno | Podrazumevano | Opis |
| --- | --- | --- | --- |
| `api_key` | Da |  | Vaš Google Gemini API ključ. |
| `github_token` | Da |  | Standardni GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Da |  | Ciljni jezici razdvojeni zarezom (npr. `ru, es`). |
| `output_dir` | Ne | | Direktorijum za čuvanje prevedenih datoteka. Podrazumevano je to direktorijum izvorne datoteke. |
| `add_language_menu` | Ne | `true` | Postavite na `false` da onemogućite automatsko generisanje jezičkog menija. |
| `use_absolute_links`| Ne | `true` | Поставите на `false` да бисте користили релативне везе уместо апсолутних ГитХуб URL-ова у генерисаним менијима језика. |
| `menu_style` | Ne | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referentni stil koji AI koristi prilikom generisanja novog jezičkog menija. |
| `commit_message` | Ne | `docs: auto-translate README via Gemini` | Tekst koji se koristi za git commit poruku. |
| `model` | Ne | `gemini-3.1-pro-preview` | Gemini model koji se koristi. |
| `source_file` | Ne | `README.md` | Osnovna datoteka koja se prevodi. |

## 📤 Izlazni parametri

| Izlazni parametar | Opis |
| --- | --- |
| `total_tokens_used` | Ukupan broj obrađenih tokena. |
| `input_tokens_used` | Broj tokena u ulaznim promptovima. |
| `output_tokens_used` | Broj generisanih tokena u odgovorima. |
| `duration_seconds` | Ukupno vreme obrade u sekundama. |

## 🔑 Kako dobiti Google Gemini API ključ

Da biste koristili ovu akciju, potreban vam je besplatan API ključ iz Google AI Studija:

1. Idite na [Google AI Studio](https://aistudio.google.com/).
2. Prijavite se svojim Google nalogom.
3. U levom navigacionom meniju kliknite na **Get API key**.
4. Kliknite na dugme **Create API key**.
5. Kopirajte generisani ključ.
6. Idite na vaš GitHub repozitorijum -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Kliknite na **New repository secret**, nazovite ga `GEMINI_API_KEY`, nalepite svoj ključ u polje Secret i sačuvajte.

## 🔑 Kako konfigurisati standardni GitHub Token

Ova akcija koristi ugrađeni `GITHUB_TOKEN` za postavljanje (push) komitova. **Ne morate** ručno kreirati Personal Access Token (PAT), ali se **morate** pobrinuti da podrazumevani token ima ispravne dozvole:

1. Idite na **Settings** vašeg repozitorijuma -> **Actions** -> **General**.
2. Skrolujte dole do sekcije **Workflow permissions**.
3. Izaberite **Read and write permissions**.
4. Kliknite na **Save**.
5. U vašem workflow YAML fajlu, jednostavno prosledite `${{ secrets.GITHUB_TOKEN }}` u `github_token` ulaz (kao što je prikazano u primeru korišćenja).

## 📄 Licenca

Ovaj projekat je licenciran pod MIT Licencom - pogledajte datoteku [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) za detalje.