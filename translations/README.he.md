> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# מתרגם README של Gemini


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

פעולת GitHub Action שמתרגמת אוטומטית את קובץ ה-`README.md` שלך למספר שפות באמצעות ממשק ה-API של Gemini. היא משלבת באופן חכם תפריט ניווט שפות המקושר בין כל הקבצים ומבצעת קומיט (commit) אוטומטי לשינויים.

## 🚀 תכונות
* **תמיכה מרובת שפות:** יצירת קבצי README למספר שפות בריצה אחת.
* **ניווט אוטומטי:** מוסיף ומתחזק אוטומטית תפריט החלפת שפות סטנדרטי בראש הקבצים שלך (ניתן לביטול). ה-AI מעצב אותו אוטומטית!
* **עיצוב מותאם אישית:** ניתן לספק פרמטר עיצוב תפריט מותאם אישית כדי שה-AI יעצב את מחליף השפות בדיוק כפי שתרצו.
* **מעקב אחר אסימונים (Tokens):** פולט סטטיסטיקות שימוש באסימונים של Gemini.

## 🛠 שימוש

צור קובץ workflow (לדוגמה, `.github/workflows/translate.yml`):

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

## 📥 קלטים (Inputs)

| קלט | חובה | ברירת מחדל | תיאור |
| --- | --- | --- | --- |
| `api_key` | כן |  | מפתח ה-API שלך ל-Google Gemini. |
| `github_token` | כן |  | אסימון GitHub סטנדרטי (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | כן |  | שפות היעד מופרדות בפסיקים (לדוגמה `ru, es`). |
| `output_dir` | לא | | תיקייה לשמירת הקבצים המתורגמים. ברירת המחדל היא התיקייה של קובץ המקור. |
| `add_language_menu` | לא | `true` | הגדר כ-`false` כדי להשבית יצירה אוטומטית של תפריט השפות. |
| `menu_style` | לא | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | סגנון ההתייחסות בו משתמש ה-AI בעת יצירת תפריט שפות חדש. |
| `commit_message` | לא | `docs: auto-translate README via Gemini` | הטקסט שישמש כהודעת ה-commit של git. |
| `model` | לא | `gemini-3.1-pro-preview` | מודל ה-Gemini לשימוש. |
| `source_file` | לא | `README.md` | קובץ הבסיס לתרגום. |

## 📤 פלטים (Outputs)

| פלט | תיאור |
| --- | --- |
| `total_tokens_used` | סך כל האסימונים (tokens) שעובדו. |
| `input_tokens_used` | מספר האסימונים בבקשות (prompts) של הקלט. |
| `output_tokens_used` | מספר האסימונים שנוצרו בתגובות. |
| `duration_seconds` | זמן העיבוד הכולל בשניות. |

## 🔑 כיצד להשיג מפתח API של Google Gemini

כדי להשתמש ב-action זה, דרוש לך מפתח API חינמי מ-Google AI Studio:

1. עבור אל [Google AI Studio](https://aistudio.google.com/).
2. התחבר עם חשבון ה-Google שלך.
3. בתפריט הניווט השמאלי, לחץ על **Get API key**.
4. לחץ על הלחצן **Create API key**.
5. העתק את המפתח שנוצר.
6. עבור אל מאגר ה-GitHub שלך -> **Settings** -> **Secrets and variables** -> **Actions**.
7. לחץ על **New repository secret**, קרא לו `GEMINI_API_KEY`, הדבק את המפתח לשדה ה-Secret ושמור.

## 🔑 כיצד להגדיר את אסימון ה-GitHub הסטנדרטי (GITHUB_TOKEN)

Action זה משתמש ב-`GITHUB_TOKEN` המובנה כדי לדחוף (push) קומיטים. **אין** צורך ליצור Personal Access Token (PAT) באופן ידני, אך עליך **לוודא** שלאסימון ברירת המחדל יש את ההרשאות המתאימות:

1. עבור אל **Settings** במאגר שלך -> **Actions** -> **General**.
2. גלול מטה אל אזור ה-**Workflow permissions**.
3. בחר באפשרות **Read and write permissions**.
4. לחץ על **Save**.
5. בקובץ ה-YAML של ה-workflow, פשוט העבר את `${{ secrets.GITHUB_TOKEN }}` לקלט `github_token` (כפי שמוצג בדוגמת השימוש).

## 📄 רישיון

פרויקט זה מורשה תחת רישיון MIT - ראו את קובץ ה-[LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) לפרטים נוספים.