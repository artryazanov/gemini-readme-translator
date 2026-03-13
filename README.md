> 🌐 **Languages:** [English](README.md) | [Русский](translations/README.ru.md) | [ไทย](translations/README.th.md) | [简体中文](translations/README.zh-CN.md) | [繁體中文](translations/README.zh-TW.md) | [हिन्दी](translations/README.hi.md) | [Español](translations/README.es.md) | [Français](translations/README.fr.md) | [العربية](translations/README.ar.md) | [বাংলা](translations/README.bn.md) | [Português](translations/README.pt.md) | [اردو](translations/README.ur.md) | [Bahasa Indonesia](translations/README.id.md) | [Deutsch](translations/README.de.md) | [日本語](translations/README.ja.md) | [मराठी](translations/README.mr.md) | [తెలుగు](translations/README.te.md) | [Türkçe](translations/README.tr.md) | [தமிழ்](translations/README.ta.md) | [Tiếng Việt](translations/README.vi.md) | [한국어](translations/README.ko.md) | [Kiswahili](translations/README.sw.md) | [Italiano](translations/README.it.md) | [ગુજરાતી](translations/README.gu.md) | [فارسی](translations/README.fa.md) | [ಕನ್ನಡ](translations/README.kn.md) | [Polski](translations/README.pl.md) | [മലയാളം](translations/README.ml.md) | [Українська](translations/README.uk.md) | [Română](translations/README.ro.md) | [Nederlands](translations/README.nl.md) | [Ελληνικά](translations/README.el.md) | [Magyar](translations/README.hu.md) | [Svenska](translations/README.sv.md) | [Čeština](translations/README.cs.md) | [Српски](translations/README.sr.md) | [עברית](translations/README.he.md) | [Български](translations/README.bg.md) | [Dansk](translations/README.da.md) | [Suomi](translations/README.fi.md) | [Norsk](translations/README.no.md) | [Slovenčina](translations/README.sk.md) | [Hrvatski](translations/README.hr.md) | [Lietuvių](translations/README.lt.md) | [Slovenščina](translations/README.sl.md) | [Latviešu](translations/README.lv.md) | [Eesti](translations/README.et.md)

# Gemini README Translator

[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A GitHub Action that automatically translates your `README.md` into multiple languages using the Gemini API. It intelligently injects a cross-linked language navigation menu into all files and automatically commits the changes.

## 🚀 Features
* **Multi-Language Support:** Generate READMEs for multiple languages in one run.
* **Auto-Navigation:** Automatically inserts and maintains a standard language switcher menu at the top of your files (can be disabled). AI styles it automatically!
* **Custom Styling:** You can provide a custom menu style parameter so the AI formats the language switcher exactly how you want.
* **Token Tracking:** Outputs Gemini token usage statistics.

## 🛠 Usage

Create a workflow file (e.g., `.github/workflows/translate.yml`):

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

## 📥 Inputs

| Input | Required | Default | Description |
| --- | --- | --- | --- |
| `api_key` | Yes |  | Your Google Gemini API Key. |
| `github_token` | Yes |  | Standard GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Yes |  | Comma-separated target languages (e.g. `ru, es`). |
| `output_dir` | No | | Directory to save translated files. Defaults to source file's directory. |
| `add_language_menu` | No | `true` | Set to `false` to disable auto-generation of the language menu. |
| `menu_style` | No | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | The reference style AI uses when generating a new language menu. |
| `commit_message` | No | `docs: auto-translate README via Gemini` | Text used for the git commit message. |
| `model` | No | `gemini-3.1-pro-preview` | The Gemini model to use. |
| `source_file` | No | `README.md` | The base file to translate. |

## 📤 Outputs

| Output | Description |
| --- | --- |
| `total_tokens_used` | Total number of tokens processed. |
| `input_tokens_used` | Number of tokens in the input prompts. |
| `output_tokens_used` | Number of tokens generated in the responses. |
| `duration_seconds` | Total processing time in seconds. |

## 🔑 How to get a Google Gemini API Key

To use this action, you need a free API key from Google AI Studio:

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. In the left navigation menu, click on **Get API key**.
4. Click the **Create API key** button.
5. Copy the generated key.
6. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Click **New repository secret**, name it `GEMINI_API_KEY`, paste your key into the Secret field, and save.

## 🔑 How to configure the Standard GitHub Token

This action uses the built-in `GITHUB_TOKEN` to push commits. You **do not** need to create a Personal Access Token (PAT) manually, but you **must** ensure the default token has the correct permissions:

1. Go to your repository **Settings** -> **Actions** -> **General**.
2. Scroll down to the **Workflow permissions** section.
3. Select **Read and write permissions**.
4. Click **Save**.
5. In your workflow YAML, simply pass `${{ secrets.GITHUB_TOKEN }}` to the `github_token` input (as shown in the usage example).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) file for details.