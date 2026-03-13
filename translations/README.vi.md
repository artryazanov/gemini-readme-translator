> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Một GitHub Action tự động dịch tệp `README.md` của bạn sang nhiều ngôn ngữ khác nhau bằng cách sử dụng Gemini API. Nó tự động chèn một menu điều hướng ngôn ngữ có liên kết chéo vào tất cả các tệp và tự động commit các thay đổi một cách thông minh.

## 🚀 Tính năng
* **Hỗ trợ Đa Ngôn ngữ:** Tạo tệp README cho nhiều ngôn ngữ chỉ trong một lần chạy.
* **Tự động Điều hướng:** Tự động chèn và duy trì một menu chuyển đổi ngôn ngữ tiêu chuẩn ở đầu các tệp của bạn (có thể tắt). AI sẽ tự động định dạng cho nó!
* **Tùy chỉnh Giao diện:** Bạn có thể cung cấp tham số định dạng menu tùy chỉnh để AI định dạng trình chuyển đổi ngôn ngữ theo đúng ý bạn.
* **Theo dõi Token:** Xuất ra số liệu thống kê việc sử dụng token của Gemini.

## 🛠 Cách sử dụng

Tạo một tệp workflow (ví dụ: `.github/workflows/translate.yml`):

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

## 📥 Tham số Đầu vào (Inputs)

| Đầu vào | Bắt buộc | Mặc định | Mô tả |
| --- | --- | --- | --- |
| `api_key` | Có |  | Khóa API Google Gemini của bạn. |
| `github_token` | Có |  | GitHub token tiêu chuẩn (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Có |  | Các ngôn ngữ mục tiêu được phân tách bằng dấu phẩy (ví dụ: `ru, es`). |
| `output_dir` | Không | | Thư mục lưu các tệp đã dịch. Mặc định là thư mục của tệp nguồn. |
| `add_language_menu` | Không | `true` | Đặt thành `false` để tắt tính năng tự động tạo menu ngôn ngữ. |
| `menu_style` | Không | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Định dạng tham chiếu mà AI sử dụng khi tạo menu ngôn ngữ mới. |
| `commit_message` | Không | `docs: auto-translate README via Gemini` | Văn bản được sử dụng cho tin nhắn git commit. |
| `model` | Không | `gemini-3.1-pro-preview` | Mô hình Gemini cần sử dụng. |
| `source_file` | Không | `README.md` | Tệp cơ sở cần dịch. |

## 📤 Đầu ra (Outputs)

| Đầu ra | Mô tả |
| --- | --- |
| `total_tokens_used` | Tổng số token đã được xử lý. |
| `input_tokens_used` | Số lượng token trong các prompt đầu vào. |
| `output_tokens_used` | Số lượng token được tạo trong các phản hồi. |
| `duration_seconds` | Tổng thời gian xử lý tính bằng giây. |

## 🔑 Cách lấy Khóa API Google Gemini

Để sử dụng action này, bạn cần có một khóa API miễn phí từ Google AI Studio:

1. Truy cập [Google AI Studio](https://aistudio.google.com/).
2. Đăng nhập bằng tài khoản Google của bạn.
3. Trong menu điều hướng bên trái, nhấp vào **Get API key**.
4. Nhấp vào nút **Create API key**.
5. Sao chép khóa đã được tạo.
6. Truy cập kho lưu trữ GitHub của bạn -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Nhấp vào **New repository secret**, đặt tên là `GEMINI_API_KEY`, dán khóa của bạn vào trường Secret và lưu lại.

## 🔑 Cách cấu hình Standard GitHub Token

Action này sử dụng `GITHUB_TOKEN` tích hợp để đẩy (push) các commit. Bạn **không** cần phải tạo thủ công Personal Access Token (PAT), nhưng bạn **phải** đảm bảo token mặc định có các quyền chính xác:

1. Đi tới **Settings** -> **Actions** -> **General** của kho lưu trữ.
2. Cuộn xuống phần **Workflow permissions**.
3. Chọn **Read and write permissions**.
4. Nhấp vào **Save**.
5. Trong file YAML workflow của bạn, chỉ cần truyền `${{ secrets.GITHUB_TOKEN }}` vào đầu vào `github_token` (như được hiển thị trong ví dụ sử dụng).

## 📄 Giấy phép

Dự án này được cấp phép theo Giấy phép MIT - xem tệp [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) để biết thêm chi tiết.