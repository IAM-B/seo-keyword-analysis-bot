# SEO Keyword Analysis Bot

This repository contains a bot designed to automate the analysis of keywords for SEO, particularly to build a list of high-potential keywords for niche blog title creation. By leveraging Google’s `allintitle` search feature, the bot identifies keywords with strong SEO potential, helping content creators target phrases that are more likely to rank well in search engines.

## Objective

The bot aims to create a list of keywords with high SEO value, ideal for crafting titles in niche blogs. By filtering keywords based on search volume, competition level, and relevance, this tool provides valuable insights to optimize content strategy and improve search visibility.

## Features

- **Keyword Collection**: Fetches keywords from a `keywords.csv` file, expected to be exported from **Google Ads Keyword Planner**.
- **Search Volume and Competition Analysis**: Uses Google search to check the `allintitle` count for each keyword, identifying phrases with less competition.
- **Filtering and Sorting**: Filters keywords based on predefined monthly average thresholds and quality indices, saving sorted results to `final_sorted.csv` for easy reference.

## Prerequisites

- **Python 3.7+**
- **Selenium** (for automated browsing)
- **Google Chrome** and **ChromeDriver** (for Selenium)
- **Pytest** (for running tests)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IAM-B/seo-keyword-analysis-bot.git
   cd seo-keyword-analysis-bot
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**:
   - Ensure your ChromeDriver version matches your Chrome browser version.
   - Download from [ChromeDriver](https://sites.google.com/chromium.org/driver/).

4. **Prepare the `keywords.csv` file**:
   - Export a CSV file from **Google Ads Keyword Planner**.
   - **Required Columns**: Ensure your file includes `Keyword`, `Monthly Average`, and other relevant columns.

## File Descriptions

- **`keywords.csv`**: Source file with keywords exported from Google Ads. This file should be placed in the project directory.
- **`final.csv`**: Results file containing keywords that meet the quality criteria for SEO potential.
- **`final_sorted.csv`**: Sorted results based on quality index, showing keywords with the highest potential for ranking well in search engines.

## Usage

### Makefile Commands

This project includes a `Makefile` for streamlined execution.

1. **Run Tests and Sort Keywords**:
   ```bash
   make run
   ```

   This command:
   - Runs tests using `pytest`.
   - Sorts keywords based on quality index and saves the results in `final_sorted.csv`.

2. **Individual Commands**:
   - **Run Tests Only**:
     ```bash
     make collect
     ```
   - **Sort Keywords Only**:
     ```bash
     make sort
     ```

### Running Individual Scripts

If preferred, you can also run each script individually:

1. **Collect SEO Data**:
   ```bash
   python -m pytest -s
   ```

2. **Sort Results**:
   ```bash
   python sort_best_keywords.py
   ```

## Configuration

Edit `sort_best_keywords.py` or other scripts as necessary to adjust thresholds, update file paths, or configure other parameters based on your SEO strategy.

## License

This project is licensed under the MIT License.
