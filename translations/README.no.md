> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

En GitHub Action som automatisk oversetter din `README.md` til flere språk ved hjelp av Gemini API. Den injiserer intelligent en krysslenket språknavigasjonsmeny i alle filer og legger automatisk inn (commits) endringene.

## 🚀 Funksjoner
* **Flerspråklig støtte:** Generer README-filer for flere språk i én enkelt kjøring.
* **Auto-navigasjon:** Setter automatisk inn og vedlikeholder en standard meny for språkvalg øverst i filene dine (kan deaktiveres). KI-en tilpasser stilen automatisk!
* **Egendefinert stil:** Du kan oppgi en parameter for egendefinert menystil slik at KI-en formaterer språkvelgeren nøyaktig slik du ønsker.
* **Token-sporing:** Skriver ut statistikk for bruk av Gemini-tokens.

## 🛠 Bruk

Opprett en arbeidsflytfil (for eksempel `.github/workflows/translate.yml`):

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

## 📥 Inndata

| Inndata | Påkrevd | Standard | Beskrivelse |
| --- | --- | --- | --- |
| `api_key` | Ja |  | Din Google Gemini API-nøkkel. |
| `github_token` | Ja |  | Standard GitHub-token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ja |  | Kommaseparerte målspråk (f.eks. `ru, es`). |
| `output_dir` | Nei | | Mappe for å lagre oversatte filer. Standard er kildefilens mappe. |
| `add_language_menu` | Nei | `true` | Sett til `false` for å deaktivere automatisk generering av språkmeny. |
| `use_absolute_links`| Nei | `true` | Sett til `false` for å bruke relative lenker i stedet for absolutte GitHub-URL-er i de genererte språkmenyene. |
| `menu_style` | Nei | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referansestilen KI-en bruker ved generering av en ny språkmeny. |
| `commit_message` | Nei | `docs: auto-translate README via Gemini` | Tekst som brukes til git commit-meldingen. |
| `model` | Nei | `gemini-3.1-pro-preview` | Gemini-modellen som skal brukes. |
| `source_file` | Nei | `README.md` | Grunnfilen som skal oversettes. |

## 📤 Utdata

| Utdata | Beskrivelse |
| --- | --- |
| `total_tokens_used` | Totalt antall tokens behandlet. |
| `input_tokens_used` | Antall tokens i inndata-forespørslene (input prompts). |
| `output_tokens_used` | Antall tokens generert i responsene. |
| `duration_seconds` | Total behandlingstid i sekunder. |

## 🔑 Hvordan få en Google Gemini API-nøkkel

For å bruke denne handlingen (action), trenger du en gratis API-nøkkel fra Google AI Studio:

1. Gå til [Google AI Studio](https://aistudio.google.com/).
2. Logg inn med din Google-konto.
3. I den venstre navigasjonsmenyen, klikk på **Get API key**.
4. Klikk på knappen **Create API key**.
5. Kopier den genererte nøkkelen.
6. Gå til ditt GitHub-repositorium -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klikk på **New repository secret**, gi den navnet `GEMINI_API_KEY`, lim inn nøkkelen i Secret-feltet, og lagre.

## 🔑 Hvordan konfigurere standard GitHub Token

Denne handlingen bruker den innebygde `GITHUB_TOKEN` for å pushe commits. Du trenger **ikke** å opprette en Personal Access Token (PAT) manuelt, men du **må** sørge for at standard-tokenet har de riktige tillatelsene:

1. Gå til **Settings** -> **Actions** -> **General** i repositoriet ditt.
2. Rull ned til delen for **Workflow permissions**.
3. Velg **Read and write permissions**.
4. Klikk på **Save**.
5. I arbeidsflyt-YAML-filen din, angir du ganske enkelt `${{ secrets.GITHUB_TOKEN }}` for `github_token` inndataen (som vist i brukseksempelet).

## 📄 Lisens

Dette prosjektet er lisensiert under MIT-lisensen - se [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE)-filen for detaljer.