# Walmart Scraper

This module extracts product and review data from Walmart's website. It uses ZenRows to bypass CAPTCHA protection, but we could use other CAPTCHA and proxy services to handle bot protection.


## Features

- Fetches product data from a specified URL.
- Fetches customer reviews data from a specified URL.
- Filters the reviews based on a given date.
- Creates a Product object with the fetched and filtered data.
- Saves the processed data to a JSON file.

## Requirements

- Python 3.x
- `requests`
- `pydantic`
- `python-decouple`

## Setup
Clone the repository:

```bash
git clone git@github.com:alexanderfebres/walmart-scraper.git
cd walmart-scraper
