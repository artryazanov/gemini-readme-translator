> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action ที่จะแปล `README.md` ของคุณเป็นหลายภาษาโดยอัตโนมัติด้วย Gemini API โดยระบบจะแทรกเมนูนำทางภาษาที่เชื่อมโยงถึงกันลงในทุกไฟล์อย่างชาญฉลาด และทำการ commit การเปลี่ยนแปลงโดยอัตโนมัติ

## 🚀 คุณสมบัติ
* **รองรับหลายภาษา:** สร้าง README สำหรับหลายภาษาได้ในการรันเพียงครั้งเดียว
* **การนำทางอัตโนมัติ:** แทรกและดูแลรักษาเมนูสลับภาษามาตรฐานที่ด้านบนสุดของไฟล์คุณโดยอัตโนมัติ (สามารถปิดใช้งานได้) AI จะจัดสไตล์ให้โดยอัตโนมัติ!
* **ปรับแต่งสไตล์ได้:** คุณสามารถระบุพารามิเตอร์สำหรับสไตล์เมนูแบบกำหนดเองเพื่อให้ AI จัดรูปแบบตัวสลับภาษาได้ตรงตามที่คุณต้องการ
* **การติดตาม Token:** แสดงสถิติการใช้งาน Token ของ Gemini

## 🛠 วิธีใช้งาน

สร้างไฟล์ workflow (เช่น `.github/workflows/translate.yml`):

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

## 📥 ข้อมูลนำเข้า (Inputs)

| ข้อมูลนำเข้า | บังคับ | ค่าเริ่มต้น | คำอธิบาย |
| --- | --- | --- | --- |
| `api_key` | ใช่ |  | คีย์ Google Gemini API ของคุณ |
| `github_token` | ใช่ |  | โทเค็น GitHub มาตรฐาน (`${{ secrets.GITHUB_TOKEN }}`) |
| `languages` | ใช่ |  | ภาษาเป้าหมายที่คั่นด้วยเครื่องหมายจุลภาค (เช่น `ru, es`) |
| `output_dir` | ไม่ | | ไดเรกทอรีสำหรับบันทึกไฟล์ที่แปลแล้ว ค่าเริ่มต้นคือไดเรกทอรีของไฟล์ต้นฉบับ |
| `add_language_menu` | ไม่ | `true` | ตั้งค่าเป็น `false` เพื่อปิดใช้งานการสร้างเมนูภาษาโดยอัตโนมัติ |
| `menu_style` | ไม่ | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | สไตล์อ้างอิงที่ AI ใช้เมื่อสร้างเมนูภาษาใหม่ |
| `commit_message` | ไม่ | `docs: auto-translate README via Gemini` | ข้อความที่ใช้สำหรับ git commit message |
| `model` | ไม่ | `gemini-3.1-pro-preview` | โมเดล Gemini ที่จะใช้ |
| `source_file` | ไม่ | `README.md` | ไฟล์หลักที่จะนำมาแปล |

## 📤 ข้อมูลส่งออก (Outputs)

| ข้อมูลส่งออก | คำอธิบาย |
| --- | --- |
| `total_tokens_used` | จำนวน Token ทั้งหมดที่ประมวลผล |
| `input_tokens_used` | จำนวน Token ใน input prompts |
| `output_tokens_used` | จำนวน Token ที่สร้างขึ้นใน response |
| `duration_seconds` | เวลาประมวลผลรวมเป็นวินาที |

## 🔑 วิธีรับคีย์ Google Gemini API

หากต้องการใช้งาน action นี้ คุณต้องมี API key ฟรีจาก Google AI Studio:

1. ไปที่ [Google AI Studio](https://aistudio.google.com/)
2. ลงชื่อเข้าใช้ด้วยบัญชี Google ของคุณ
3. ในเมนูการนำทางด้านซ้าย ให้คลิกที่ **Get API key**
4. คลิกปุ่ม **Create API key**
5. คัดลอกคีย์ที่สร้างขึ้นมา
6. ไปที่ GitHub repository ของคุณ -> **Settings** -> **Secrets and variables** -> **Actions**
7. คลิก **New repository secret** ตั้งชื่อว่า `GEMINI_API_KEY` วางคีย์ของคุณลงในช่อง Secret แล้วกดยืนยันบันทึก

## 🔑 วิธีการตั้งค่าโทเค็น GitHub มาตรฐาน (Standard GitHub Token)

Action นี้ใช้ `GITHUB_TOKEN` ที่มีมาให้อยู่แล้วเพื่อ push commits คุณ **ไม่จำเป็น** ต้องสร้าง Personal Access Token (PAT) เอง แต่คุณ **ต้อง** ตรวจสอบให้แน่ใจว่าโทเค็นเริ่มต้นมีสิทธิ์การเข้าถึงที่ถูกต้อง:

1. ไปที่ **Settings** ของ repository คุณ -> **Actions** -> **General**
2. เลื่อนลงไปที่ส่วน **Workflow permissions**
3. เลือก **Read and write permissions**
4. คลิก **Save**
5. ในไฟล์ YAML ของ workflow คุณ เพียงแค่ส่ง `${{ secrets.GITHUB_TOKEN }}` ไปที่ข้อมูลนำเข้า `github_token` (ตามที่แสดงในตัวอย่างการใช้งาน)

## 📄 สัญญาอนุญาต (License)

โปรเจกต์นี้อยู่ภายใต้สัญญาอนุญาต MIT - ดูรายละเอียดเพิ่มเติมได้ในไฟล์ [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE)