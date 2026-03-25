> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Egy GitHub Action, amely automatikusan lefordítja a `README.md` fájlokat több nyelvre a Gemini API használatával. Intelligensen beilleszt egy keresztlinkelt nyelvi navigációs menüt minden fájlba, és automatikusan véglegesíti (commit) a változtatásokat.

## 🚀 Funkciók
* **Többnyelvű támogatás:** README fájlok generálása több nyelvre egyetlen futtatással.
* **Automatikus navigáció:** Automatikusan beilleszt és karbantart egy szabványos nyelvválasztó menüt a fájlok tetején (kikapcsolható). Az MI automatikusan formázza!
* **Egyéni formázás:** Megadhatsz egy egyéni menüstílus-paramétert, így az MI pontosan úgy formázza a nyelvválasztót, ahogyan szeretnéd.
* **Tokenkövetés:** Kiírja a Gemini tokenhasználati statisztikáit.

## 🛠 Használat

Hozz létre egy workflow fájlt (pl. `.github/workflows/translate.yml`):

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

## 📥 Bemenetek (Inputs)

| Bemenet | Kötelező | Alapértelmezett | Leírás |
| --- | --- | --- | --- |
| `api_key` | Igen |  | A Google Gemini API kulcsod. |
| `github_token` | Igen |  | Szabványos GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Igen |  | Vesszővel elválasztott célnyelvek (pl. `ru, es`). |
| `output_dir` | Nem | | Könyvtár a lefordított fájlok mentéséhez. Alapértelmezés szerint a forrásfájl könyvtára. |
| `add_language_menu` | Nem | `true` | Állítsd `false`-ra a nyelvi menü automatikus generálásának letiltásához. |
| `use_absolute_links`| Nem | `true` | Állítsa `false` értékre a relatív hivatkozások használatához a generált nyelvi menükben a teljes GitHub URL-ek helyett. |
| `menu_style` | Nem | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | A referenciastílus, amelyet az MI használ az új nyelvi menü generálásakor. |
| `commit_message` | Nem | `docs: auto-translate README via Gemini` | A git commit üzenethez használt szöveg. |
| `model` | Nem | `gemini-3.1-pro-preview` | A használni kívánt Gemini modell. |
| `source_file` | Nem | `README.md` | A fordítandó alapfájl. |

## 📤 Kimenetek (Outputs)

| Kimenet | Leírás |
| --- | --- |
| `total_tokens_used` | A feldolgozott tokenek teljes száma. |
| `input_tokens_used` | A bemeneti promptok tokenszáma. |
| `output_tokens_used` | A válaszokban generált tokenek száma. |
| `duration_seconds` | Teljes feldolgozási idő másodpercben. |

## 🔑 Hogyan szerezz Google Gemini API kulcsot

A művelet (action) használatához szükséged lesz egy ingyenes API kulcsra a Google AI Studio-ból:

1. Látogass el a [Google AI Studio](https://aistudio.google.com/) oldalára.
2. Jelentkezz be a Google-fiókoddal.
3. A bal oldali navigációs menüben kattints a **Get API key** gombra.
4. Kattints a **Create API key** gombra.
5. Másold ki a generált kulcsot.
6. Menj a GitHub tárolód (repository) -> **Settings** -> **Secrets and variables** -> **Actions** menüpontjába.
7. Kattints a **New repository secret** gombra, nevezd el `GEMINI_API_KEY`-nek, illeszd be a kulcsot a Secret mezőbe, majd mentsd el.

## 🔑 A szabványos GitHub Token konfigurálása

Ez a művelet a beépített `GITHUB_TOKEN`-t használja a commitok pusholásához. **Nem** kell manuálisan Personal Access Token-t (PAT) létrehoznod, de **gondoskodnod kell** arról, hogy az alapértelmezett token megfelelő jogosultságokkal rendelkezzen:

1. Menj a tárolód **Settings** -> **Actions** -> **General** menüpontjába.
2. Görgess le a **Workflow permissions** szekcióhoz.
3. Válaszd ki a **Read and write permissions** lehetőséget.
4. Kattints a **Save** gombra.
5. A workflow YAML fájlodban egyszerűen add át a `${{ secrets.GITHUB_TOKEN }}` értéket a `github_token` bemenetnek (ahogy a használati példában is látható).

## 📄 Licenc

Ez a projekt az MIT Licenc alatt áll - a részletekért lásd a [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) fájlt.