> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# „Gemini“ README vertėjas


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

„GitHub Action“ įrankis, kuris automatiškai išverčia jūsų `README.md` į kelias kalbas naudojant „Gemini API“. Jis sumaniai įterpia susietą kalbų naršymo meniu į visus failus ir automatiškai išsaugo pakeitimus (įvykdo „commit“).

## 🚀 Ypatybės
* **Kelių kalbų palaikymas:** Generuokite README failus keliomis kalbomis vienu paleidimu.
* **Automatinis naršymas:** Automatiškai įterpia ir palaiko standartinį kalbų perjungimo meniu failų viršuje (galima išjungti). Dirbtinis intelektas jį stilizuoja automatiškai!
* **Tinkintas stilius:** Galite pateikti tinkintą meniu stiliaus parametrą, kad DI suformatuotų kalbų perjungiklį tiksliai taip, kaip norite.
* **Žetonų (token) stebėjimas:** Išveda „Gemini“ žetonų naudojimo statistiką.

## 🛠 Naudojimas

Sukurkite darbo eigos failą (pvz., `.github/workflows/translate.yml`):

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

## 📥 Įvestys

| Įvestis | Būtina | Numatytasis | Aprašymas |
| --- | --- | --- | --- |
| `api_key` | Taip |  | Jūsų „Google Gemini“ API raktas. |
| `github_token` | Taip |  | Standartinis „GitHub“ prieigos raktas (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Taip |  | Kableliais atskirtos tikslinės kalbos (pvz., `ru, es`). |
| `output_dir` | Ne | | Katalogas, kuriame bus išsaugoti išversti failai. Numatytasis yra šaltinio failo katalogas. |
| `add_language_menu` | Ne | `true` | Nustatykite `false`, jei norite išjungti automatinį kalbų meniu generavimą. |
| `use_absolute_links`| Ne | `true` | Nustatykite kaip `false`, jei norite naudoti santykines nuorodas, o ne absoliučius „GitHub“ URL adresus sugeneruotuose kalbų meniu. |
| `menu_style` | Ne | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Etaloninis stilius, kurį DI naudoja generuodamas naują kalbų meniu. |
| `commit_message` | Ne | `docs: auto-translate README via Gemini` | Tekstas, naudojamas „git commit“ žinutėje. |
| `model` | Ne | `gemini-3.1-pro-preview` | Naudojamas „Gemini“ modelis. |
| `source_file` | Ne | `README.md` | Bazinis failas, kurį reikia išversti. |

## 📤 Išvestys

| Išvestis | Aprašymas |
| --- | --- |
| `total_tokens_used` | Bendras apdorotų žetonų (token) skaičius. |
| `input_tokens_used` | Įvesties užklausų žetonų skaičius. |
| `output_tokens_used` | Atsakymuose sugeneruotų žetonų skaičius. |
| `duration_seconds` | Bendras apdorojimo laikas sekundėmis. |

## 🔑 Kaip gauti „Google Gemini“ API raktą

Norėdami naudoti šį veiksmą („Action“), turite turėti nemokamą API raktą iš „Google AI Studio“:

1. Eikite į [Google AI Studio](https://aistudio.google.com/).
2. Prisijunkite su savo „Google“ paskyra.
3. Kairiajame naršymo meniu spustelėkite **Get API key**.
4. Spustelėkite mygtuką **Create API key**.
5. Nukopijuokite sugeneruotą raktą.
6. Eikite į savo „GitHub“ repozitoriją -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Spustelėkite **New repository secret**, pavadinkite jį `GEMINI_API_KEY`, įklijuokite savo raktą į laukelį „Secret“ ir išsaugokite.

## 🔑 Kaip sukonfigūruoti standartinį „GitHub“ prieigos raktą

Šis veiksmas naudoja įmontuotą `GITHUB_TOKEN` pakeitimams išsiųsti („push commits“). Jums **nereikia** rankiniu būdu kurti asmeninės prieigos rakto (PAT), tačiau **privalote** užtikrinti, kad numatytasis raktas turėtų tinkamus leidimus:

1. Eikite į savo repozitorijos **Settings** -> **Actions** -> **General**.
2. Slinkite žemyn iki skilties **Workflow permissions**.
3. Pasirinkite **Read and write permissions**.
4. Spustelėkite **Save**.
5. Savo darbo eigos YAML faile paprasčiausiai perduokite `${{ secrets.GITHUB_TOKEN }}` į `github_token` įvestį (kaip parodyta naudojimo pavyzdyje).

## 📄 Licencija

Šis projektas licencijuotas pagal MIT licenciją – daugiau informacijos rasite [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) faile.