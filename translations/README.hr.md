> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Prevoditelj Gemini README-a


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action koji automatski prevodi vaš `README.md` na više jezika koristeći Gemini API. Pametno ubacuje međusobno povezani navigacijski izbornik za jezike u sve datoteke i automatski izvršava commit promjena.

## 🚀 Značajke
* **Višejezična podrška:** Generirajte README datoteke za više jezika u jednom pokretanju.
* **Auto-navigacija:** Automatski umeće i održava standardni izbornik za odabir jezika na vrhu vaših datoteka (može se isključiti). Umjetna inteligencija ga automatski stilizira!
* **Prilagođeno stiliziranje:** Možete proslijediti parametar za prilagođeni stil izbornika kako bi AI formatirao izbornik jezika točno onako kako želite.
* **Praćenje tokena:** Prikazuje statistiku korištenja Gemini tokena.

## 🛠 Korištenje

Napravite datoteku tijeka rada (npr. `.github/workflows/translate.yml`):

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

| Ulazni parametar | Obavezno | Zadano | Opis |
| --- | --- | --- | --- |
| `api_key` | Da |  | Vaš Google Gemini API ključ. |
| `github_token` | Da |  | Standardni GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Da |  | Ciljani jezici odvojeni zarezom (npr. `ru, es`). |
| `output_dir` | Ne | | Direktorij u koji se spremaju prevedene datoteke. Zadani direktorij je onaj izvorne datoteke. |
| `add_language_menu` | Ne | `true` | Postavite na `false` kako biste onemogućili automatsko generiranje izbornika jezika. |
| `menu_style` | Ne | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referentni stil koji AI koristi pri generiranju novog izbornika jezika. |
| `commit_message` | Ne | `docs: auto-translate README via Gemini` | Tekst koji se koristi za git commit poruku. |
| `model` | Ne | `gemini-3.1-pro-preview` | Model Gemini koji će se koristiti. |
| `source_file` | Ne | `README.md` | Osnovna datoteka za prijevod. |

## 📤 Izlazni parametri

| Izlazni parametar | Opis |
| --- | --- |
| `total_tokens_used` | Ukupan broj obrađenih tokena. |
| `input_tokens_used` | Broj tokena u ulaznim promptovima. |
| `output_tokens_used` | Broj tokena generiranih u odgovorima. |
| `duration_seconds` | Ukupno vrijeme obrade u sekundama. |

## 🔑 Kako dobiti Google Gemini API ključ

Za korištenje ovog Actiona potreban vam je besplatni API ključ iz Google AI Studija:

1. Idite na [Google AI Studio](https://aistudio.google.com/).
2. Prijavite se sa svojim Google računom.
3. U lijevom navigacijskom izborniku kliknite na **Get API key**.
4. Kliknite gumb **Create API key**.
5. Kopirajte generirani ključ.
6. Idite u svoj GitHub repozitorij -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Kliknite **New repository secret**, nazovite ga `GEMINI_API_KEY`, zalijepite svoj ključ u polje Secret i spremite.

## 🔑 Kako konfigurirati standardni GitHub token

Ovaj Action koristi ugrađeni `GITHUB_TOKEN` za guranje (push) commitova. **Ne morate** ručno kreirati Personal Access Token (PAT), ali **morate** osigurati da zadani token ima odgovarajuća prava (dozvole):

1. Idite u postavke vašeg repozitorija **Settings** -> **Actions** -> **General**.
2. Pomaknite se dolje do odjeljka **Workflow permissions**.
3. Odaberite **Read and write permissions**.
4. Kliknite **Save**.
5. U YAML datoteci svog tijeka rada, jednostavno proslijedite `${{ secrets.GITHUB_TOKEN }}` u `github_token` ulazni parametar (kao što je prikazano u primjeru korištenja).

## 📄 Licenca

Ovaj projekt je licenciran pod MIT licencom - pogledajte [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) datoteku za detalje.