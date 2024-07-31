from typing import List, Dict, Optional
from pydantic import BaseModel, Field, HttpUrl


class GlassBadge(BaseModel):
    """Represents a glass badge associated with a badge."""

    id: str
    text: str


class Badge(BaseModel):
    """Represents a badge associated with a review."""

    badge_type: str = Field(alias="badgeType")
    content_type: str = Field(alias="contentType")
    id: str
    glass_badge: Optional[GlassBadge] = Field(alias="glassBadge")


class MediaSize(BaseModel):
    """Represents the size of a media item."""

    id: str
    url: str


class Photo(BaseModel):
    """Represents a photo associated with a review."""

    caption: Optional[str]
    id: str
    sizes: Dict[str, MediaSize]


class Media(BaseModel):
    """Represents a media item associated with a review."""

    id: str
    review_id: str = Field(alias="reviewId")
    media_type: str = Field(alias="mediaType")
    normal_url: HttpUrl = Field(alias="normalUrl")
    thumbnail_url: HttpUrl = Field(alias="thumbnailUrl")
    caption: Optional[str]
    rating: int


class Review(BaseModel):
    """Represents a customer review for a product."""

    author_id: str = Field(alias="authorId")
    badges: List[Badge]
    user_location: Optional[str] = Field(alias="userLocation")
    negative_feedback: int = Field(alias="negativeFeedback")
    positive_feedback: int = Field(alias="positiveFeedback")
    rating: int
    recommended: Optional[bool]
    review_id: str = Field(alias="reviewId")
    review_submission_time: str = Field(alias="reviewSubmissionTime")
    review_text: str = Field(alias="reviewText")
    review_title: Optional[str] = Field(alias="reviewTitle")
    review_aspect_start: Optional[int] = Field(alias="reviewAspectStart")
    review_aspect_end: Optional[int] = Field(alias="reviewAspectEnd")
    review_sentiment_start: Optional[int] = Field(alias="reviewSentimentStart")
    review_sentiment_end: Optional[int] = Field(alias="reviewSentimentEnd")
    snippet_from_title: Optional[str] = Field(alias="snippetFromTitle")
    show_recommended: Optional[bool] = Field(alias="showRecommended")
    client_responses: Optional[List[Dict]] = Field(alias="clientResponses")
    syndication_source: Optional[str] = Field(alias="syndicationSource")
    user_nickname: str = Field(alias="userNickname")
    external_source: str = Field(alias="externalSource")
    media: List[Media]
    photos: List[Photo]


class Product(BaseModel):
    """Represents a product with its details and customer reviews."""

    id: str = Field(alias="sku")
    url: str
    name: str
    image: HttpUrl
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
    reviews: List[Review]

    class Config:
        """Configuration for the Product model."""

        populate_by_name = True
