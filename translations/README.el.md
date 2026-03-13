> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Ένα GitHub Action που μεταφράζει αυτόματα το `README.md` σας σε πολλαπλές γλώσσες χρησιμοποιώντας το Gemini API. Εισάγει έξυπνα ένα μενού πλοήγησης γλωσσών με διασυνδέσεις (cross-links) σε όλα τα αρχεία και κάνει commit τις αλλαγές αυτόματα.

## 🚀 Χαρακτηριστικά
* **Υποστήριξη Πολλαπλών Γλωσσών:** Δημιουργία αρχείων README για πολλές γλώσσες σε μία μόνο εκτέλεση.
* **Αυτόματη Πλοήγηση:** Εισάγει και διατηρεί αυτόματα ένα τυπικό μενού εναλλαγής γλωσσών στην κορυφή των αρχείων σας (μπορεί να απενεργοποιηθεί). Το AI το μορφοποιεί αυτόματα!
* **Προσαρμοσμένη Μορφοποίηση:** Μπορείτε να παρέχετε μια παράμετρο προσαρμοσμένου στιλ μενού, ώστε το AI να μορφοποιεί την εναλλαγή γλωσσών ακριβώς όπως θέλετε.
* **Παρακολούθηση Token:** Εξάγει στατιστικά στοιχεία χρήσης token του Gemini.

## 🛠 Χρήση

Δημιουργήστε ένα αρχείο workflow (π.χ. `.github/workflows/translate.yml`):

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

## 📥 Παράμετροι Εισόδου (Inputs)

| Παράμετρος | Απαιτείται | Προεπιλογή | Περιγραφή |
| --- | --- | --- | --- |
| `api_key` | Ναι |  | Το Google Gemini API Key σας. |
| `github_token` | Ναι |  | Το τυπικό GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ναι |  | Γλώσσες-στόχοι διαχωρισμένες με κόμμα (π.χ. `ru, es`). |
| `output_dir` | Όχι | | Κατάλογος για την αποθήκευση των μεταφρασμένων αρχείων. Προεπιλογή είναι ο κατάλογος του αρχείου προέλευσης. |
| `add_language_menu` | Όχι | `true` | Ορίστε το σε `false` για να απενεργοποιήσετε την αυτόματη δημιουργία του μενού γλωσσών. |
| `menu_style` | Όχι | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Το στιλ αναφοράς που χρησιμοποιεί το AI κατά τη δημιουργία ενός νέου μενού γλωσσών. |
| `commit_message` | Όχι | `docs: auto-translate README via Gemini` | Κείμενο που χρησιμοποιείται για το μήνυμα του git commit. |
| `model` | Όχι | `gemini-3.1-pro-preview` | Το μοντέλο Gemini που θα χρησιμοποιηθεί. |
| `source_file` | Όχι | `README.md` | Το βασικό αρχείο προς μετάφραση. |

## 📤 Παράμετροι Εξόδου (Outputs)

| Έξοδος | Περιγραφή |
| --- | --- |
| `total_tokens_used` | Συνολικός αριθμός token που επεξεργάστηκαν. |
| `input_tokens_used` | Αριθμός token στα μηνύματα προτροπής (input prompts). |
| `output_tokens_used` | Αριθμός token που δημιουργήθηκαν στις απαντήσεις. |
| `duration_seconds` | Συνολικός χρόνος επεξεργασίας σε δευτερόλεπτα. |

## 🔑 Πώς να αποκτήσετε ένα Google Gemini API Key

Για να χρησιμοποιήσετε αυτό το action, χρειάζεστε ένα δωρεάν API key από το Google AI Studio:

1. Μεταβείτε στο [Google AI Studio](https://aistudio.google.com/).
2. Συνδεθείτε με τον λογαριασμό σας Google.
3. Στο αριστερό μενού πλοήγησης, κάντε κλικ στο **Get API key**.
4. Κάντε κλικ στο κουμπί **Create API key**.
5. Αντιγράψτε το παραγόμενο κλειδί.
6. Μεταβείτε στο αποθετήριο GitHub σας -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Κάντε κλικ στο **New repository secret**, ονομάστε το `GEMINI_API_KEY`, επικολλήστε το κλειδί σας στο πεδίο Secret, και αποθηκεύστε.

## 🔑 Πώς να ρυθμίσετε το Τυπικό GitHub Token

Αυτό το action χρησιμοποιεί το ενσωματωμένο `GITHUB_TOKEN` για να κάνει push τα commits. **Δεν** χρειάζεται να δημιουργήσετε ένα Personal Access Token (PAT) χειροκίνητα, αλλά **πρέπει** να βεβαιωθείτε ότι το προεπιλεγμένο token έχει τα σωστά δικαιώματα:

1. Μεταβείτε στο αποθετήριό σας **Settings** -> **Actions** -> **General**.
2. Κάντε κύλιση προς τα κάτω στην ενότητα **Workflow permissions**.
3. Επιλέξτε **Read and write permissions**.
4. Κάντε κλικ στο **Save**.
5. Στο workflow YAML σας, απλώς περάστε το `${{ secrets.GITHUB_TOKEN }}` στην παράμετρο `github_token` (όπως φαίνεται στο παράδειγμα χρήσης).

## 📄 Άδεια χρήσης

Αυτό το έργο αδειοδοτείται υπό την MIT License - δείτε το αρχείο [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) για λεπτομέρειες.