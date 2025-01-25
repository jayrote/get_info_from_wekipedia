# Wikipedia Search and Content Extractor

## Project Description
A Python-based web scraping tool that uses Selenium to:
- Perform Google searches
- Navigate to Wikipedia pages
- Extract text content
- Collect image URLs
- Save information to a text file

## Features
- Automated Google search
- Wikipedia page navigation
- Smooth page scrolling
- Content extraction
- Text and image URL saving

## Prerequisites
- Python 3.8+
- Selenium WebDriver
- Chrome Browser
- ChromeDriver

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/wikipedia-scraper.git
cd wikipedia-scraper
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install selenium webdriver-manager
```

## Usage
```bash
python scraper.py
```
- Enter your search query when prompted
- Script will generate a text file with content and image URLs

## Dependencies
- selenium
- webdriver-manager
- time
- random

## Project Structure
```
wikipedia-scraper/
├── scraper.py          # Main scraping script
└── README.md           # Project documentation
```

## How It Works
1. Performs Google search for Wikipedia page
2. Navigates to first Wikipedia result
3. Scrolls through page to load content
4. Extracts paragraphs and image URLs
5. Saves information to text file

## Limitations
- Requires Chrome browser
- Depends on webpage structure
- No image downloading (only URLs)

## Future Improvements
- Add image download functionality
- Support multiple search engines
- Enhance error handling
