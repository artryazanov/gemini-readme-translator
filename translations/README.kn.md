> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README ಅನುವಾದಕ (Translator)


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

ಇದು Gemini API ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ `README.md` ಅನ್ನು ಬಹು ಭಾಷೆಗಳಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಿಸುವ GitHub Action ಆಗಿದೆ. ಇದು ಎಲ್ಲಾ ಫೈಲ್‌ಗಳಿಗೆ ಅಡ್ಡ-ಸಂಪರ್ಕಿತ (cross-linked) ಭಾಷಾ ನ್ಯಾವಿಗೇಶನ್ ಮೆನುವನ್ನು ಬುದ್ಧಿವಂತಿಕೆಯಿಂದ ಸೇರಿಸುತ್ತದೆ ಮತ್ತು ಬದಲಾವಣೆಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಮಿಟ್ (commit) ಮಾಡುತ್ತದೆ.

## 🚀 ವೈಶಿಷ್ಟ್ಯಗಳು
* **ಬಹು-ಭಾಷಾ ಬೆಂಬಲ:** ಒಂದೇ ಓಟದಲ್ಲಿ (run) ಬಹು ಭಾಷೆಗಳಿಗೆ README ಗಳನ್ನು ರಚಿಸಿ.
* **ಸ್ವಯಂ-ನ್ಯಾವಿಗೇಶನ್:** ನಿಮ್ಮ ಫೈಲ್‌ಗಳ ಮೇಲ್ಭಾಗದಲ್ಲಿ ಪ್ರಮಾಣಿತ ಭಾಷೆ ಬದಲಾಯಿಸುವ (switcher) ಮೆನುವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೇರಿಸುತ್ತದೆ ಮತ್ತು ನಿರ್ವಹಿಸುತ್ತದೆ (ಇದನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಬಹುದು). AI ಇದನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸುತ್ತದೆ!
* **ಕಸ್ಟಮ್ ಸ್ಟೈಲಿಂಗ್:** ನೀವು ಕಸ್ಟಮ್ ಮೆನು ಸ್ಟೈಲ್ ಪ್ಯಾರಾಮೀಟರ್ ಅನ್ನು ಒದಗಿಸಬಹುದು, ಇದರಿಂದ AI ಭಾಷೆ ಬದಲಿಸುವ ಮೆನುವನ್ನು ನಿಮಗೆ ಬೇಕಾದ ರೀತಿಯಲ್ಲಿಯೇ ವಿನ್ಯಾಸಗೊಳಿಸುತ್ತದೆ.
* **ಟೋಕನ್ ಟ್ರ್ಯಾಕಿಂಗ್:** Gemini ಟೋಕನ್ ಬಳಕೆಯ ಅಂಕಿಅಂಶಗಳನ್ನು ಔಟ್‌ಪುಟ್ ಮಾಡುತ್ತದೆ.

## 🛠 ಬಳಕೆ

ಒಂದು ವರ್ಕ್‌ಫ್ಲೋ (workflow) ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ (ಉದಾ: `.github/workflows/translate.yml`):

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

## 📥 ಇನ್‌ಪುಟ್‌ಗಳು

