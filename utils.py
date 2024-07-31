import json
from datetime import datetime
from typing import List, Dict, Any, Optional


def filter_reviews_by_date(
    reviews: List[Dict[str, Any]],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Filters reviews by date range. Dates should be in 'YYYY-MM-DD' format."""
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    filtered_reviews = []
    for review in reviews:
        if isinstance(review, dict):
            review_date_str = review.get("reviewSubmissionTime")
            if review_date_str:
                review_date = datetime.strptime(review_date_str, "%m/%d/%Y")
                if (not start_date or review_date >= start_date) and (
                    not end_date or review_date <= end_date
                ):
                    filtered_reviews.append(review)
    return filtered_reviews


def load_json(file_path: str) -> Dict[str, Any]:
    """Loads JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)


def save_to_json(data: Dict[str, Any], file_path: str):
    """Saves data to a JSON file."""
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
