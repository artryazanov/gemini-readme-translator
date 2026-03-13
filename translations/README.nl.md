> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Een GitHub Action die je `README.md` automatisch naar meerdere talen vertaalt met behulp van de Gemini API. Het injecteert op intelligente wijze een cross-linked taalnavigatiemenu in alle bestanden en commit de wijzigingen automatisch.

## 🚀 Functies
* **Meertalige Ondersteuning:** Genereer README's voor meerdere talen in één run.
* **Auto-Navigatie:** Voegt automatisch een standaard taalwisselmenu bovenaan je bestanden in en onderhoudt dit (kan worden uitgeschakeld). AI stijlt dit automatisch!
* **Aangepaste Stijlen:** Je kunt een parameter voor een aangepaste menustijl opgeven, zodat de AI de taalwisselaar precies opmaakt zoals jij wilt.
* **Token Tracking:** Voert statistieken uit over het Gemini-tokengebruik.

## 🛠 Gebruik

Maak een workflowbestand aan (bijv. `.github/workflows/translate.yml`):

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

## 📥 Inputs

| Input | Vereist | Standaard | Beschrijving |
| --- | --- | --- | --- |
| `api_key` | Ja |  | Jouw Google Gemini API-sleutel. |
| `github_token` | Ja |  | Standaard GitHub-token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ja |  | Kommagescheiden doeltalen (bijv. `ru, es`). |
| `output_dir` | Nee | | Map om vertaalde bestanden op te slaan. Standaard is dit de map van het bronbestand. |
| `add_language_menu` | Nee | `true` | Stel in op `false` om het automatisch genereren van het taalmenu uit te schakelen. |
| `menu_style` | Nee | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | De referentiestijl die de AI gebruikt bij het genereren van een nieuw taalmenu. |
| `commit_message` | Nee | `docs: auto-translate README via Gemini` | Tekst die wordt gebruikt voor de git commit-message. |
| `model` | Nee | `gemini-3.1-pro-preview` | Het te gebruiken Gemini-model. |
| `source_file` | Nee | `README.md` | Het basisbestand om te vertalen. |

## 📤 Outputs

| Output | Beschrijving |
| --- | --- |
| `total_tokens_used` | Totaal aantal verwerkte tokens. |
| `input_tokens_used` | Aantal tokens in de input prompts. |
| `output_tokens_used` | Aantal tokens gegenereerd in de reacties. |
| `duration_seconds` | Totale verwerkingstijd in seconden. |

## 🔑 Hoe krijg je een Google Gemini API-sleutel

Om deze action te gebruiken, heb je een gratis API-sleutel nodig van Google AI Studio:

1. Ga naar [Google AI Studio](https://aistudio.google.com/).
2. Log in met je Google-account.
3. Klik in het linkernavigatiemenu op **Get API key**.
4. Klik op de knop **Create API key**.
5. Kopieer de gegenereerde sleutel.
6. Ga naar je GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klik op **New repository secret**, noem het `GEMINI_API_KEY`, plak je sleutel in het Secret veld en sla op.

## 🔑 Hoe configureer je de Standaard GitHub Token

Deze action gebruikt de ingebouwde `GITHUB_TOKEN` om commits te pushen. Je hoeft **geen** Personal Access Token (PAT) handmatig aan te maken, maar je **moet** er wel voor zorgen dat de standaard token de juiste rechten heeft:

1. Ga naar je repository **Settings** -> **Actions** -> **General**.
2. Scroll naar beneden naar de sectie **Workflow permissions**.
3. Selecteer **Read and write permissions**.
4. Klik op **Save**.
5. Geef in je workflow YAML simpelweg `${{ secrets.GITHUB_TOKEN }}` door aan de `github_token` input (zoals weergegeven in het gebruiksvoorbeeld).

## 📄 Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) bestand voor details.