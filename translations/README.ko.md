> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini API를 사용하여 `README.md`를 여러 언어로 자동 번역하는 GitHub Action입니다. 모든 파일에 상호 연결된 언어 탐색 메뉴를 지능적으로 주입하고 변경 사항을 자동으로 커밋합니다.

## 🚀 기능
* **다국어 지원:** 한 번의 실행으로 여러 언어의 README를 생성합니다.
* **자동 탐색:** 파일의 최상단에 표준 언어 전환 메뉴를 자동으로 삽입하고 유지 관리합니다(비활성화 가능). AI가 자동으로 스타일을 지정합니다!
* **사용자 정의 스타일링:** 사용자 정의 메뉴 스타일 매개변수를 제공하여 AI가 원하는 방식으로 언어 전환기의 형식을 지정하도록 할 수 있습니다.
* **토큰 추적:** Gemini 토큰 사용 통계를 출력합니다.

## 🛠 사용법

워크플로우 파일(예: `.github/workflows/translate.yml`)을 생성하세요:

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

## 📥 입력(Inputs)

| 입력(Input) | 필수(Required) | 기본값(Default) | 설명(Description) |
| --- | --- | --- | --- |
| `api_key` | 예 |  | Google Gemini API 키. |
| `github_token` | 예 |  | 표준 GitHub 토큰 (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | 예 |  | 쉼표로 구분된 대상 언어 (예: `ru, es`). |
| `output_dir` | 아니요 | | 번역된 파일을 저장할 디렉토리. 기본값은 원본 파일의 디렉토리입니다. |
| `add_language_menu` | 아니요 | `true` | 언어 메뉴의 자동 생성을 비활성화하려면 `false`로 설정하세요. |
| `menu_style` | 아니요 | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | 새로운 언어 메뉴를 생성할 때 AI가 참조하는 스타일. |
| `commit_message` | 아니요 | `docs: auto-translate README via Gemini` | git 커밋 메시지에 사용되는 텍스트. |
| `model` | 아니요 | `gemini-3.1-pro-preview` | 사용할 Gemini 모델. |
| `source_file` | 아니요 | `README.md` | 번역할 기준 파일. |

## 📤 출력(Outputs)

| 출력(Output) | 설명(Description) |
| --- | --- |
| `total_tokens_used` | 처리된 총 토큰 수. |
| `input_tokens_used` | 입력 프롬프트의 토큰 수. |
| `output_tokens_used` | 응답에서 생성된 토큰 수. |
| `duration_seconds` | 총 처리 시간(초). |

## 🔑 Google Gemini API 키 발급 방법

이 액션을 사용하려면 Google AI Studio에서 무료 API 키를 받아야 합니다:

1. [Google AI Studio](https://aistudio.google.com/)로 이동합니다.
2. Google 계정으로 로그인합니다.
3. 왼쪽 탐색 메뉴에서 **Get API key**를 클릭합니다.
4. **Create API key** 버튼을 클릭합니다.
5. 생성된 키를 복사합니다.
6. GitHub 저장소 -> **Settings** -> **Secrets and variables** -> **Actions**로 이동합니다.
7. **New repository secret**을 클릭하고, 이름을 `GEMINI_API_KEY`로 지정한 후 발급받은 키를 Secret 필드에 붙여넣고 저장합니다.

## 🔑 표준 GitHub 토큰 구성 방법

이 액션은 커밋을 푸시하기 위해 기본 제공되는 `GITHUB_TOKEN`을 사용합니다. 수동으로 Personal Access Token (PAT)을 생성할 **필요는 없지만**, 기본 토큰에 올바른 권한이 있는지 **반드시** 확인해야 합니다:

1. 저장소의 **Settings** -> **Actions** -> **General**로 이동합니다.
2. **Workflow permissions** 섹션으로 아래로 스크롤합니다.
3. **Read and write permissions**를 선택합니다.
4. **Save**를 클릭합니다.
5. 워크플로우 YAML에서 사용 예시에 표시된 것처럼 `${{ secrets.GITHUB_TOKEN }}`을 `github_token` 입력으로 전달하기만 하면 됩니다.

## 📄 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) 파일을 참조하세요.