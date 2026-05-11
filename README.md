# Automation Bot

Automation bot for:

- account registration
- profile filling
- captcha OCR solving
- excel-based bulk input

## Features

- Playwright automation
- OCR captcha solving
- Human-like typing
- Retry system
- Success/failed export
- Linux + macOS support

## Requirements

- Python 3.11+
- Tesseract OCR
- Chromium

## Install

```bash
pip install -r requirements.txt
playwright install chromium
```

## Run

```bash
python main.py
```

## Excel Format

| fullname | phone_number | id_number | password |
| -------- | ------------ | --------- | -------- |

## Notes

Use responsibly.
