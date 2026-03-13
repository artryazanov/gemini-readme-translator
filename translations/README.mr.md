> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

एक GitHub Action जे Gemini API चा वापर करून तुमच्या `README.md` चे अनेक भाषांमध्ये आपोआप भाषांतर करते. हे सर्व फाईल्समध्ये हुशारीने एक क्रॉस-लिंक्ड भाषा नेव्हिगेशन मेनू समाविष्ट करते आणि बदल आपोआप कमिट करते.

## 🚀 वैशिष्ट्ये
* **बहु-भाषिक समर्थन (Multi-Language Support):** एकाच वेळी अनेक भाषांसाठी README तयार करा.
* **ऑटो-नेव्हिगेशन (Auto-Navigation):** तुमच्या फाईल्सच्या वरच्या बाजूला एक प्रमाणित भाषा बदलण्याचा मेनू (language switcher menu) आपोआप समाविष्ट करते आणि मेंटेन करते (हे बंद देखील करता येते). AI याला आपोआप स्टाईल करते!
* **कस्टम स्टायलिंग (Custom Styling):** तुम्ही एक कस्टम मेनू स्टाईल पॅरामीटर देऊ शकता जेणेकरून AI भाषा स्विचरला तुमच्या इच्छेनुसार अचूक फॉरमॅट करेल.
* **टोकन ट्रॅकिंग (Token Tracking):** जेमिनी (Gemini) टोकन वापराची आकडेवारी आउटपुट करते.

## 🛠 वापर

एक वर्कफ्लो फाईल तयार करा (उदा., `.github/workflows/translate.yml`):

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

## 📥 इनपुट्स (Inputs)

| इनपुट (Input) | आवश्यक (Required) | डीफॉल्ट (Default) | वर्णन (Description) |
| --- | --- | --- | --- |
| `api_key` | होय |  | तुमची Google Gemini API की. |
| `github_token` | होय |  | प्रमाणित GitHub टोकन (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | होय |  | स्वल्पविरामाने (comma) वेगळ्या केलेल्या लक्षित भाषा (उदा. `ru, es`). |
| `output_dir` | नाही | | भाषांतरित फाईल्स सेव्ह करण्यासाठी डिरेक्टरी. डीफॉल्टनुसार मूळ फाईलची डिरेक्टरी वापरली जाते. |
| `add_language_menu` | नाही | `true` | भाषा मेनूचे आपोआप तयार होणे अक्षम (disable) करण्यासाठी `false` वर सेट करा. |
| `menu_style` | नाही | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | नवीन भाषा मेनू तयार करताना AI वापरत असलेली संदर्भ स्टाईल. |
| `commit_message` | नाही | `docs: auto-translate README via Gemini` | गिट कमिट (git commit) संदेशासाठी वापरलेला मजकूर. |
| `model` | नाही | `gemini-3.1-pro-preview` | वापरण्यासाठीचे Gemini मॉडेल. |
| `source_file` | नाही | `README.md` | भाषांतर करण्यासाठीची मूळ फाईल. |

## 📤 आउटपुट्स (Outputs)

| आउटपुट (Output) | वर्णन (Description) |
| --- | --- |
| `total_tokens_used` | प्रक्रिया केलेल्या एकूण टोकन्सची संख्या. |
| `input_tokens_used` | इनपुट प्रॉम्प्ट्समधील टोकन्सची संख्या. |
| `output_tokens_used` | प्रतिसादांमध्ये (responses) तयार झालेल्या टोकन्सची संख्या. |
| `duration_seconds` | एकूण प्रक्रियेचा वेळ सेकंदांमध्ये. |

## 🔑 Google Gemini API की कशी मिळवायची?

ही Action वापरण्यासाठी, तुम्हाला Google AI Studio कडून एक मोफत API की आवश्यक आहे:

1. [Google AI Studio](https://aistudio.google.com/) वर जा.
2. तुमच्या Google खात्यासह साईन इन करा.
3. डाव्या बाजूच्या नेव्हिगेशन मेनूमध्ये, **Get API key** वर क्लिक करा.
4. **Create API key** बटणावर क्लिक करा.
5. तयार केलेली की कॉपी करा.
6. तुमच्या GitHub रिपॉझिटरीवर जा -> **Settings** -> **Secrets and variables** -> **Actions**.
7. **New repository secret** वर क्लिक करा, त्याला `GEMINI_API_KEY` नाव द्या, तुमची की सिक्रेट (Secret) फील्डमध्ये पेस्ट करा आणि सेव्ह करा.

## 🔑 प्रमाणित GitHub टोकन कसे कॉन्फिगर करायचे?

ही Action कमिट्स पुश करण्यासाठी अंगभूत (built-in) `GITHUB_TOKEN` वापरते. तुम्हाला मॅन्युअली पर्सनल ऍक्सेस टोकन (PAT) तयार करण्याची **गरज नाही**, परंतु तुम्ही हे **निश्चित केले पाहिजे** की डीफॉल्ट टोकनला योग्य परवानग्या आहेत:

1. तुमच्या रिपॉझिटरीच्या **Settings** -> **Actions** -> **General** वर जा.
2. खाली स्क्रोल करून **Workflow permissions** विभागात जा.
3. **Read and write permissions** निवडा.
4. **Save** वर क्लिक करा.
5. तुमच्या वर्कफ्लो YAML मध्ये, साध्या पद्धतीने `${{ secrets.GITHUB_TOKEN }}` हे `github_token` इनपुटमध्ये पास करा (वापरण्याच्या उदाहरणात दाखवल्याप्रमाणे).

## 📄 परवाना (License)

हा प्रोजेक्ट MIT परवान्याअंतर्गत परवानाकृत आहे - अधिक माहितीसाठी [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) फाईल पहा.