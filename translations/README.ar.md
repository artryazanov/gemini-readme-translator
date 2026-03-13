> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# مترجم Gemini لملفات README


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

إجراء GitHub (GitHub Action) يترجم ملف `README.md` تلقائيًا إلى لغات متعددة باستخدام واجهة برمجة تطبيقات Gemini (Gemini API). يقوم بذكاء بإدراج قائمة تنقل مترابطة للغات في جميع الملفات ويقوم بتنفيذ (commit) التغييرات تلقائيًا.

## 🚀 الميزات
* **دعم لغات متعددة:** إنشاء ملفات README بلغات متعددة في تشغيل واحد.
* **التنقل التلقائي:** يقوم بإدراج قائمة قياسية لتبديل اللغة تلقائيًا ويحافظ عليها في أعلى ملفاتك (يمكن تعطيلها). يقوم الذكاء الاصطناعي بتنسيقها تلقائيًا!
* **تنسيق مخصص:** يمكنك توفير معلمة نمط مخصصة للقائمة بحيث يقوم الذكاء الاصطناعي بتنسيق مبدل اللغة تمامًا كما تريد.
* **تتبع الرموز (Tokens):** يعرض إحصائيات استخدام الرموز في Gemini.

## 🛠 الاستخدام

أنشئ ملف سير عمل (على سبيل المثال، `.github/workflows/translate.yml`):

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

## 📥 المدخلات

| المدخل | مطلوب | الافتراضي | الوصف |
| --- | --- | --- | --- |
| `api_key` | نعم |  | مفتاح Google Gemini API الخاص بك. |
| `github_token` | نعم |  | رمز GitHub القياسي (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | نعم |  | اللغات المستهدفة مفصولة بفواصل (مثل `ru, es`). |
| `output_dir` | لا | | الدليل لحفظ الملفات المترجمة. الافتراضي هو دليل الملف المصدر. |
| `add_language_menu` | لا | `true` | عيّن إلى `false` لتعطيل الإنشاء التلقائي لقائمة اللغات. |
| `menu_style` | لا | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | النمط المرجعي الذي يستخدمه الذكاء الاصطناعي عند إنشاء قائمة لغات جديدة. |
| `commit_message` | لا | `docs: auto-translate README via Gemini` | النص المستخدم لرسالة التنفيذ (commit) في git. |
| `model` | لا | `gemini-3.1-pro-preview` | نموذج Gemini المراد استخدامه. |
| `source_file` | لا | `README.md` | الملف الأساسي المراد ترجمته. |

## 📤 المخرجات

| المخرج | الوصف |
| --- | --- |
| `total_tokens_used` | إجمالي عدد الرموز (tokens) التي تمت معالجتها. |
| `input_tokens_used` | عدد الرموز في مطالبات الإدخال. |
| `output_tokens_used` | عدد الرموز الناتجة في الردود. |
| `duration_seconds` | إجمالي وقت المعالجة بالثواني. |

## 🔑 كيفية الحصول على مفتاح Google Gemini API

لاستخدام هذا الإجراء، تحتاج إلى مفتاح API مجاني من Google AI Studio:

1. اذهب إلى [Google AI Studio](https://aistudio.google.com/).
2. قم بتسجيل الدخول باستخدام حساب Google الخاص بك.
3. في قائمة التنقل اليسرى، انقر على **Get API key**.
4. انقر على زر **Create API key**.
5. انسخ المفتاح الذي تم إنشاؤه.
6. اذهب إلى مستودع GitHub الخاص بك -> **Settings** -> **Secrets and variables** -> **Actions**.
7. انقر على **New repository secret**، وقم بتسميته `GEMINI_API_KEY`، ثم الصق المفتاح في حقل Secret، واحفظ.

## 🔑 كيفية تكوين رمز GitHub القياسي (Standard GitHub Token)

يستخدم هذا الإجراء الرمز المدمج `GITHUB_TOKEN` لدفع (push) التنفيذات (commits). أنت **لست** بحاجة إلى إنشاء رمز وصول شخصي (PAT) يدويًا، ولكن **يجب** عليك التأكد من أن الرمز الافتراضي يمتلك الأذونات الصحيحة:

1. اذهب إلى مستودعك **Settings** -> **Actions** -> **General**.
2. قم بالتمرير لأسفل إلى قسم **Workflow permissions**.
3. حدد **Read and write permissions**.
4. انقر على **Save**.
5. في ملف YAML الخاص بسير العمل، قم ببساطة بتمرير `${{ secrets.GITHUB_TOKEN }}` إلى المدخل `github_token` (كما هو موضح في مثال الاستخدام).

## 📄 الترخيص

هذا المشروع مرخص بموجب ترخيص MIT - راجع ملف [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) للحصول على التفاصيل.