> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, která automaticky překládá váš soubor `README.md` do několika jazyků pomocí Gemini API. Inteligentně vkládá provázané navigační menu pro volbu jazyka do všech souborů a automaticky provádí commit těchto změn.

## 🚀 Funkce
* **Podpora více jazyků:** Vygenerujte README pro více jazyků v jednom běhu.
* **Automatická navigace:** Automaticky vkládá a udržuje standardní menu pro přepínání jazyků na začátku vašich souborů (lze deaktivovat). AI jej automaticky naformátuje!
* **Vlastní stylování:** Můžete zadat parametr s vlastním stylem menu, takže AI naformátuje přepínač jazyků přesně podle vašich představ.
* **Sledování tokenů:** Vypisuje statistiky využití tokenů Gemini.

## 🛠 Použití

Vytvořte soubor workflow (např. `.github/workflows/translate.yml`):

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

| Vstup | Vyžadováno | Výchozí | Popis |
| --- | --- | --- | --- |
| `api_key` | Ano |  | Váš API klíč pro Google Gemini. |
| `github_token` | Ano |  | Standardní GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ano |  | Cílové jazyky oddělené čárkou (např. `ru, es`). |
| `output_dir` | Ne | | Adresář pro uložení přeložených souborů. Výchozí je adresář zdrojového souboru. |
| `add_language_menu` | Ne | `true` | Nastavte na `false` pro deaktivaci automatického generování jazykového menu. |
| `menu_style` | Ne | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referenční styl, který AI použije při generování nového jazykového menu. |
| `commit_message` | Ne | `docs: auto-translate README via Gemini` | Text použitý pro zprávu gitu při commitu. |
| `model` | Ne | `gemini-3.1-pro-preview` | Model Gemini, který se má použít. |
| `source_file` | Ne | `README.md` | Výchozí soubor k překladu. |

## 📤 Výstupy

| Výstup | Popis |
| --- | --- |
| `total_tokens_used` | Celkový počet zpracovaných tokenů. |
| `input_tokens_used` | Počet tokenů ve vstupních promptech. |
| `output_tokens_used` | Počet tokenů vygenerovaných v odpovědích. |
| `duration_seconds` | Celková doba zpracování v sekundách. |

## 🔑 Jak získat API klíč Google Gemini

Pro použití této akce potřebujete bezplatný API klíč z Google AI Studio:

1. Přejděte do [Google AI Studio](https://aistudio.google.com/).
2. Přihlaste se svým účtem Google.
3. V levém navigačním menu klikněte na **Get API key**.
4. Klikněte na tlačítko **Create API key**.
5. Zkopírujte si vygenerovaný klíč.
6. Přejděte do svého repozitáře na GitHubu -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Klikněte na **New repository secret**, pojmenujte jej `GEMINI_API_KEY`, vložte svůj klíč do pole Secret a uložte.

## 🔑 Jak nakonfigurovat standardní GitHub Token

Tato akce používá vestavěný `GITHUB_TOKEN` pro nahrávání commitů. **Nemusíte** ručně vytvářet Personal Access Token (PAT), ale **musíte** zajistit, aby měl výchozí token správná oprávnění:

1. Přejděte ve svém repozitáři do **Settings** -> **Actions** -> **General**.
2. Sjeďte dolů do sekce **Workflow permissions**.
3. Vyberte **Read and write permissions**.
4. Klikněte na **Save**.
5. Ve vašem YAML souboru workflow jednoduše předejte `${{ secrets.GITHUB_TOKEN }}` do vstupu `github_token` (jak je znázorněno v příkladu použití).

## 📄 Licence

Tento projekt je licencován pod MIT licencí – podrobnosti naleznete v souboru [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).