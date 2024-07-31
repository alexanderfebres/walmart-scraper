"""
This module fetches product and review data from Walmart's website and processes it.

The module performs the following tasks:
1. Fetches product data from a specified URL.
2. Fetches customer reviews data from a specified URL.
3. Filters the reviews based on a given date.
4. Creates a Product object with the fetched and filtered data.
5. Saves the processed data to a JSON file.
"""

import requests
import logging
import urllib3

from typing import List, Dict, Any
from models import Product, Review
from decorators import error_handler
from utils import filter_reviews_by_date, save_to_json
from decouple import config
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress only the single InsecureRequestWarning from urllib3 needed
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

PRODUCT_URL = (
    "https://www.walmart.com/ip/Beats-Solo3-Wireless-Headphones-Black/604599575"
)
REVIEWS_URL = "https://www.walmart.com/reviews/product/604599575"

PROXY = config("PROXY")
PROXIES = {"http": PROXY, "https": PROXY}


@error_handler
def fetch_product_data(url: str) -> Dict[str, Any]:
    """Fetches product data from the given URL."""
    logging.info(f"Fetching product data from {url}")
    response = requests.get(
        url=url,
        proxies=PROXIES,
        verify=False,
    )
    response.raise_for_status()
    logging.info("Product data fetched successfully")
    return response.json()


@error_handler
def fetch_reviews_data(url: str) -> List[Dict[str, Any]]:
    """Fetches customer reviews data from the given URL."""
    logging.info(f"Fetching reviews data from {url}")
    reviews = []
    page = 1

    def fetch_page(page: int) -> List[Dict[str, Any]]:
        logging.info(f"Fetching page {page} of reviews")
        response = requests.get(
            url=url,
            params={"page": page},
            proxies=PROXIES,
            verify=False,
        )
        response.raise_for_status()
        return (
            response.json()[1]
            .get("props", {})
            .get("pageProps", {})
            .get("initialData", {})
            .get("data", {})
            .get("reviews", {})
            .get("customerReviews", [])
        )

    with ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            futures = [executor.submit(fetch_page, page + i) for i in range(10)]
            page_reviews_list = [future.result() for future in as_completed(futures)]

            # Flatten the list of lists
            page_reviews = [
                review for sublist in page_reviews_list for review in sublist
            ]

            if not page_reviews:
                logging.info("No more reviews found")
                break

            reviews.extend(page_reviews)
            page += 10

    logging.info("Reviews data fetched successfully")
    return reviews


def main():
    logging.info("Starting main function")
    product_data = fetch_product_data(PRODUCT_URL)
    reviews_data = fetch_reviews_data(REVIEWS_URL)

    logging.info("Filtering reviews by date")
    product_data["reviews"] = [
        Review(**review)
        for review in filter_reviews_by_date(
            reviews_data,
            start_date="2022-01-01",
        )
    ]

    logging.info("Creating Product object")
    product = Product(**product_data)

    logging.info("Saving product data to JSON")
    save_to_json(product.model_dump(), "product_data.json")
    logging.info("Product data saved successfully")


if __name__ == "__main__":
    main()
