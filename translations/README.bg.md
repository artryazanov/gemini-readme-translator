> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, което автоматично превежда вашия `README.md` на множество езици с помощта на Gemini API. То интелигентно инжектира меню за езикова навигация с вътрешни връзки във всички файлове и автоматично комитва промените.

## 🚀 Характеристики
* **Многоезична поддръжка:** Генерирайте README файлове за множество езици с едно изпълнение.
* **Автоматична навигация:** Автоматично вмъква и поддържа стандартно меню за превключване на езиците в горната част на вашите файлове (може да бъде деактивирано). Изкуственият интелект го стилизира автоматично!
* **Персонализиран стил:** Можете да предоставите параметър за персонализиран стил на менюто, така че ИИ да форматира превключвателя на езици точно както искате.
* **Проследяване на токени:** Извежда статистика за използването на токени в Gemini.

## 🛠 Употреба

Създайте workflow файл (напр., `.github/workflows/translate.yml`):

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

## 📥 Входни параметри

| Параметър | Задължителен | По подразбиране | Описание |
| --- | --- | --- | --- |
| `api_key` | Да |  | Вашият Google Gemini API ключ. |
| `github_token` | Да |  | Стандартен GitHub токен (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Да |  | Целеви езици, разделени със запетая (напр. `ru, es`). |
| `output_dir` | Не | | Директория за запазване на преведените файлове. По подразбиране е директорията на изходния файл. |
| `add_language_menu` | Не | `true` | Задайте на `false`, за да деактивирате автоматичното генериране на езиковото меню. |
| `use_absolute_links`| Не | `true` | Задайте като `false`, за да използвате относителни връзки вместо абсолютни GitHub URL адреси в генерираните езикови менюта. |
| `menu_style` | Не | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Референтният стил, който ИИ използва при генерирането на ново езиково меню. |
| `commit_message` | Не | `docs: auto-translate README via Gemini` | Текстът, използван за съобщението на git комита. |
| `model` | Не | `gemini-3.1-pro-preview` | Моделът на Gemini, който да се използва. |
| `source_file` | Не | `README.md` | Базовият файл за превод. |

## 📤 Изходни параметри

| Параметър | Описание |
| --- | --- |
| `total_tokens_used` | Общ брой обработени токени. |
| `input_tokens_used` | Брой токени във входящите заявки (prompts). |
| `output_tokens_used` | Брой токени, генерирани в отговорите. |
| `duration_seconds` | Общо време за обработка в секунди. |

## 🔑 Как да получите Google Gemini API ключ

За да използвате това action, се нуждаете от безплатен API ключ от Google AI Studio:

1. Отидете на [Google AI Studio](https://aistudio.google.com/).
2. Влезте с вашия Google акаунт.
3. В лявото навигационно меню кликнете върху **Get API key**.
4. Кликнете върху бутона **Create API key**.
5. Копирайте генерирания ключ.
6. Отидете във вашето GitHub хранилище -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Кликнете върху **New repository secret**, наименувайте го `GEMINI_API_KEY`, поставете вашия ключ в полето Secret и запазете.

## 🔑 Как да конфигурирате стандартния GitHub токен

Това действие (action) използва вградения `GITHUB_TOKEN` за push на комити. **Не е** необходимо ръчно да създавате Personal Access Token (PAT), но **трябва** да се уверите, че токенът по подразбиране има правилните права:

1. Отидете в **Settings** -> **Actions** -> **General** на вашето хранилище.
2. Превъртете надолу до раздела **Workflow permissions**.
3. Изберете **Read and write permissions**.
4. Кликнете върху **Save**.
5. Във вашия workflow YAML, просто предайте `${{ secrets.GITHUB_TOKEN }}` на параметъра `github_token` (както е показано в примера за употреба).

## 📄 Лиценз

Този проект е лицензиран под MIT License - вижте файла [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) за подробности.