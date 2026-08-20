# 🌍 Country Web Scraper

A simple Python web scraping project that collects country names and population data from [Scrape This Site](https://www.scrapethissite.com/pages/simple) and saves the results to a CSV file.

## ✨ Features

* Scrapes country names and population data
* Uses Requests to fetch web pages
* Uses BeautifulSoup to parse HTML
* Exports data to CSV
* Automatically creates the output directory

## 🛠️ Built With

* Python 3
* Requests
* BeautifulSoup4
* CSV

## 📂 Project Structure

```text
country-web-scraper/
├── scraper.py
├── output/
│   └── countries.csv
├── requirements.txt
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd country-web-scraper
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the scraper:

```bash
python scraper.py
```

The scraped data will be saved to:

```text
output/countries.csv
```

## 📊 Example Output

```text
country,population
Afghanistan,37172386
Albania,2866376
Algeria,42228429
...
```

## 📚 What I Learned

This project helped me practice:

* Python web scraping
* HTTP requests
* HTML parsing with BeautifulSoup
* Working with CSV files
* File and directory handling
* Basic Python project structure

## 🎯 Purpose

This project was created as a practical exercise to learn the fundamentals of web scraping with Python and working with extracted data.

## ⚠️ Disclaimer

This project is for educational purposes and uses publicly available data from Scrape This Site.
