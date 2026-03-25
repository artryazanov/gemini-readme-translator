> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHubi Action, mis tõlgib teie `README.md` faili automaatselt mitmesse keelde, kasutades Gemini API-t. See lisab intelligentselt ristviidetega keelenavigatsioonimenüü kõikidesse failidesse ja teeb muudatustest automaatselt *commit*'i.

## 🚀 Funktsioonid
* **Mitmekeelne tugi:** Loo README failid mitme keele jaoks ühe käivitamisega.
* **Automaatne navigeerimine:** Lisab ja haldab automaatselt standardset keelevahetuse menüüd teie failide ülaosas (saab välja lülitada). Tehisintellekt kujundab selle automaatselt!
* **Kohandatud stiil:** Saate määrata kohandatud menüüstiili parameetri, et AI vormindaks keelevahetaja täpselt teie soovide järgi.
* **Žetoonide jälgimine (Token Tracking):** Väljastab Gemini žetoonide kasutamise statistika.

## 🛠 Kasutamine

Loo töövoo (workflow) fail (nt `.github/workflows/translate.yml`):

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

## 📥 Sisendid

| Sisend | Kohustuslik | Vaikimisi | Kirjeldus |
| --- | --- | --- | --- |
| `api_key` | Jah |  | Sinu Google Gemini API võti. |
| `github_token` | Jah |  | Standardne GitHubi žetoon (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Jah |  | Komadega eraldatud sihtkeeled (nt `ru, es`). |
| `output_dir` | Ei | | Kataloog, kuhu salvestatakse tõlgitud failid. Vaikimisi on see lähtefaili kataloog. |
| `add_language_menu` | Ei | `true` | Määra `false`, et keelata keelemenüü automaatne genereerimine. |
| `use_absolute_links`| Ei | `true` | Määrake `false`, et kasutada suhtelisi linke absoluutsete GitHubi URLide asemel genereeritud keelemenüüdes. |
| `menu_style` | Ei | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Võrdlusstiil, mida AI kasutab uue keelemenüü loomisel. |
| `commit_message` | Ei | `docs: auto-translate README via Gemini` | Git'i sissekande (*commit*) sõnumis kasutatav tekst. |
| `model` | Ei | `gemini-3.1-pro-preview` | Kasutatav Gemini mudel. |
| `source_file` | Ei | `README.md` | Baasfail, mida tõlkida. |

## 📤 Väljundid

| Väljund | Kirjeldus |
| --- | --- |
| `total_tokens_used` | Töödeldud žetoonide (tokenite) koguarv. |
| `input_tokens_used` | Sisendviipades (*prompts*) olevate žetoonide arv. |
| `output_tokens_used` | Vastustes genereeritud žetoonide arv. |
| `duration_seconds` | Kogu töötlemisaeg sekundites. |

## 🔑 Kuidas saada Google Gemini API võtit

Selle Actioni kasutamiseks vajate tasuta API võtit Google AI Studio'st:

1. Mine lehele [Google AI Studio](https://aistudio.google.com/).
2. Logi sisse oma Google'i kontoga.
3. Klõpsa vasakpoolses navigatsioonimenüüs valikule **Get API key** (Hangi API võti).
4. Klõpsa nupule **Create API key** (Loo API võti).
5. Kopeeri loodud võti.
6. Mine oma GitHubi hoidlasse (*repository*) -> **Settings** (Seaded) -> **Secrets and variables** (Saladused ja muutujad) -> **Actions**.
7. Klõpsa **New repository secret** (Uus hoidla saladus), pane sellele nimeks `GEMINI_API_KEY`, kleebi oma võti *Secret* väljale ja salvesta.

## 🔑 Kuidas seadistada standardset GitHubi žetooni (Token)

See Action kasutab sissekannete (*commit*) tegemiseks sisseehitatud `GITHUB_TOKEN`-it. Sa **ei pea** käsitsi looma personaalset juurdepääsužetooni (PAT), kuid sa **pead** veenduma, et vaikežetoonil on õiged load:

1. Mine oma hoidlas (*repository*) **Settings** -> **Actions** -> **General**.
2. Keri alla jaotiseni **Workflow permissions** (Töövoo load).
3. Vali **Read and write permissions** (Lugemis- ja kirjutamisõigused).
4. Klõpsa **Save** (Salvesta).
5. Oma töövoo YAML-failis edasta lihtsalt `${{ secrets.GITHUB_TOKEN }}` `github_token` sisendile (nagu on näidatud kasutusnäites).

## 📄 Litsents

See projekt on litsentsitud MIT litsentsi all - lisateabe saamiseks vaata faili [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).