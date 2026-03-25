> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Eine GitHub Action, die Ihre `README.md` mithilfe der Gemini-API automatisch in mehrere Sprachen übersetzt. Sie fügt intelligent ein verlinktes Sprachnavigationsmenü in alle Dateien ein und committet die Änderungen automatisch.

## 🚀 Funktionen
* **Mehrsprachigkeits-Unterstützung:** Generieren Sie READMEs für mehrere Sprachen in einem Durchlauf.
* **Auto-Navigation:** Fügt automatisch ein Standard-Menü zum Sprachwechsel am Anfang Ihrer Dateien ein und verwaltet dieses (kann deaktiviert werden). Die KI formatiert es automatisch!
* **Benutzerdefiniertes Styling:** Sie können einen Parameter für den Menüstil angeben, damit die KI den Sprachwechsler genau so formatiert, wie Sie es möchten.
* **Token-Tracking:** Gibt Statistiken zur Nutzung der Gemini-Token aus.

## 🛠 Verwendung

Erstellen Sie eine Workflow-Datei (z. B. `.github/workflows/translate.yml`):

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

## 📥 Eingaben

| Eingabe | Erforderlich | Standard | Beschreibung |
| --- | --- | --- | --- |
| `api_key` | Ja |  | Ihr Google Gemini API-Schlüssel. |
| `github_token` | Ja |  | Standard-GitHub-Token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ja |  | Kommagetrennte Zielsprachen (z. B. `ru, es`). |
| `output_dir` | Nein | | Verzeichnis zum Speichern der übersetzten Dateien. Standardmäßig das Verzeichnis der Quelldatei. |
| `add_language_menu` | Nein | `true` | Auf `false` setzen, um die automatische Generierung des Sprachmenüs zu deaktivieren. |
| `use_absolute_links`| Nein | `true` | Setzen Sie dies auf `false`, um in den generierten Sprachmenüs relative Links anstelle von absoluten GitHub-URLs zu verwenden. |
| `menu_style` | Nein | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Der Referenzstil, den die KI beim Generieren eines neuen Sprachmenüs verwendet. |
| `commit_message` | Nein | `docs: auto-translate README via Gemini` | Text, der für die Git-Commit-Nachricht verwendet wird. |
| `model` | Nein | `gemini-3.1-pro-preview` | Das zu verwendende Gemini-Modell. |
| `source_file` | Nein | `README.md` | Die zu übersetzende Basisdatei. |

## 📤 Ausgaben

| Ausgabe | Beschreibung |
| --- | --- |
| `total_tokens_used` | Gesamtzahl der verarbeiteten Token. |
| `input_tokens_used` | Anzahl der Token in den Eingabe-Prompts. |
| `output_tokens_used` | Anzahl der in den Antworten generierten Token. |
| `duration_seconds` | Gesamte Verarbeitungszeit in Sekunden. |

## 🔑 So erhalten Sie einen Google Gemini API-Schlüssel

Um diese Action zu verwenden, benötigen Sie einen kostenlosen API-Schlüssel von Google AI Studio:

1. Gehen Sie zu [Google AI Studio](https://aistudio.google.com/).
2. Melden Sie sich mit Ihrem Google-Konto an.
3. Klicken Sie im linken Navigationsmenü auf **Get API key**.
4. Klicken Sie auf die Schaltfläche **Create API key**.
5. Kopieren Sie den generierten Schlüssel.
6. Gehen Sie in Ihrem GitHub-Repository auf **Settings** -> **Secrets and variables** -> **Actions**.
7. Klicken Sie auf **New repository secret**, benennen Sie es `GEMINI_API_KEY`, fügen Sie Ihren Schlüssel in das Feld "Secret" ein und speichern Sie.

## 🔑 So konfigurieren Sie das Standard-GitHub-Token

Diese Action verwendet das integrierte `GITHUB_TOKEN`, um Commits zu pushen. Sie **müssen kein** Personal Access Token (PAT) manuell erstellen, aber Sie **müssen** sicherstellen, dass das Standard-Token über die richtigen Berechtigungen verfügt:

1. Gehen Sie in den **Settings** Ihres Repositorys auf **Actions** -> **General**.
2. Scrollen Sie nach unten zum Abschnitt **Workflow permissions**.
3. Wählen Sie **Read and write permissions**.
4. Klicken Sie auf **Save**.
5. Übergeben Sie in Ihrem YAML-Workflow einfach `${{ secrets.GITHUB_TOKEN }}` an die Eingabe `github_token` (wie im Verwendungsbeispiel gezeigt).

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – weitere Details finden Sie in der Datei [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).