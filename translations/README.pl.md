> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Akcja GitHub, która automatycznie tłumaczy Twój plik `README.md` na wiele języków za pomocą API Gemini. Inteligentnie wstrzykuje menu nawigacyjne języków z linkami krzyżowymi do wszystkich plików i automatycznie zatwierdza (commituje) zmiany.

## 🚀 Funkcje
* **Obsługa wielu języków:** Generuj pliki README dla wielu języków podczas jednego uruchomienia.
* **Automatyczna nawigacja:** Automatycznie wstawia i utrzymuje standardowe menu przełączania języków na górze plików (można to wyłączyć). AI automatycznie je formatuje!
* **Niestandardowe formatowanie:** Możesz podać własny parametr stylu menu, dzięki czemu AI sformatuje przełącznik języków dokładnie tak, jak chcesz.
* **Śledzenie tokenów:** Zwraca statystyki zużycia tokenów Gemini.

## 🛠 Użytkowanie

Utwórz plik przepływu pracy (np. `.github/workflows/translate.yml`):

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

## 📥 Dane wejściowe

| Dane wejściowe | Wymagane | Domyślnie | Opis |
| --- | --- | --- | --- |
| `api_key` | Tak |  | Twój klucz API Google Gemini. |
| `github_token` | Tak |  | Standardowy token GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Tak |  | Języki docelowe oddzielone przecinkami (np. `ru, es`). |
| `output_dir` | Nie | | Katalog zapisu przetłumaczonych plików. Domyślnie jest to katalog pliku źródłowego. |
| `add_language_menu` | Nie | `true` | Ustaw na `false`, aby wyłączyć automatyczne generowanie menu językowego. |
| `menu_style` | Nie | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Styl referencyjny, którego AI używa podczas generowania nowego menu językowego. |
| `commit_message` | Nie | `docs: auto-translate README via Gemini` | Tekst używany do komunikatu commita git. |
| `model` | Nie | `gemini-3.1-pro-preview` | Model Gemini do użycia. |
| `source_file` | Nie | `README.md` | Plik bazowy do przetłumaczenia. |

## 📤 Dane wyjściowe

| Dane wyjściowe | Opis |
| --- | --- |
| `total_tokens_used` | Całkowita liczba przetworzonych tokenów. |
| `input_tokens_used` | Liczba tokenów w promptach wejściowych. |
| `output_tokens_used` | Liczba tokenów wygenerowanych w odpowiedziach. |
| `duration_seconds` | Całkowity czas przetwarzania w sekundach. |

## 🔑 Jak zdobyć klucz API Google Gemini

Aby korzystać z tej akcji, potrzebujesz darmowego klucza API od Google AI Studio:

1. Przejdź do [Google AI Studio](https://aistudio.google.com/).
2. Zaloguj się za pomocą swojego konta Google.
3. W lewym menu nawigacyjnym kliknij **Get API key** (Pobierz klucz API).
4. Kliknij przycisk **Create API key** (Utwórz klucz API).
5. Skopiuj wygenerowany klucz.
6. Przejdź do swojego repozytorium GitHub -> **Settings** (Ustawienia) -> **Secrets and variables** (Sekrety i zmienne) -> **Actions** (Akcje).
7. Kliknij **New repository secret** (Nowy sekret repozytorium), nazwij go `GEMINI_API_KEY`, wklej swój klucz w pole Secret i zapisz.

## 🔑 Jak skonfigurować standardowy token GitHub

Ta akcja wykorzystuje wbudowany `GITHUB_TOKEN` do wypychania (push) commitów. **Nie musisz** ręcznie tworzyć Personal Access Token (PAT), ale **musisz** upewnić się, że domyślny token ma odpowiednie uprawnienia:

1. Przejdź do **Settings** (Ustawienia) repozytorium -> **Actions** (Akcje) -> **General** (Ogólne).
2. Przewiń w dół do sekcji **Workflow permissions** (Uprawnienia przepływu pracy).
3. Wybierz **Read and write permissions** (Uprawnienia do odczytu i zapisu).
4. Kliknij **Save** (Zapisz).
5. W pliku YAML przepływu pracy po prostu przekaż `${{ secrets.GITHUB_TOKEN }}` do danych wejściowych `github_token` (jak pokazano w przykładzie użytkowania).

## 📄 Licencja

Ten projekt jest licencjonowany na warunkach licencji MIT - zobacz plik [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) po więcej szczegółów.