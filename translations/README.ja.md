> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini APIを使用して、`README.md`を複数の言語に自動的に翻訳するGitHub Actionです。相互リンクされた言語ナビゲーションメニューをすべてのファイルにインテリジェントに注入し、変更を自動的にコミットします。

## 🚀 機能
* **多言語サポート:** 1回の実行で複数の言語のREADMEを生成します。
* **自動ナビゲーション:** ファイルの先頭に標準の言語切り替えメニューを自動的に挿入および維持します（無効化可能）。AIが自動的にスタイルを設定します！
* **カスタムスタイリング:** カスタムメニュースタイルパラメーターを提供することで、AIに言語スイッチャーを正確に希望どおりにフォーマットさせることができます。
* **トークン追跡:** Geminiのトークン使用状況の統計を出力します。

## 🛠 使用方法

ワークフローファイルを作成します（例：`.github/workflows/translate.yml`）:

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

## 📥 入力

| 入力 | 必須 | デフォルト | 説明 |
| --- | --- | --- | --- |
| `api_key` | はい |  | あなたのGoogle Gemini APIキー。 |
| `github_token` | はい |  | 標準のGitHubトークン (`${{ secrets.GITHUB_TOKEN }}`)。 |
| `languages` | はい |  | カンマ区切りのターゲット言語（例：`ru, es`）。 |
| `output_dir` | いいえ | | 翻訳されたファイルを保存するディレクトリ。デフォルトはソースファイルのディレクトリです。 |
| `add_language_menu` | いいえ | `true` | 言語メニューの自動生成を無効にする場合は `false` に設定します。 |
| `menu_style` | いいえ | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | 新しい言語メニューを生成する際にAIが使用する参照スタイル。 |
| `commit_message` | いいえ | `docs: auto-translate README via Gemini` | gitコミットメッセージに使用されるテキスト。 |
| `model` | いいえ | `gemini-3.1-pro-preview` | 使用するGeminiモデル。 |
| `source_file` | いいえ | `README.md` | 翻訳するベースファイル。 |

## 📤 出力

| 出力 | 説明 |
| --- | --- |
| `total_tokens_used` | 処理されたトークンの総数。 |
| `input_tokens_used` | 入力プロンプト内のトークン数。 |
| `output_tokens_used` | レスポンスで生成されたトークン数。 |
| `duration_seconds` | 合計処理時間（秒）。 |

## 🔑 Google Gemini APIキーの取得方法

このアクションを使用するには、Google AI Studioからの無料のAPIキーが必要です。

1. [Google AI Studio](https://aistudio.google.com/) にアクセスします。
2. Googleアカウントでサインインします。
3. 左側のナビゲーションメニューで、**Get API key** をクリックします。
4. **Create API key** ボタンをクリックします。
5. 生成されたキーをコピーします。
6. GitHubリポジトリの **Settings**（設定） -> **Secrets and variables**（シークレットと変数） -> **Actions** に移動します。
7. **New repository secret** をクリックし、名前に `GEMINI_API_KEY` を指定し、Secretフィールドにキーを貼り付けて保存します。

## 🔑 標準GitHubトークンの設定方法

このアクションは、組み込みの `GITHUB_TOKEN` を使用してコミットをプッシュします。Personal Access Token (PAT) を手動で作成する**必要はありません**が、デフォルトのトークンに正しい権限があることを確認する**必要があります**:

1. リポジトリの **Settings**（設定） -> **Actions** -> **General** に移動します。
2. **Workflow permissions** セクションまでスクロールします。
3. **Read and write permissions** を選択します。
4. **Save** をクリックします。
5. ワークフローYAMLで（使用例で示されているように）、`${{ secrets.GITHUB_TOKEN }}` を `github_token` 入力に渡すだけです。

## 📄 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については、[LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ファイルを参照してください。