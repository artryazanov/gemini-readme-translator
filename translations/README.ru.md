> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, которое автоматически переводит ваш `README.md` на несколько языков с использованием Gemini API. Оно интеллектуально внедряет перекрестное навигационное меню языков во все файлы и автоматически коммитит изменения.

## 🚀 Возможности
* **Многоязычная поддержка:** Генерация README для нескольких языков за один запуск.
* **Автонавигация:** Автоматически вставляет и поддерживает стандартное меню переключения языков в верхней части ваших файлов (можно отключить). ИИ стилизует его автоматически!
* **Пользовательская стилизация:** Вы можете задать параметр пользовательского стиля меню, чтобы ИИ отформатировал переключатель языков именно так, как вам нужно.
* **Отслеживание токенов:** Выводит статистику использования токенов Gemini.

## 🛠 Использование

Создайте файл рабочего процесса (например, `.github/workflows/translate.yml`):

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

## 📥 Входные параметры

| Параметр | Обязательно | По умолчанию | Описание |
| --- | --- | --- | --- |
| `api_key` | Да |  | Ваш API-ключ Google Gemini. |
| `github_token` | Да |  | Стандартный токен GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Да |  | Целевые языки, разделенные запятыми (например, `ru, es`). |
| `output_dir` | Нет | | Каталог для сохранения переведенных файлов. По умолчанию используется каталог исходного файла. |
| `add_language_menu` | Нет | `true` | Установите в `false`, чтобы отключить автогенерацию языкового меню. |
| `use_absolute_links`| Нет | `true` | Установите в `false`, чтобы использовать относительные ссылки вместо абсолютных URL GitHub в сгенерированных языковых меню. |
| `menu_style` | Нет | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Эталонный стиль, который использует ИИ при генерации нового языкового меню. |
| `commit_message` | Нет | `docs: auto-translate README via Gemini` | Текст, используемый для сообщения коммита git. |
| `model` | Нет | `gemini-3.1-pro-preview` | Используемая модель Gemini. |
| `source_file` | Нет | `README.md` | Базовый файл для перевода. |

## 📤 Выходные параметры

| Параметр | Описание |
| --- | --- |
| `total_tokens_used` | Общее количество обработанных токенов. |
| `input_tokens_used` | Количество токенов во входящих промптах. |
| `output_tokens_used` | Количество токенов, сгенерированных в ответах. |
| `duration_seconds` | Общее время обработки в секундах. |

## 🔑 Как получить API-ключ Google Gemini

Для использования этого Action вам потребуется бесплатный API-ключ от Google AI Studio:

1. Перейдите в [Google AI Studio](https://aistudio.google.com/).
2. Войдите с помощью своего аккаунта Google.
3. В левом навигационном меню нажмите на **Get API key**.
4. Нажмите кнопку **Create API key**.
5. Скопируйте сгенерированный ключ.
6. Перейдите в ваш репозиторий GitHub -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Нажмите **New repository secret**, назовите его `GEMINI_API_KEY`, вставьте ваш ключ в поле Secret и сохраните.

## 🔑 Как настроить стандартный токен GitHub

Это Action использует встроенный `GITHUB_TOKEN` для отправки коммитов. Вам **не нужно** вручную создавать Personal Access Token (PAT), но вы **должны** убедиться, что у токена по умолчанию есть правильные разрешения:

1. Перейдите в **Settings** -> **Actions** -> **General** вашего репозитория.
2. Прокрутите вниз до раздела **Workflow permissions**.
3. Выберите **Read and write permissions**.
4. Нажмите **Save**.
5. В вашем YAML-файле рабочего процесса просто передайте `${{ secrets.GITHUB_TOKEN }}` во входной параметр `github_token` (как показано в примере использования).

## 📄 Лицензия

Этот проект лицензирован на условиях MIT License - подробности см. в файле [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).