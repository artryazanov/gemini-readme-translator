> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

一个使用 Gemini API 自动将你的 `README.md` 翻译成多种语言的 GitHub Action。它会智能地在所有文件中注入相互链接的语言导航菜单，并自动提交更改。

## 🚀 功能特性
* **多语言支持：** 一次运行即可生成多种语言的 README 文件。
* **自动导航：** 自动在文件顶部插入并维护标准的语言切换菜单（可禁用）。AI 会自动为其设置样式！
* **自定义样式：** 你可以提供自定义的菜单样式参数，让 AI 完全按照你的期望来格式化语言切换器。
* **Token 统计：** 输出 Gemini token 的使用统计信息。

## 🛠 使用方法

创建一个工作流文件（例如：`.github/workflows/translate.yml`）：

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

## 📥 输入参数

| 输入参数 | 是否必填 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `api_key` | 是 |  | 你的 Google Gemini API 密钥。 |
| `github_token` | 是 |  | 标准的 GitHub token (`${{ secrets.GITHUB_TOKEN }}`)。 |
| `languages` | 是 |  | 以逗号分隔的目标语言（例如：`ru, es`）。 |
| `output_dir` | 否 | | 保存翻译后文件的目录。默认为源文件所在的目录。 |
| `add_language_menu` | 否 | `true` | 设置为 `false` 以禁用语言菜单的自动生成。 |
| `use_absolute_links`| 否 | `true` | 设置为 `false`，在生成的语言菜单中使用相对链接，而不是绝对的 GitHub URL。 |
| `menu_style` | 否 | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | AI 在生成新语言菜单时使用的参考样式。 |
| `commit_message` | 否 | `docs: auto-translate README via Gemini` | 用于 git 提交信息的文本。 |
| `model` | 否 | `gemini-3.1-pro-preview` | 要使用的 Gemini 模型。 |
| `source_file` | 否 | `README.md` | 要翻译的基础文件。 |

## 📤 输出参数

| 输出参数 | 描述 |
| --- | --- |
| `total_tokens_used` | 处理的 token 总数。 |
| `input_tokens_used` | 输入提示词中的 token 数量。 |
| `output_tokens_used` | 响应中生成的 token 数量。 |
| `duration_seconds` | 总处理时间（以秒为单位）。 |

## 🔑 如何获取 Google Gemini API 密钥

要使用此 Action，你需要从 Google AI Studio 获取一个免费的 API 密钥：

1. 访问 [Google AI Studio](https://aistudio.google.com/)。
2. 使用你的 Google 账号登录。
3. 在左侧导航菜单中，点击 **Get API key**。
4. 点击 **Create API key** 按钮。
5. 复制生成的密钥。
6. 进入你的 GitHub 仓库 -> **Settings** -> **Secrets and variables** -> **Actions**。
7. 点击 **New repository secret**，将其命名为 `GEMINI_API_KEY`，将你的密钥粘贴到 Secret 字段中，然后保存。

## 🔑 如何配置标准 GitHub Token

此 Action 使用内置的 `GITHUB_TOKEN` 来推送提交。你**不需要**手动创建个人访问令牌（PAT），但你**必须**确保默认 token 具有正确的权限：

1. 进入你的仓库 **Settings** -> **Actions** -> **General**。
2. 向下滚动到 **Workflow permissions** 部分。
3. 选择 **Read and write permissions**。
4. 点击 **Save**。
5. 在你的工作流 YAML 文件中，只需将 `${{ secrets.GITHUB_TOKEN }}` 传递给 `github_token` 输入参数（如使用示例所示）。

## 📄 许可证

本项目采用 MIT 许可证进行授权 - 有关详细信息，请参阅 [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) 文件。