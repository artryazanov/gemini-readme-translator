> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

एक GitHub Action जो Gemini API का उपयोग करके आपके `README.md` को स्वचालित रूप से कई भाषाओं में अनुवाद करता है। यह बुद्धिमानी से सभी फ़ाइलों में एक क्रॉस-लिंक्ड भाषा नेविगेशन मेनू डालता है और परिवर्तनों को स्वचालित रूप से कमिट (commit) करता है।

## 🚀 विशेषताएँ
* **बहु-भाषा समर्थन (Multi-Language Support):** एक ही बार में कई भाषाओं के लिए README जनरेट करें।
* **ऑटो-नेविगेशन:** स्वचालित रूप से आपकी फ़ाइलों के शीर्ष पर एक मानक भाषा स्विचर मेनू सम्मिलित करता है और बनाए रखता है (इसे अक्षम किया जा सकता है)। AI इसे स्वचालित रूप से स्टाइल करता है!
* **कस्टम स्टाइलिंग:** आप एक कस्टम मेनू स्टाइल पैरामीटर प्रदान कर सकते हैं ताकि AI भाषा स्विचर को बिल्कुल उसी तरह फ़ॉर्मेट करे जैसा आप चाहते हैं।
* **टोकन ट्रैकिंग:** जेमिनी (Gemini) टोकन उपयोग के आँकड़े आउटपुट करता है।

## 🛠 उपयोग

एक वर्कफ़्लो फ़ाइल बनाएँ (उदा., `.github/workflows/translate.yml`):

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

## 📥 इनपुट

| इनपुट | आवश्यक | डिफ़ॉल्ट | विवरण |
| --- | --- | --- | --- |
| `api_key` | हाँ |  | आपकी Google Gemini API की (Key)। |
| `github_token` | हाँ |  | मानक GitHub टोकन (`${{ secrets.GITHUB_TOKEN }}`)। |
| `languages` | हाँ |  | अल्पविराम द्वारा अलग की गई लक्ष्य भाषाएँ (उदा. `ru, es`)। |
| `output_dir` | नहीं | | अनुवादित फ़ाइलों को सहेजने के लिए निर्देशिका। डिफ़ॉल्ट रूप से स्रोत फ़ाइल की निर्देशिका होती है। |
| `add_language_menu` | नहीं | `true` | भाषा मेनू के स्वतः-निर्माण को अक्षम करने के लिए `false` पर सेट करें। |
| `use_absolute_links`| नहीं | `true` | उत्पन्न भाषा मेनू में निरपेक्ष GitHub URL के बजाय सापेक्ष लिंक का उपयोग करने के लिए `false` पर सेट करें। |
| `menu_style` | नहीं | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | संदर्भ शैली जिसका AI नया भाषा मेनू जनरेट करते समय उपयोग करता है। |
| `commit_message` | नहीं | `docs: auto-translate README via Gemini` | git कमिट संदेश के लिए प्रयुक्त टेक्स्ट। |
| `model` | नहीं | `gemini-3.1-pro-preview` | उपयोग करने के लिए Gemini मॉडल। |
| `source_file` | नहीं | `README.md` | अनुवाद करने के लिए मूल (base) फ़ाइल। |

## 📤 आउटपुट

| आउटपुट | विवरण |
| --- | --- |
| `total_tokens_used` | संसाधित किए गए टोकन की कुल संख्या। |
| `input_tokens_used` | इनपुट प्रॉम्प्ट में टोकन की संख्या। |
| `output_tokens_used` | प्रतिक्रियाओं (responses) में जनरेट किए गए टोकन की संख्या। |
| `duration_seconds` | सेकंड में कुल प्रोसेसिंग समय। |

## 🔑 Google Gemini API की (Key) कैसे प्राप्त करें

इस एक्शन का उपयोग करने के लिए, आपको Google AI Studio से एक मुफ़्त API की (Key) की आवश्यकता होगी:

1. [Google AI Studio](https://aistudio.google.com/) पर जाएँ।
2. अपने Google खाते से साइन इन करें।
3. बाईं ओर के नेविगेशन मेनू में, **Get API key** पर क्लिक करें।
4. **Create API key** बटन पर क्लिक करें।
5. जनरेट की गई की (Key) को कॉपी करें।
6. अपनी GitHub रिपॉजिटरी पर जाएँ -> **Settings** -> **Secrets and variables** -> **Actions**।
7. **New repository secret** पर क्लिक करें, इसका नाम `GEMINI_API_KEY` रखें, अपनी की (Key) को Secret फ़ील्ड में पेस्ट करें, और सेव करें।

## 🔑 मानक GitHub टोकन कैसे कॉन्फ़िगर करें

यह एक्शन कमिट पुश करने के लिए इनबिल्ट `GITHUB_TOKEN` का उपयोग करता है। आपको मैन्युअल रूप से पर्सनल एक्सेस टोकन (PAT) बनाने की आवश्यकता **नहीं** है, लेकिन आपको यह सुनिश्चित **जरूर** करना चाहिए कि डिफ़ॉल्ट टोकन के पास सही अनुमतियाँ (permissions) हों:

1. अपनी रिपॉजिटरी की **Settings** -> **Actions** -> **General** में जाएँ।
2. **Workflow permissions** अनुभाग तक नीचे स्क्रॉल करें।
3. **Read and write permissions** चुनें।
4. **Save** पर क्लिक करें।
5. अपने वर्कफ़्लो YAML में, बस `${{ secrets.GITHUB_TOKEN }}` को `github_token` इनपुट में पास करें (जैसा कि उपयोग उदाहरण में दिखाया गया है)।

## 📄 लाइसेंस

यह प्रोजेक्ट MIT लाइसेंस के अंतर्गत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) फ़ाइल देखें।