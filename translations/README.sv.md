> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

En GitHub Action som automatiskt översätter din `README.md` till flera språk med hjälp av Gemini API. Den injicerar på ett smart sätt en korslänkad språkmeny i alla filer och skapar automatiskt en commit med ändringarna.

## 🚀 Funktioner
* **Stöd för flera språk:** Generera README-filer för flera språk i en och samma körning.
* **Autonavigering:** Infogar och underhåller automatiskt en standardmeny för språkbyte högst upp i dina filer (kan inaktiveras). AI:n formaterar den automatiskt!
* **Anpassad stil:** Du kan ange en anpassad formatparameter för menyn så att AI:n utformar språkväljaren exakt som du vill ha den.
* **Spårning av tokens:** Returnerar statistik över Gemini-tokenanvändning.

## 🛠 Användning

Skapa en arbetsflödesfil (t.ex. `.github/workflows/translate.yml`):

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

## 📥 Indata

| Indata | Krävs | Standard | Beskrivning |
| --- | --- | --- | --- |
| `api_key` | Ja |  | Din Google Gemini API-nyckel. |
| `github_token` | Ja |  | Standard GitHub-token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ja |  | Kommaseparerade målspråk (t.ex. `ru, es`). |
| `output_dir` | Nej | | Katalog för att spara översatta filer. Standard är källfilens katalog. |
| `add_language_menu` | Nej | `true` | Sätt till `false` för att inaktivera automatisk generering av språkmenyn. |
| `menu_style` | Nej | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referensstilen som AI:n använder när den genererar en ny språkmeny. |
| `commit_message` | Nej | `docs: auto-translate README via Gemini` | Text som används för git-commitmeddelandet. |
| `model` | Nej | `gemini-3.1-pro-preview` | Gemini-modellen som ska användas. |
| `source_file` | Nej | `README.md` | Basfilen som ska översättas. |

## 📤 Utdata

| Utdata | Beskrivning |
| --- | --- |
| `total_tokens_used` | Totalt antal tokens som behandlats. |
| `input_tokens_used` | Antal tokens i inmatningsprompterna (input). |
| `output_tokens_used` | Antal tokens som genererats i svaren. |
| `duration_seconds` | Total bearbetningstid i sekunder. |

## 🔑 Så här skaffar du en Google Gemini API-nyckel

För att använda denna Action behöver du en gratis API-nyckel från Google AI Studio:

1. Gå till [Google AI Studio](https://aistudio.google.com/).
2. Logga in med ditt Google-konto.
3. I den vänstra navigeringsmenyn klickar du på **Get API key**.
4. Klicka på knappen **Create API key**.
5. Kopiera den genererade nyckeln.
6. Gå till ditt GitHub-repository -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klicka på **New repository secret**, namnge den `GEMINI_API_KEY`, klistra in din nyckel i Secret-fältet och spara.

## 🔑 Så här konfigurerar du standard-GitHub-token

Denna Action använder den inbyggda `GITHUB_TOKEN` för att checka in (push commits). Du behöver **inte** skapa en Personal Access Token (PAT) manuellt, men du **måste** se till att standardtoken har rätt behörigheter:

1. Gå till ditt repositorys **Settings** -> **Actions** -> **General**.
2. Rulla ner till sektionen **Workflow permissions**.
3. Välj **Read and write permissions**.
4. Klicka på **Save**.
5. I din YAML för arbetsflödet, skicka helt enkelt med `${{ secrets.GITHUB_TOKEN }}` till indata-fältet `github_token` (som visas i användningsexemplet).

## 📄 Licens

Detta projekt är licensierat under MIT-licensen – se filen [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) för mer information.