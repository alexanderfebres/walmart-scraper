from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class Review(BaseModel):
    """Represents a customer review for a product."""

    user_nickname: Optional[str] = Field(alias="userNickname", default=None)
    rating: int
    recommended: Optional[bool]
    user_location: Optional[str] = Field(alias="userLocation", default=None)
    negative_feedback: int = Field(alias="negativeFeedback", default=None)
    positive_feedback: int = Field(alias="positiveFeedback", default=None)
    author_id: Optional[str] = Field(alias="authorId", default=None)
    review_id: str = Field(alias="reviewId")
    review_submission_time: str = Field(alias="reviewSubmissionTime")
    review_text: str = Field(alias="reviewText")
    review_title: Optional[str] = Field(alias="reviewTitle", default=None)
    review_aspect_start: Optional[int] = Field(alias="reviewAspectStart", default=None)
    review_aspect_end: Optional[int] = Field(alias="reviewAspectEnd", default=None)
    review_sentiment_start: Optional[int] = Field(
        alias="reviewSentimentStart", default=None
    )
    review_sentiment_end: Optional[int] = Field(
        alias="reviewSentimentEnd", default=None
    )
    snippet_from_title: Optional[str] = Field(alias="snippetFromTitle", default=None)
    show_recommended: Optional[bool] = Field(alias="showRecommended", default=None)
    client_responses: Optional[List[Dict]] = Field(
        alias="clientResponses",
        default=None,
    )


class Product(BaseModel):
    """Represents a product with its details and customer reviews."""

    id: str = Field(alias="sku")
    url: str
    name: str
    image: str
    description: str
    model: str
    brand: str
    rating_value: float = Field(alias="ratingValue")
    best_rating: int = Field(alias="bestRating")
    review_count: int = Field(alias="reviewCount")
    price_currency: str = Field(alias="priceCurrency")
    price: float
    availability: str
    item_condition: str = Field(alias="itemCondition")
    reviews: List[Review] = []

    class Config:
        """Configuration for the Product model."""

        populate_by_name = True
