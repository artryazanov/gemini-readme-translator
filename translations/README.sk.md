> 🌐 **Jazyky:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, ktorá automaticky preloží váš súbor `README.md` do viacerých jazykov pomocou Gemini API. Inteligentne vkladá prepojené navigačné menu jazykov do všetkých súborov a automaticky vytvorí commit so zmenami.

## 🚀 Funkcie
* **Podpora viacerých jazykov:** Generovanie súborov README pre viacero jazykov v jednom behu.
* **Automatická navigácia:** Automaticky vkladá a spravuje štandardné menu na prepínanie jazykov v hornej časti vašich súborov (možno deaktivovať). AI ho automaticky naformátuje!
* **Vlastné štýlovanie:** Môžete zadať parameter pre vlastný štýl menu, aby AI naformátovala prepínač jazykov presne podľa vašich predstáv.
* **Sledovanie tokenov:** Zobrazuje štatistiky využitia tokenov Gemini.

## 🛠 Použitie

Vytvorte súbor pracovného postupu (workflow) (napr. `.github/workflows/translate.yml`):

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

## 📥 Vstupy

| Vstup | Povinné | Predvolené | Popis |
| --- | --- | --- | --- |
| `api_key` | Áno |  | Váš kľúč Google Gemini API. |
| `github_token` | Áno |  | Štandardný GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Áno |  | Cieľové jazyky oddelené čiarkou (napr. `ru, es`). |
| `output_dir` | Nie | | Adresár na uloženie preložených súborov. Predvolene je to adresár zdrojového súboru. |
| `add_language_menu` | Nie | `true` | Nastavte na `false` pre vypnutie automatického generovania jazykového menu. |
| `use_absolute_links`| Nie | `true` | Nastavte na `false` pre použitie relatívnych odkazov namiesto absolútnych GitHub URL adresách vo vygenerovaných jazykových ponukách. |
| `menu_style` | Nie | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referenčný štýl, ktorý AI používa pri generovaní nového jazykového menu. |
| `commit_message` | Nie | `docs: auto-translate README via Gemini` | Text použitý pre správu git commitu. |
| `model` | Nie | `gemini-3.1-pro-preview` | Model Gemini, ktorý sa má použiť. |
| `source_file` | Nie | `README.md` | Základný súbor na preklad. |

## 📤 Výstupy

| Výstup | Popis |
| --- | --- |
| `total_tokens_used` | Celkový počet spracovaných tokenov. |
| `input_tokens_used` | Počet tokenov vo vstupných promtoch. |
| `output_tokens_used` | Počet vygenerovaných tokenov v odpovediach. |
| `duration_seconds` | Celkový čas spracovania v sekundách. |

## 🔑 Ako získať kľúč Google Gemini API

Ak chcete použiť túto akciu, potrebujete bezplatný kľúč API od Google AI Studio:

1. Prejdite do [Google AI Studio](https://aistudio.google.com/).
2. Prihláste sa pomocou svojho účtu Google.
3. V ľavom navigačnom menu kliknite na **Get API key**.
4. Kliknite na tlačidlo **Create API key**.
5. Skopírujte vygenerovaný kľúč.
6. Prejdite do svojho repozitára na GitHube -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Kliknite na **New repository secret**, pomenujte ho `GEMINI_API_KEY`, vložte váš kľúč do poľa Secret a uložte.

## 🔑 Ako nakonfigurovať Štandardný GitHub Token

Táto akcia používa vstavaný `GITHUB_TOKEN` na nahrávanie (push) commitov. Nepotrebujete manuálne vytvárať Personal Access Token (PAT), ale musíte zabezpečiť, aby mal predvolený token správne oprávnenia:

1. Prejdite do **Settings** -> **Actions** -> **General** vo vašom repozitári.
2. Prejdite nižšie na sekciu **Workflow permissions**.
3. Vyberte **Read and write permissions**.
4. Kliknite na **Save**.
5. Vo vašom YAML súbore pracovného postupu (workflow) jednoducho priraďte `${{ secrets.GITHUB_TOKEN }}` vstupu `github_token` (ako je znázornené v príklade použitia).

## 📄 Licencia

Tento projekt je licencovaný pod MIT licenciou - pre viac podrobností si pozrite súbor [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).