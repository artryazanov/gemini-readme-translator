# Gemini README Translator

[![CI Pipeline](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/ci.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A GitHub Action that automatically translates your `README.md` into multiple languages using the Gemini API. It intelligently injects a cross-linked language navigation menu into all files and can either commit changes directly or create a Pull Request for review.

## 🚀 Features
* **Multi-Language Support:** Generate READMEs for multiple languages in one run.
* **Auto-Navigation:** Automatically inserts and maintains a standard language switcher menu at the top of your files (can be disabled). AI styles it automatically!
* **Custom Styling:** You can provide a custom menu style parameter so the AI formats the language switcher exactly how you want.
* **Pull Request Mode:** Review translations safely via Merge/Pull Requests before merging into your main branch.
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
      pull-requests: write
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Gemini README Translator
        uses: artryazanov/gemini-readme-translator@v1
        with:
          api_key: ${{ secrets.GEMINI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          languages: 'ru, zh-CN, es'
          add_language_menu: 'true'
          menu_style: '> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md)'
          create_pr: 'true'

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
| `create_pr` | No | `false` | If `true`, creates a PR instead of a direct commit. |
| `commit_message` | No | `docs: auto-translate README via Gemini` | Text used for the git commit message. |
| `model` | No | `gemini-3.1-pro-preview` | The Gemini model to use. |
| `source_file` | No | `README.md` | The base file to translate. |

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

This action uses the built-in `GITHUB_TOKEN` to push commits or create Pull Requests. You **do not** need to create a Personal Access Token (PAT) manually, but you **must** ensure the default token has the correct permissions:

1. Go to your repository **Settings** -> **Actions** -> **General**.
2. Scroll down to the **Workflow permissions** section.
3. Select **Read and write permissions**.
4. Check the box for *Allow GitHub Actions to create and approve pull requests* (required if you use `create_pr: 'true'`).
5. Click **Save**.
6. In your workflow YAML, simply pass `${{ secrets.GITHUB_TOKEN }}` to the `github_token` input (as shown in the usage example).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) file for details.
