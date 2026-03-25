> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README 翻譯工具


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

這是一個 GitHub Action，使用 Gemini API 自動將您的 `README.md` 翻譯成多種語言。它會智慧地在所有檔案中插入互相連結的語言導覽選單，並自動提交變更。

## 🚀 功能特色
* **多語言支援：** 一次執行即可產生多種語言的 README 檔案。
* **自動導覽：** 自動在您的檔案頂部插入並維護標準的語言切換選單（可停用）。AI 會自動為其套用樣式！
* **自訂樣式：** 您可以提供自訂的選單樣式參數，讓 AI 完全按照您想要的方式格式化語言切換器。
* **Token 追蹤：** 輸出 Gemini token 的使用統計資料。

## 🛠 使用方法

建立一個工作流程檔案（例如：`.github/workflows/translate.yml`）：

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

## 📥 輸入參數

| 輸入 (Input) | 必填 (Required) | 預設值 (Default) | 說明 (Description) |
| --- | --- | --- | --- |
| `api_key` | 是 |  | 您的 Google Gemini API 金鑰。 |
| `github_token` | 是 |  | 標準的 GitHub token (`${{ secrets.GITHUB_TOKEN }}`)。 |
| `languages` | 是 |  | 以逗號分隔的目標語言（例如 `ru, es`）。 |
| `output_dir` | 否 | | 儲存翻譯檔案的目錄。預設為來源檔案所在的目錄。 |
| `add_language_menu` | 否 | `true` | 設定為 `false` 可停用自動產生語言選單。 |
| `use_absolute_links`| 否 | `true` | 設定為 `false`，在產生的語言選單中使用相對連結，而非絕對的 GitHub URL。 |
| `menu_style` | 否 | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | AI 在產生新語言選單時所使用的參考樣式。 |
| `commit_message` | 否 | `docs: auto-translate README via Gemini` | 用於 Git 提交訊息的文字。 |
| `model` | 否 | `gemini-3.1-pro-preview` | 要使用的 Gemini 模型。 |
| `source_file` | 否 | `README.md` | 要翻譯的基礎檔案。 |

## 📤 輸出參數

| 輸出 (Output) | 說明 (Description) |
| --- | --- |
| `total_tokens_used` | 處理的 Token 總數。 |
| `input_tokens_used` | 輸入提示 (prompts) 中的 Token 數量。 |
| `output_tokens_used` | 回應中產生的 Token 數量。 |
| `duration_seconds` | 總處理時間（以秒為單位）。 |

## 🔑 如何取得 Google Gemini API 金鑰

要使用此 Action，您需要從 Google AI Studio 取得免費的 API 金鑰：

1. 前往 [Google AI Studio](https://aistudio.google.com/)。
2. 使用您的 Google 帳戶登入。
3. 在左側導覽選單中，點擊 **Get API key**。
4. 點擊 **Create API key** 按鈕。
5. 複製產生的金鑰。
6. 前往您的 GitHub 儲存庫 -> **Settings** -> **Secrets and variables** -> **Actions**。
7. 點擊 **New repository secret**，將其命名為 `GEMINI_API_KEY`，將您的金鑰貼到 Secret 欄位中，然後儲存。

## 🔑 如何設定標準 GitHub Token

此 Action 使用內建的 `GITHUB_TOKEN` 來推送提交。您**不需要**手動建立個人存取權杖 (PAT)，但您**必須**確保預設的 token 具有正確的權限：

1. 前往您的儲存庫 **Settings** -> **Actions** -> **General**。
2. 向下捲動至 **Workflow permissions** 區塊。
3. 選擇 **Read and write permissions**。
4. 點擊 **Save**。
5. 在您的工作流程 YAML 中，只需將 `${{ secrets.GITHUB_TOKEN }}` 傳遞給 `github_token` 輸入參數（如使用方法範例所示）。

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳情請見 [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) 檔案。