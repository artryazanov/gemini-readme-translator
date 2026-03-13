> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

এটি একটি গিটহাব অ্যাকশন (GitHub Action) যা জেমিনি এপিআই (Gemini API) ব্যবহার করে স্বয়ংক্রিয়ভাবে আপনার `README.md` ফাইলটিকে একাধিক ভাষায় অনুবাদ করে। এটি বুদ্ধিমত্তার সাথে সমস্ত ফাইলে ক্রস-লিঙ্কযুক্ত ভাষা নেভিগেশন মেনু যুক্ত করে এবং স্বয়ংক্রিয়ভাবে পরিবর্তনগুলি কমিট করে।

## 🚀 বৈশিষ্ট্যসমূহ
* **একাধিক ভাষার সাপোর্ট:** এক রান-এ একাধিক ভাষার জন্য README তৈরি করুন।
* **অটো-নেভিগেশন:** স্বয়ংক্রিয়ভাবে আপনার ফাইলগুলোর উপরের অংশে একটি স্ট্যান্ডার্ড ল্যাঙ্গুয়েজ সুইচার মেনু ইনসার্ট এবং মেইনটেইন করে (ডিজেবল করা যায়)। এআই স্বয়ংক্রিয়ভাবে এটি স্টাইল করে!
* **কাস্টম স্টাইলিং:** আপনি একটি কাস্টম মেনু স্টাইল প্যারামিটার প্রদান করতে পারেন যাতে এআই আপনার পছন্দমতো ল্যাঙ্গুয়েজ সুইচার ফর্ম্যাট করে।
* **টোকেন ট্র্যাকিং:** জেমিনি টোকেন ব্যবহারের পরিসংখ্যান আউটপুট করে।

## 🛠 ব্যবহারবিধি

একটি ওয়ার্কফ্লো ফাইল তৈরি করুন (যেমন- `.github/workflows/translate.yml`):

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

## 📥 ইনপুটসমূহ

| ইনপুট | আবশ্যিক | ডিফল্ট | বিবরণ |
| --- | --- | --- | --- |
| `api_key` | হ্যাঁ |  | আপনার গুগল জেমিনি এপিআই (Google Gemini API) কী। |
| `github_token` | হ্যাঁ |  | স্ট্যান্ডার্ড গিটহাব টোকেন (`${{ secrets.GITHUB_TOKEN }}`)। |
| `languages` | হ্যাঁ |  | কমা দ্বারা পৃথক করা টার্গেট ভাষা (যেমন `ru, es`)। |
| `output_dir` | না | | অনুদিত ফাইলগুলো সংরক্ষণের ডিরেক্টরি। ডিফল্টরূপে সোর্স ফাইলের ডিরেক্টরি ব্যবহৃত হয়। |
| `add_language_menu` | না | `true` | ভাষা মেনুর অটো-জেনারেশন ডিজেবল করতে `false` সেট করুন। |
| `menu_style` | না | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | নতুন ভাষা মেনু জেনারেট করার সময় এআই যে রেফারেন্স স্টাইলটি ব্যবহার করে। |
| `commit_message` | না | `docs: auto-translate README via Gemini` | গিট কমিট মেসেজের জন্য ব্যবহৃত টেক্সট। |
| `model` | না | `gemini-3.1-pro-preview` | ব্যবহারের জন্য জেমিনি মডেল। |
| `source_file` | না | `README.md` | অনুবাদ করার জন্য বেস ফাইল। |

## 📤 আউটপুটসমূহ

| আউটপুট | বিবরণ |
| --- | --- |
| `total_tokens_used` | প্রক্রিয়াকৃত মোট টোকেনের সংখ্যা। |
| `input_tokens_used` | ইনপুট প্রম্পটে ব্যবহৃত টোকেনের সংখ্যা। |
| `output_tokens_used` | রেসপন্সে জেনারেট হওয়া টোকেনের সংখ্যা। |
| `duration_seconds` | সেকেন্ডে মোট প্রক্রিয়াকরণের সময়। |

## 🔑 কীভাবে গুগল জেমিনি এপিআই কী (Google Gemini API Key) পাবেন

এই অ্যাকশনটি ব্যবহার করতে, আপনার গুগল এআই স্টুডিও (Google AI Studio) থেকে একটি বিনামূল্যের API key প্রয়োজন:

১. [Google AI Studio](https://aistudio.google.com/)-তে যান।
২. আপনার গুগল অ্যাকাউন্ট দিয়ে সাইন ইন করুন।
৩. বামদিকের নেভিগেশন মেনু থেকে **Get API key**-তে ক্লিক করুন।
৪. **Create API key** বাটনে ক্লিক করুন।
৫. জেনারেট হওয়া কী (key) কপি করুন।
৬. আপনার গিটহাব রিপোজিটরিতে যান -> **Settings** -> **Secrets and variables** -> **Actions**।
৭. **New repository secret**-এ ক্লিক করুন, এর নাম দিন `GEMINI_API_KEY`, Secret ফিল্ডে আপনার কী-টি পেস্ট করুন এবং সেভ করুন।

## 🔑 কীভাবে স্ট্যান্ডার্ড গিটহাব টোকেন (Standard GitHub Token) কনফিগার করবেন

কমিট পুশ করার জন্য এই অ্যাকশনটি বিল্ট-ইন `GITHUB_TOKEN` ব্যবহার করে। আপনাকে ম্যানুয়ালি কোনো পার্সোনাল অ্যাক্সেস টোকেন (PAT) তৈরি করতে **হবে না**, তবে আপনাকে **অবশ্যই** নিশ্চিত করতে হবে যে ডিফল্ট টোকেনটির সঠিক পারমিশন রয়েছে:

১. আপনার রিপোজিটরির **Settings** -> **Actions** -> **General**-এ যান।
২. স্ক্রল করে **Workflow permissions** সেকশনে যান।
৩. **Read and write permissions** নির্বাচন করুন।
৪. **Save**-এ ক্লিক করুন।
৫. আপনার ওয়ার্কফ্লো YAML-এ, `github_token` ইনপুটে সহজভাবে `${{ secrets.GITHUB_TOKEN }}` পাস করুন (যেমনটি ব্যবহারের উদাহরণে দেখানো হয়েছে)।

## 📄 লাইসেন্স

এই প্রজেক্টটি এমআইটি লাইসেন্সের (MIT License) অধীনে লাইসেন্সকৃত - বিস্তারিত তথ্যের জন্য [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ফাইলটি দেখুন।