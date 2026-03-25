> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Çevirmeni


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini API'sini kullanarak `README.md` dosyanızı otomatik olarak birden fazla dile çeviren bir GitHub Action (Eylemi). Tüm dosyalara akıllı bir şekilde çapraz bağlantılı bir dil gezinme menüsü ekler ve değişiklikleri otomatik olarak commit eder (işler).

## 🚀 Özellikler
* **Çoklu Dil Desteği:** Tek bir çalıştırmada birden fazla dil için README dosyaları oluşturun.
* **Otomatik Gezinme:** Dosyalarınızın en üstüne standart bir dil değiştirici menüyü otomatik olarak ekler ve günceller (devre dışı bırakılabilir). Yapay Zeka bunu otomatik olarak şekillendirir!
* **Özel Şekillendirme:** Özel bir menü stili parametresi sağlayabilirsiniz, böylece Yapay Zeka dil değiştiriciyi tam olarak istediğiniz gibi biçimlendirir.
* **Token Takibi:** Gemini token kullanım istatistiklerinin çıktısını verir.

## 🛠 Kullanım

Bir iş akışı (workflow) dosyası oluşturun (örneğin, `.github/workflows/translate.yml`):

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

## 📥 Girdiler

| Girdi | Gerekli | Varsayılan | Açıklama |
| --- | --- | --- | --- |
| `api_key` | Evet |  | Google Gemini API Anahtarınız. |
| `github_token` | Evet |  | Standart GitHub token'ı (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Evet |  | Virgülle ayrılmış hedef diller (ör. `ru, es`). |
| `output_dir` | Hayır | | Çevrilen dosyaların kaydedileceği dizin. Varsayılan olarak kaynak dosyanın dizinidir. |
| `add_language_menu` | Hayır | `true` | Dil menüsünün otomatik olarak oluşturulmasını devre dışı bırakmak için `false` olarak ayarlayın. |
| `use_absolute_links`| Hayır | `true` | Oluşturulan dil menülerinde mutlak GitHub URL'leri yerine göreli bağlantılar kullanmak için `false` olarak ayarlayın. |
| `menu_style` | Hayır | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Yeni bir dil menüsü oluştururken yapay zekanın kullanacağı referans stili. |
| `commit_message` | Hayır | `docs: auto-translate README via Gemini` | Git commit mesajı için kullanılan metin. |
| `model` | Hayır | `gemini-3.1-pro-preview` | Kullanılacak Gemini modeli. |
| `source_file` | Hayır | `README.md` | Çevrilecek temel dosya. |

## 📤 Çıktılar

| Çıktı | Açıklama |
| --- | --- |
| `total_tokens_used` | İşlenen toplam token sayısı. |
| `input_tokens_used` | Girdi istemlerindeki (prompts) token sayısı. |
| `output_tokens_used` | Yanıtlarda oluşturulan token sayısı. |
| `duration_seconds` | Saniye cinsinden toplam işlem süresi. |

## 🔑 Google Gemini API Anahtarı Nasıl Alınır?

Bu eylemi kullanmak için Google AI Studio'dan ücretsiz bir API anahtarına ihtiyacınız var:

1. [Google AI Studio](https://aistudio.google.com/) adresine gidin.
2. Google hesabınızla giriş yapın.
3. Sol gezinme menüsünde **Get API key** (API anahtarı al) seçeneğine tıklayın.
4. **Create API key** (API anahtarı oluştur) düğmesine tıklayın.
5. Oluşturulan anahtarı kopyalayın.
6. GitHub deponuza gidin -> **Settings** (Ayarlar) -> **Secrets and variables** (Gizli diziler ve değişkenler) -> **Actions** (Eylemler).
7. **New repository secret** (Yeni depo gizli dizisi) seçeneğine tıklayın, adını `GEMINI_API_KEY` yapın, anahtarınızı Secret alanına yapıştırın ve kaydedin.

## 🔑 Standart GitHub Token'ı Nasıl Yapılandırılır?

Bu eylem, commit'leri göndermek için yerleşik `GITHUB_TOKEN`'ı kullanır. Manuel olarak bir Kişisel Erişim Belirteci (PAT) oluşturmanıza **gerek yoktur**, ancak varsayılan token'ın doğru izinlere sahip olduğundan emin **olmalısınız**:

1. Deponuzun **Settings** (Ayarlar) -> **Actions** (Eylemler) -> **General** (Genel) bölümüne gidin.
2. **Workflow permissions** (İş akışı izinleri) bölümüne doğru aşağı kaydırın.
3. **Read and write permissions** (Okuma ve yazma izinleri) seçeneğini belirleyin.
4. **Save** (Kaydet) düğmesine tıklayın.
5. İş akışı YAML dosyanızda, `${{ secrets.GITHUB_TOKEN }}` değerini `github_token` girdisine iletmeniz yeterlidir (kullanım örneğinde gösterildiği gibi).

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) dosyasına bakın.