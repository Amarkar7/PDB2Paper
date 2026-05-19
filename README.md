# PDB Paper Downloader

Automatically download research papers associated with Protein Data Bank (PDB) structures using DOI metadata from RCSB.

The script queries the RCSB API, extracts DOI information, searches publisher pages for PDF links, and downloads accessible papers automatically.

---

## Features

- DOI retrieval from RCSB
- Automatic PDF discovery
- Handles redirects
- Multiple publisher support
- Randomized browser headers
- PDF validation
- Failed download logging
- Resume-safe execution

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Amarkar7/PDB2Paper.git
cd PDB2Paper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Add PDB IDs to:

```text
pdb_ids.txt
```

Example:

```text
1A4T
1ETF
3ICE
```

Run:

```bash
python3 download_papers.py
```

Downloaded papers will be stored in:

```text
PDB_Papers/
```

Failed entries will be stored in:

```text
failed_downloads.txt
```

---

## Repository Structure

```text
PDB2Paper/
├── download_papers.py
├── requirements.txt
├── pdb_ids.txt
├── README.md
├── .gitignore
└── PDB_Papers/
```

---

## Notes

Some publishers may block automated downloads.

Possible reasons for failed downloads:

- CAPTCHA or anti-bot protection
- Institutional access restrictions
- JavaScript-rendered PDF buttons
- Invalid or outdated DOI
- Temporary rate limiting

---

## Disclaimer

This project is intended for academic and research purposes only.

Please respect publisher copyright policies and institutional access rules.
