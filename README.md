# PDB Paper Downloader

Automatically download research papers associated with Protein Data Bank (PDB) structures using DOI metadata from RCSB.

The script queries the RCSB API, extracts DOI information, searches publisher pages for PDF links, and downloads accessible papers automatically.

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
git clone https://github.com/yourusername/PDB-Paper-Downloader.git
cd PDB-Paper-Downloader
