> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

ایک گٹ ہب ایکشن (GitHub Action) جو Gemini API کا استعمال کرتے ہوئے خودکار طور پر آپ کے `README.md` کا متعدد زبانوں میں ترجمہ کرتا ہے۔ یہ تمام فائلوں میں ایک مربوط زبان کے نیویگیشن مینو کا ذہانت سے اضافہ کرتا ہے اور تبدیلیوں کو خودکار طور پر کمٹ (commit) کرتا ہے۔

## 🚀 خصوصیات
* **متعدد زبانوں کی معاونت:** ایک ہی عمل میں کئی زبانوں کے لیے README تیار کریں۔
* **خودکار نیویگیشن:** آپ کی فائلوں کے اوپری حصے میں زبان تبدیل کرنے کا ایک معیاری مینو خود بخود شامل اور برقرار رکھتا ہے (اسے غیر فعال بھی کیا جا سکتا ہے)۔ AI اسے خود بخود اسٹائل کرتا ہے!
* **اپنی مرضی کا اسٹائل:** آپ مینو کے اسٹائل کا ایک حسب ضرورت پیرامیٹر فراہم کر سکتے ہیں تاکہ AI زبان کے سوئچر (switcher) کو بالکل ویسا ہی فارمیٹ کرے جیسا آپ چاہتے ہیں۔
* **ٹوکن ٹریکنگ:** یہ Gemini ٹوکن کے استعمال کے اعداد و شمار بھی آؤٹ پٹ کرتا ہے۔

## 🛠 طریقہ استعمال

ایک ورک فلو (workflow) فائل بنائیں (مثلاً، `.github/workflows/translate.yml`):

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

## 📥 ان پٹس (Inputs)

| ان پٹ | درکار | ڈیفالٹ | تفصیل |
| --- | --- | --- | --- |
| `api_key` | ہاں |  | آپ کی Google Gemini API کلید (Key)۔ |
| `github_token` | ہاں |  | معیاری GitHub ٹوکن (`${{ secrets.GITHUB_TOKEN }}`)۔ |
| `languages` | ہاں |  | کوما سے الگ کی گئی ٹارگٹ زبانیں (مثال کے طور پر `ru, es`)۔ |
| `output_dir` | نہیں | | ترجمہ شدہ فائلوں کو محفوظ کرنے کی ڈائرکٹری۔ ڈیفالٹ کے طور پر سورس فائل کی ڈائرکٹری استعمال ہوتی ہے۔ |
| `add_language_menu` | نہیں | `true` | زبان کے مینو کی خودکار تخلیق کو غیر فعال کرنے کے لیے اسے `false` پر سیٹ کریں۔ |
| `use_absolute_links`| نہیں | `true` | اس کو `false` پر سیٹ کریں تاکہ تیار شدہ زبان کے مینو میں مکمل GitHub URLs کے بجائے رشتہ دار لنکس کا استعمال کیا جا سکے۔ |
| `menu_style` | نہیں | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | وہ حوالہ جاتی اسٹائل جسے AI نیا زبان کا مینو بناتے وقت استعمال کرتا ہے۔ |
| `commit_message` | نہیں | `docs: auto-translate README via Gemini` | گٹ کمٹ (git commit) میسج کے لیے استعمال ہونے والا متن۔ |
| `model` | نہیں | `gemini-3.1-pro-preview` | استعمال کرنے کے لیے Gemini ماڈل۔ |
| `source_file` | نہیں | `README.md` | ترجمہ کرنے کے لیے بنیادی فائل۔ |

## 📤 آؤٹ پٹس (Outputs)

| آؤٹ پٹ | تفصیل |
| --- | --- |
| `total_tokens_used` | پروسیس کیے گئے ٹوکنز کی کل تعداد۔ |
| `input_tokens_used` | ان پٹ پرامپٹس (prompts) میں ٹوکنز کی تعداد۔ |
| `output_tokens_used` | جوابات میں تیار کردہ ٹوکنز کی تعداد۔ |
| `duration_seconds` | سیکنڈز میں پروسیسنگ کا کل وقت۔ |

## 🔑 گوگل جیمنی (Google Gemini) API کلید کیسے حاصل کریں

اس ایکشن کو استعمال کرنے کے لیے، آپ کو Google AI Studio سے ایک مفت API کلید درکار ہے:

1. [Google AI Studio](https://aistudio.google.com/) پر جائیں۔
2. اپنے گوگل اکاؤنٹ کے ساتھ سائن ان (Sign in) کریں۔
3. بائیں جانب موجود نیویگیشن مینو میں، **Get API key** پر کلک کریں۔
4. **Create API key** بٹن پر کلک کریں۔
5. تیار شدہ کلید کو کاپی (Copy) کریں۔
6. اپنی GitHub ریپوزٹری کی **Settings** -> **Secrets and variables** -> **Actions** میں جائیں۔
7. **New repository secret** پر کلک کریں، اسے `GEMINI_API_KEY` کا نام دیں، اپنی کلید کو سیکریٹ (Secret) فیلڈ میں پیسٹ کریں اور محفوظ (save) کریں۔

## 🔑 معیاری GitHub ٹوکن کو کیسے کنفیگر (Configure) کریں

یہ ایکشن کمٹس (commits) کو پش کرنے کے لیے بلٹ ان `GITHUB_TOKEN` کا استعمال کرتا ہے۔ آپ کو دستی طور پر پرسنل ایکسس ٹوکن (PAT) بنانے کی **ضرورت نہیں** ہے، لیکن آپ کو یہ یقینی بنانا **لازمی** ہے کہ ڈیفالٹ ٹوکن کے پاس درست پرمیشنز (permissions) موجود ہیں:

1. اپنی ریپوزٹری کی **Settings** -> **Actions** -> **General** میں جائیں۔
2. نیچے اسکرول کر کے **Workflow permissions** سیکشن تک جائیں۔
3. **Read and write permissions** کو منتخب کریں۔
4. **Save** پر کلک کریں۔
5. اپنے ورک فلو YAML میں، بس `${{ secrets.GITHUB_TOKEN }}` کو `github_token` ان پٹ میں پاس کریں (جیسا کہ استعمال کی مثال میں دکھایا گیا ہے)۔

## 📄 لائسنس

یہ پروجیکٹ MIT لائسنس کے تحت لائسنس یافتہ ہے - مزید تفصیلات کے لیے [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) فائل دیکھیں۔