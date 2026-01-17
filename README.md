# Ekantipur Entertainment Scraper

A collection of web scrapers built with Playwright to extract content from ekantipur.com, a popular Nepali news website.

## 📁 Project Structure

```
ekantipur-entertainment-scraper/
├── cartoon-scraper/          # Task 2: Cartoon scraper
│   ├── scraper.py
│   ├── prompt.txt
│   ├── pyproject.toml
│   └── output.json
├── entertainment-scrape/      # Task 1: Entertainment news scraper
│   ├── scraper.py
│   ├── prompt.txt
│   ├── pyproject.toml
│   └── output.json
├── .gitignore
└── README.md
```

## 🚀 Features

### Task 1: Entertainment News Scraper
- Scrapes top 5 entertainment news articles from ekantipur.com
- Extracts: title, image URL, category, and author
- Navigates through the मनोरञ्जन (Entertainment) section
- Automatic navigation and interaction with the website
- Waits for dynamic content to load (network idle)
- Handles missing elements gracefully (sets to null)
- UTF-8 encoding for proper Nepali character support

### Task 2: Cartoon Scraper
- Scrapes all available cartoons from ekantipur.com/cartoon
- Extracts: title, image URL, and author
- Robust error handling with fallback selectors
- Handles timeout scenarios gracefully
- Extracts title and author from combined text (splits on " - ")
- Supports both `src` and `srcset` image attributes
- Only saves cartoons with at least title OR image_url

## 🛠️ Tech Stack

- **Python 3.12+**
- **Playwright** - Browser automation
- **uv** - Modern Python package manager

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- uv package manager ([Install uv](https://github.com/astral-sh/uv))

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ekantipur-entertainment-scraper
```

2. Navigate to the scraper directory:
```bash
# For entertainment scraper
cd entertainment-scrape

# OR for cartoon scraper
cd cartoon-scraper
```

3. Install dependencies:
```bash
uv sync
```

4. Install Playwright browsers:
```bash
uv run playwright install chromium
```

## 🎯 Usage

### Entertainment News Scraper
```bash
cd entertainment-scrape
uv run python scraper.py
```

Output will be saved to `output.json`.

### Cartoon Scraper
```bash
cd cartoon-scraper
uv run python scraper.py
```

Output will be saved to `output.json`.

## 📄 Output Format

### Entertainment News
```json
{
  "entertainment_news": [
    {
      "title": "Article Title",
      "image_url": "https://...",
      "category": "मनोरञ्जन",
      "author": "Author Name"
    }
  ]
}
```

### Cartoon
```json
{
  "cartoons": [
    {
      "title": "Cartoon Title",
      "image_url": "https://...",
      "author": "Author Name"
    }
  ]
}
```

## 📝 Notes

- Both scrapers run in non-headless mode (browser window visible)
- Output files are saved in UTF-8 encoding to support Nepali characters
- The scrapers include robust error handling for missing elements
- Each scraper has a `prompt.txt` file containing the instructions used to generate the code
- Output JSON files are generated when scrapers run (ignored by git)

## 📚 License

This project is for educational purposes.
