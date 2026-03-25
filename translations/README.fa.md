> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# مترجم Gemini README


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

یک GitHub Action که با استفاده از API جمینای (Gemini)، به طور خودکار فایل `README.md` شما را به چندین زبان ترجمه می‌کند. این ابزار به صورت هوشمندانه یک منوی ناوبری زبان با لینک‌های متقابل را در تمامی فایل‌ها قرار داده و تغییرات را به شکل خودکار کامیت می‌کند.

## 🚀 ویژگی‌ها
* **پشتیبانی از چند زبان:** تولید فایل‌های README برای چندین زبان تنها در یک بار اجرا.
* **ناوبری خودکار:** به صورت خودکار یک منوی استاندارد برای تغییر زبان را در بالای فایل‌های شما درج و نگهداری می‌کند (قابل غیرفعال‌سازی). هوش مصنوعی استایل آن را نیز به صورت خودکار تنظیم می‌کند!
* **استایل‌دهی سفارشی:** می‌توانید یک پارامتر استایل سفارشی برای منو ارائه دهید تا هوش مصنوعی تغییردهنده زبان را دقیقاً به شکلی که شما می‌خواهید قالب‌بندی کند.
* **ردیابی توکن:** ارائه آمار مربوط به استفاده از توکن‌های جمینای.

## 🛠 نحوه استفاده

یک فایل گردش کار (workflow) ایجاد کنید (به عنوان مثال، `.github/workflows/translate.yml`):

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

## 📥 ورودی‌ها

| ورودی | الزامی | پیش‌فرض | توضیحات |
| --- | --- | --- | --- |
| `api_key` | بله |  | کلید API گوگل جمینای (Google Gemini) شما. |
| `github_token` | بله |  | توکن استاندارد گیت‌هاب (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | بله |  | زبان‌های هدف که با کاما از هم جدا شده‌اند (به عنوان مثال `ru, es`). |
| `output_dir` | خیر | | پوشه‌ای برای ذخیره فایل‌های ترجمه شده. پیش‌فرض، پوشه فایل مبدأ است. |
| `add_language_menu` | خیر | `true` | برای غیرفعال کردن تولید خودکار منوی زبان، آن را روی `false` تنظیم کنید. |
| `use_absolute_links`| خیر | `true` | برای استفاده از پیوندهای نسبی به جای URL های مطلق گیت‌هاب در منوهای زبان تولید شده، آن را روی `false` تنظیم کنید. |
| `menu_style` | خیر | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | استایل مرجعی که هوش مصنوعی هنگام تولید یک منوی زبان جدید از آن استفاده می‌کند. |
| `commit_message` | خیر | `docs: auto-translate README via Gemini` | متنی که برای پیام کامیت git استفاده می‌شود. |
| `model` | خیر | `gemini-3.1-pro-preview` | مدل جمینای که مورد استفاده قرار می‌گیرد. |
| `source_file` | خیر | `README.md` | فایل پایه‌ای که قرار است ترجمه شود. |

## 📤 خروجی‌ها

| خروجی | توضیحات |
| --- | --- |
| `total_tokens_used` | تعداد کل توکن‌های پردازش شده. |
| `input_tokens_used` | تعداد توکن‌های استفاده شده در پرامپت‌های ورودی. |
| `output_tokens_used` | تعداد توکن‌های تولید شده در پاسخ‌ها. |
| `duration_seconds` | کل زمان پردازش به ثانیه. |

## 🔑 نحوه دریافت کلید API گوگل جمینای

برای استفاده از این اکشن، به یک کلید API رایگان از Google AI Studio نیاز دارید:

1. به [Google AI Studio](https://aistudio.google.com/) بروید.
2. با حساب کاربری گوگل خود وارد شوید.
3. در منوی ناوبری سمت چپ، روی **Get API key** کلیک کنید.
4. روی دکمه **Create API key** کلیک کنید.
5. کلید تولید شده را کپی کنید.
6. به مخزن (repository) گیت‌هاب خود بروید -> **Settings** -> **Secrets and variables** -> **Actions**.
7. روی **New repository secret** کلیک کنید، نام آن را `GEMINI_API_KEY` قرار دهید، کلید کپی شده را در فیلد Secret وارد کنید و ذخیره نمایید.

## 🔑 نحوه پیکربندی توکن استاندارد گیت‌هاب

این اکشن از توکن داخلی `GITHUB_TOKEN` برای پوش کردن (push) کامیت‌ها استفاده می‌کند. شما **نیازی ندارید** یک Personal Access Token (PAT) به صورت دستی ایجاد کنید، اما **باید** اطمینان حاصل کنید که توکن پیش‌فرض مجوزهای صحیحی را دارا باشد:

1. به مخزن خود بروید: **Settings** -> **Actions** -> **General**.
2. به پایین اسکرول کنید تا به بخش **Workflow permissions** برسید.
3. گزینه **Read and write permissions** را انتخاب کنید.
4. روی **Save** کلیک کنید.
5. در فایل YAML گردش کار (workflow) خود، به سادگی `${{ secrets.GITHUB_TOKEN }}` را به ورودی `github_token` پاس دهید (همانطور که در مثال نحوه استفاده نشان داده شده است).

## 📄 لایسنس (مجوز)

این پروژه تحت مجوز MIT منتشر شده است - برای جزئیات بیشتر به فایل [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) مراجعه کنید.