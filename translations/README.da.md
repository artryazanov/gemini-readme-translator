> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

En GitHub Action, der automatisk oversætter din `README.md` til flere sprog ved hjælp af Gemini API'et. Den indsætter intelligent en krydslinket sprognavigationsmenu i alle filer og committer automatisk ændringerne.

## 🚀 Funktioner
* **Understøttelse af Flere Sprog:** Generer README'er på flere sprog i en enkelt kørsel.
* **Auto-Navigation:** Indsætter og vedligeholder automatisk en standard sprogskiftemenu øverst i dine filer (kan deaktiveres). AI styler den automatisk!
* **Brugerdefineret Styling:** Du kan angive en brugerdefineret menustil-parameter, så AI'en formaterer sprogskifteren præcis, som du vil have den.
* **Token-Sporing:** Udskriver statistik for brug af Gemini-tokens.

## 🛠 Brug

Opret en workflow-fil (f.eks. `.github/workflows/translate.yml`):

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

| Input | Påkrævet | Standard | Beskrivelse |
| --- | --- | --- | --- |
| `api_key` | Ja |  | Din Google Gemini API-nøgle. |
| `github_token` | Ja |  | Standard GitHub-token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ja |  | Kommaseparerede målsprog (f.eks. `ru, es`). |
| `output_dir` | Nej | | Mappe til at gemme oversatte filer. Standard er kildefilens mappe. |
| `add_language_menu` | Nej | `true` | Sæt til `false` for at deaktivere autogenerering af sprogmenuen. |
| `menu_style` | Nej | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Den referencestil, AI'en bruger, når den genererer en ny sprogmenu. |
| `commit_message` | Nej | `docs: auto-translate README via Gemini` | Tekst, der bruges til git commit-beskeden. |
| `model` | Nej | `gemini-3.1-pro-preview` | Den Gemini-model, der skal bruges. |
| `source_file` | Nej | `README.md` | Basisfilen, der skal oversættes. |

## 📤 Output

| Output | Beskrivelse |
| --- | --- |
| `total_tokens_used` | Samlet antal tokens behandlet. |
| `input_tokens_used` | Antal tokens i input-prompts. |
| `output_tokens_used` | Antal tokens genereret i svarene. |
| `duration_seconds` | Samlet behandlingstid i sekunder. |

## 🔑 Sådan får du en Google Gemini API-nøgle

For at bruge denne action, har du brug for en gratis API-nøgle fra Google AI Studio:

1. Gå til [Google AI Studio](https://aistudio.google.com/).
2. Log ind med din Google-konto.
3. I den venstre navigationsmenu, klik på **Get API key**.
4. Klik på knappen **Create API key**.
5. Kopiér den genererede nøgle.
6. Gå til dit GitHub-repository -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klik på **New repository secret**, navngiv den `GEMINI_API_KEY`, indsæt din nøgle i feltet Secret, og gem.

## 🔑 Sådan konfigurerer du Standard GitHub Token

Denne action bruger det indbyggede `GITHUB_TOKEN` til at pushe commits. Du behøver **ikke** at oprette en Personal Access Token (PAT) manuelt, men du **skal** sikre dig, at standardtokenet har de korrekte tilladelser:

1. Gå til dit repositorys **Settings** -> **Actions** -> **General**.
2. Rul ned til afsnittet **Workflow permissions**.
3. Vælg **Read and write permissions**.
4. Klik på **Save**.
5. I din workflow YAML skal du blot angive `${{ secrets.GITHUB_TOKEN }}` til inputtet `github_token` (som vist i brugseksemplet).

## 📄 Licens

Dette projekt er licenseret under MIT-licensen - se filen [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) for detaljer.