| ಇನ್‌ಪುಟ್ | ಕಡ್ಡಾಯ | ಡೀಫಾಲ್ಟ್ | ವಿವರಣೆ |
| --- | --- | --- | --- |
| `api_key` | ಹೌದು |  | ನಿಮ್ಮ Google Gemini API ಕೀ. |
| `github_token` | ಹೌದು |  | ಪ್ರಮಾಣಿತ GitHub ಟೋಕನ್ (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | ಹೌದು |  | ಅಲ್ಪವಿರಾಮದಿಂದ (comma) ಬೇರ್ಪಡಿಸಲಾದ ಗುರಿ ಭಾಷೆಗಳು (ಉದಾಹರಣೆಗೆ `ru, es`). |
| `output_dir` | ಇಲ್ಲ | | ಅನುವಾದಿತ ಫೈಲ್‌ಗಳನ್ನು ಉಳಿಸುವ ಡೈರೆಕ್ಟರಿ. ಡೀಫಾಲ್ಟ್ ಆಗಿ ಮೂಲ ಫೈಲ್‌ನ ಡೈರೆಕ್ಟರಿಗೆ ಉಳಿಸುತ್ತದೆ. |
| `add_language_menu` | ಇಲ್ಲ | `true` | ಭಾಷಾ ಮೆನುವಿನ ಸ್ವಯಂ-ರಚನೆಯನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲು `false` ಎಂದು ಹೊಂದಿಸಿ. |
| `menu_style` | ಇಲ್ಲ | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | ಹೊಸ ಭಾಷಾ ಮೆನುವನ್ನು ರಚಿಸುವಾಗ AI ಬಳಸುವ ಉಲ್ಲೇಖಿತ (reference) ಶೈಲಿ. |
| `commit_message` | ಇಲ್ಲ | `docs: auto-translate README via Gemini` | git ಕಮಿಟ್ ಸಂದೇಶಕ್ಕಾಗಿ ಬಳಸುವ ಪಠ್ಯ. |
| `model` | ಇಲ್ಲ | `gemini-3.1-pro-preview` | ಬಳಸಬೇಕಾದ Gemini ಮಾಡೆಲ್. |
| `source_file` | ಇಲ್ಲ | `README.md` | ಅನುವಾದಿಸಬೇಕಾದ ಮೂಲ ಫೈಲ್. |

## 📤 ಔಟ್‌ಪುಟ್‌ಗಳು

| ಔಟ್‌ಪುಟ್ | ವಿವರಣೆ |
| --- | --- |
| `total_tokens_used` | ಸಂಸ್ಕರಿಸಿದ (processed) ಒಟ್ಟು ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆ. |
| `input_tokens_used` | ಇನ್‌ಪುಟ್ ಪ್ರಾಂಪ್ಟ್‌ಗಳಲ್ಲಿರುವ ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆ. |
| `output_tokens_used` | ಪ್ರತಿಕ್ರಿಯೆಗಳಲ್ಲಿ (responses) ರಚಿಸಲಾದ ಟೋಕನ್‌ಗಳ ಸಂಖ್ಯೆ. |
| `duration_seconds` | ಸೆಕೆಂಡುಗಳಲ್ಲಿ ತೆಗೆದುಕೊಂಡ ಒಟ್ಟು ಪ್ರಕ್ರಿಯೆಯ ಸಮಯ. |

## 🔑 Google Gemini API ಕೀಯನ್ನು ಪಡೆಯುವುದು ಹೇಗೆ

ಈ ಆಕ್ಷನ್ ಅನ್ನು ಬಳಸಲು, ನಿಮಗೆ Google AI ಸ್ಟುಡಿಯೋದಿಂದ ಉಚಿತ API ಕೀಯ ಅಗತ್ಯವಿದೆ:

1. [Google AI Studio](https://aistudio.google.com/) ಗೆ ಹೋಗಿ.
2. ನಿಮ್ಮ Google ಖಾತೆಯೊಂದಿಗೆ ಸೈನ್-ಇನ್ ಮಾಡಿ.
3. ಎಡಭಾಗದ ನ್ಯಾವಿಗೇಶನ್ ಮೆನುವಿನಲ್ಲಿ, **Get API key** ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
4. **Create API key** ಬಟನ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ರಚಿಸಲಾದ ಕೀಯನ್ನು ಕಾಪಿ (copy) ಮಾಡಿ.
6. ನಿಮ್ಮ GitHub ರೆಪಾಸಿಟರಿಗೆ ಹೋಗಿ -> **Settings** -> **Secrets and variables** -> **Actions**.
7. **New repository secret** ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ, ಅದಕ್ಕೆ `GEMINI_API_KEY` ಎಂದು ಹೆಸರಿಸಿ, ನಿಮ್ಮ ಕೀಯನ್ನು Secret ಫೀಲ್ಡ್‌ನಲ್ಲಿ ಪೇಸ್ಟ್ ಮಾಡಿ ಮತ್ತು ಸೇವ್ (save) ಮಾಡಿ.

## 🔑 ಪ್ರಮಾಣಿತ GitHub ಟೋಕನ್ ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು ಹೇಗೆ

ಕಮಿಟ್‌ಗಳನ್ನು ಪುಶ್ ಮಾಡಲು ಈ ಆಕ್ಷನ್ ಅಂತರ್ನಿರ್ಮಿತ (built-in) `GITHUB_TOKEN` ಅನ್ನು ಬಳಸುತ್ತದೆ. ನೀವು ಮ್ಯಾನುಯಲ್ ಆಗಿ ಪರ್ಸನಲ್ ಆಕ್ಸೆಸ್ ಟೋಕನ್ (PAT) ಅನ್ನು ರಚಿಸುವ ಅಗತ್ಯವಿಲ್ಲ, ಆದರೆ ಡೀಫಾಲ್ಟ್ ಟೋಕನ್‌ಗೆ ಸರಿಯಾದ ಅನುಮತಿಗಳಿವೆಯೇ ಎಂಬುದನ್ನು ನೀವು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬೇಕು:

1. ನಿಮ್ಮ ರೆಪಾಸಿಟರಿಯ **Settings** -> **Actions** -> **General** ಗೆ ಹೋಗಿ.
2. ಕೆಳಗೆ ಸ್ಕ್ರಾಲ್ ಮಾಡಿ **Workflow permissions** ವಿಭಾಗಕ್ಕೆ ಹೋಗಿ.
3. **Read and write permissions** ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ.
4. **Save** ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ನಿಮ್ಮ ವರ್ಕ್‌ಫ್ಲೋ YAML ನಲ್ಲಿ, `github_token` ಇನ್‌ಪುಟ್‌ಗೆ ಕೇವಲ `${{ secrets.GITHUB_TOKEN }}` ಅನ್ನು ರವಾನಿಸಿ (ಬಳಕೆಯ ಉದಾಹರಣೆಯಲ್ಲಿ ತೋರಿಸಿರುವಂತೆ).

## 📄 ಪರವಾನಗಿ

ಈ ಪ್ರಾಜೆಕ್ಟ್ MIT ಪರವಾನಗಿಯ ಅಡಿಯಲ್ಲಿ ಪರವಾನಗಿ ಪಡೆದಿದೆ - ವಿವರಗಳಿಗಾಗಿ [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ಫೈಲ್ ಅನ್ನು ನೋಡಿ.