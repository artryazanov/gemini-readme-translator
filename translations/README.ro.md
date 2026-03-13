> 🌐 **Languages:** [English](README.md) | [English (en)](translations/README.en.md) | [Русский](translations/README.ru.md) | [ไทย](translations/README.th.md) | [简体中文](translations/README.zh-CN.md) | [繁體中文](translations/README.zh-TW.md) | [हिन्दी](translations/README.hi.md) | [Español](translations/README.es.md) | [Français](translations/README.fr.md) | [العربية](translations/README.ar.md) | [বাংলা](translations/README.bn.md) | [Português](translations/README.pt.md) | [اردو](translations/README.ur.md) | [Bahasa Indonesia](translations/README.id.md) | [Deutsch](translations/README.de.md) | [日本語](translations/README.ja.md) | [मराठी](translations/README.mr.md) | [తెలుగు](translations/README.te.md) | [Türkçe](translations/README.tr.md) | [தமிழ்](translations/README.ta.md) | [Tiếng Việt](translations/README.vi.md) | [한국어](translations/README.ko.md) | [Kiswahili](translations/README.sw.md) | [Italiano](translations/README.it.md) | [ગુજરાતી](translations/README.gu.md) | [فارسی](translations/README.fa.md) | [ಕನ್ನಡ](translations/README.kn.md) | [Polski](translations/README.pl.md) | [മലയാളം](translations/README.ml.md) | [Українська](translations/README.uk.md) | [Română](translations/README.ro.md) | [Nederlands](translations/README.nl.md) | [Ελληνικά](translations/README.el.md) | [Magyar](translations/README.hu.md) | [Svenska](translations/README.sv.md) | [Čeština](translations/README.cs.md) | [Српски](translations/README.sr.md) | [עברית](translations/README.he.md) | [Български](translations/README.bg.md) | [Dansk](translations/README.da.md) | [Suomi](translations/README.fi.md) | [Norsk](translations/README.no.md) | [Slovenčina](translations/README.sk.md) | [Hrvatski](translations/README.hr.md) | [Lietuvių](translations/README.lt.md) | [Slovenščina](translations/README.sl.md) | [Latviešu](translations/README.lv.md) | [Eesti](translations/README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

O acțiune GitHub (GitHub Action) care vă traduce automat fișierul `README.md` în mai multe limbi folosind API-ul Gemini. Injectează inteligent un meniu de navigare între limbi, cu linkuri încrucișate, în toate fișierele și poate fie să facă commit modificărilor direct, fie să creeze un Pull Request pentru revizuire.

## 🚀 Caracteristici
* **Suport multi-lingvistic:** Generează fișiere README pentru mai multe limbi într-o singură rulare.
* **Auto-Navigare:** Inserează și menține automat un meniu standard de comutare a limbii în partea de sus a fișierelor (poate fi dezactivat). AI-ul îl stilizează automat!
* **Stilizare personalizată:** Puteți furniza un parametru personalizat pentru stilul meniului, astfel încât AI-ul să formateze comutatorul de limbă exact așa cum doriți.
* **Urmărire token-uri:** Afișează statistici privind utilizarea token-urilor Gemini.

## 🛠 Utilizare

Creați un fișier de flux de lucru (workflow) (de exemplu, `.github/workflows/translate.yml`):

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
        uses: artryazanov/gemini-readme-translator@v1
        with:
          api_key: ${{ secrets.GEMINI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          languages: 'ru, zh-CN, es'
          add_language_menu: 'true'
          menu_style: '> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md)'

```

## 📥 Parametri de intrare

| Parametru | Necesar | Implicit | Descriere |
| --- | --- | --- | --- |
| `api_key` | Da |  | Cheia dumneavoastră API Google Gemini. |
| `github_token` | Da |  | Token-ul standard GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Da |  | Limbile țintă separate prin virgulă (de exemplu, `ru, es`). |
| `output_dir` | Nu | | Directorul în care se salvează fișierele traduse. Implicit este directorul fișierului sursă. |
| `add_language_menu` | Nu | `true` | Setați la `false` pentru a dezactiva generarea automată a meniului de limbă. |
| `menu_style` | Nu | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Stilul de referință pe care AI-ul îl folosește la generarea unui nou meniu de limbă. |
| `commit_message` | Nu | `docs: auto-translate README via Gemini` | Textul folosit pentru mesajul de commit git. |
| `model` | Nu | `gemini-3.1-pro-preview` | Modelul Gemini care va fi utilizat. |
| `source_file` | Nu | `README.md` | Fișierul de bază care va fi tradus. |

## 🔑 Cum să obțineți o cheie API Google Gemini

Pentru a utiliza această acțiune, aveți nevoie de o cheie API gratuită de la Google AI Studio:

1. Accesați [Google AI Studio](https://aistudio.google.com/).
2. Conectați-vă cu contul dumneavoastră Google.
3. În meniul de navigare din stânga, faceți clic pe **Get API key** (Obțineți cheia API).
4. Faceți clic pe butonul **Create API key** (Creați cheia API).
5. Copiați cheia generată.
6. Accesați depozitul (repository) dumneavoastră GitHub -> **Settings** (Setări) -> **Secrets and variables** (Secrete și variabile) -> **Actions** (Acțiuni).
7. Faceți clic pe **New repository secret** (Secret nou pentru depozit), denumiți-l `GEMINI_API_KEY`, inserați cheia în câmpul Secret și salvați.

## 🔑 Cum să configurați token-ul standard GitHub

Această acțiune utilizează `GITHUB_TOKEN` încorporat pentru a împinge (push) commit-uri sau pentru a crea Pull Request-uri. **Nu** este nevoie să creați manual un Personal Access Token (PAT), dar **trebuie** să vă asigurați că token-ul implicit are permisiunile corecte:

1. Accesați **Settings** (Setări) -> **Actions** (Acțiuni) -> **General** din depozitul dumneavoastră.
2. Derulați în jos până la secțiunea **Workflow permissions** (Permisiuni flux de lucru).
3. Selectați **Read and write permissions** (Permisiuni de citire și scriere).
4. Faceți clic pe **Save** (Salvare).
5. În fișierul dumneavoastră YAML pentru fluxul de lucru, pur și simplu transmiteți `${{ secrets.GITHUB_TOKEN }}` către parametrul `github_token` (așa cum se arată în exemplul de utilizare).

## 📄 Licență

Acest proiect este licențiat sub licența MIT - consultați fișierul [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) pentru detalii.