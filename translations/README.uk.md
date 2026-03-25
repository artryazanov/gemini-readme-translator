> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, яка автоматично перекладає ваш `README.md` кількома мовами за допомогою Gemini API. Вона розумно додає навігаційне меню з перехресними посиланнями на мови в усі файли та автоматично комітить зміни.

## 🚀 Особливості
* **Багатомовна підтримка:** Генерація README для декількох мов за один запуск.
* **Автонавігація:** Автоматично вставляє та підтримує стандартне меню перемикання мов у верхній частині ваших файлів (можна вимкнути). ШІ стилізує його автоматично!
* **Власний стиль:** Ви можете надати власний параметр стилю меню, щоб ШІ форматував перемикач мов саме так, як ви бажаєте.
* **Відстеження токенів:** Виводить статистику використання токенів Gemini.

## 🛠 Використання

Створіть файл робочого процесу (наприклад, `.github/workflows/translate.yml`):

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

## 📥 Вхідні параметри

| Параметр | Обов'язково | За замовчуванням | Опис |
| --- | --- | --- | --- |
| `api_key` | Так |  | Ваш Google Gemini API Key. |
| `github_token` | Так |  | Стандартний токен GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Так |  | Цільові мови, розділені комами (наприклад, `ru, es`). |
| `output_dir` | Ні | | Каталог для збереження перекладених файлів. За замовчуванням це каталог вихідного файлу. |
| `add_language_menu` | Ні | `true` | Встановіть значення `false`, щоб вимкнути автогенерацію мовного меню. |
| `use_absolute_links`| Ні | `true` | Встановіть на `false`, щоб використовувати відносні посилання замість абсолютних URL-адрес GitHub у згенерованих мовних меню. |
| `menu_style` | Ні | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Еталонний стиль, який ШІ використовує при генерації нового мовного меню. |
| `commit_message` | Ні | `docs: auto-translate README via Gemini` | Текст, що використовується для повідомлення git commit. |
| `model` | Ні | `gemini-3.1-pro-preview` | Модель Gemini для використання. |
| `source_file` | Ні | `README.md` | Базовий файл для перекладу. |

## 📤 Вихідні дані

| Вихідні дані | Опис |
| --- | --- |
| `total_tokens_used` | Загальна кількість оброблених токенів. |
| `input_tokens_used` | Кількість токенів у вхідних запитах. |
| `output_tokens_used` | Кількість згенерованих токенів у відповідях. |
| `duration_seconds` | Загальний час обробки в секундах. |

## 🔑 Як отримати Google Gemini API Key

Щоб використовувати цю дію, вам потрібен безкоштовний ключ API від Google AI Studio:

1. Перейдіть до [Google AI Studio](https://aistudio.google.com/).
2. Увійдіть за допомогою свого облікового запису Google.
3. У лівому навігаційному меню натисніть **Get API key**.
4. Натисніть кнопку **Create API key**.
5. Скопіюйте згенерований ключ.
6. Перейдіть до вашого репозиторію GitHub -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Натисніть **New repository secret**, назвіть його `GEMINI_API_KEY`, вставте свій ключ у поле Secret та збережіть.

## 🔑 Як налаштувати стандартний токен GitHub

Ця дія використовує вбудований `GITHUB_TOKEN` для надсилання комітів. Вам **не потрібно** створювати персональний маркер доступу (PAT) вручну, але ви **повинні** переконатися, що токен за замовчуванням має правильні дозволи:

1. Перейдіть до **Settings** -> **Actions** -> **General** вашого репозиторію.
2. Прокрутіть вниз до розділу **Workflow permissions**.
3. Виберіть **Read and write permissions**.
4. Натисніть **Save**.
5. У вашому YAML файлі робочого процесу просто передайте `${{ secrets.GITHUB_TOKEN }}` у параметр `github_token` (як показано в прикладі використання).

## 📄 Ліцензія

Цей проект ліцензовано на умовах ліцензії MIT — деталі дивіться у файлі [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).