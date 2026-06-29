from typing_extensions import Annotated, TypedDict,NotRequired
from langchain_ollama import ChatOllama
import time


# Define Output Schema
class SentimentAnalysis(TypedDict):
    overall_sentiment: Annotated[
        str,
        "Overall sentiment (Positive, Negative, or Neutral)"
    ]

    confidence_score: Annotated[
        str,
        "Confidence score in percentage"
    ]

    positive_points: Annotated[
        list[str],
        "List of positive points from the review"
    ]

    negative_points: Annotated[
        list[str],
        "List of negative points from the review"
    ]

    final_summary: Annotated[
        str,
        "Short summary of the review"
    ]

    # Optional Fields
    # suggested_improvements: NotRequired[str]
    # recommendation: NotRequired[str]
    # emotion: NotRequired[str]

# Load Model
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)
start = time.time()
# Structured Output
structured_llm = llm.with_structured_output(SentimentAnalysis)

# Invoke Model
response = structured_llm.invoke(
    """I recently stayed at a beach resort for a five-day family vacation. The location was beautiful, with a private beach and an amazing ocean view from our room. The hotel staff greeted us warmly and were always polite and helpful whenever we needed assistance. The room was spacious, clean, and well-maintained, and the breakfast buffet had a wide variety of delicious food options.

However, there were several issues that affected our overall experience. The Wi-Fi connection was extremely slow and often disconnected, making it difficult to work remotely. The air conditioner stopped working on the second night, and although the maintenance team fixed it after a few hours, it caused a lot of discomfort. The swimming pool was overcrowded most of the time, and finding available lounge chairs was difficult. Room service was also slower than expected, with food deliveries sometimes taking more than an hour.

Despite these problems, we enjoyed spending time on the beach, watching the sunset every evening, and participating in the resort's entertainment activities. The staff's friendly attitude and the beautiful surroundings made our stay memorable. I would consider visiting again if the hotel improves its internet service, room maintenance, and customer service response time. Overall, it was a good experience with a few significant areas that need improvement."""
)

end = time.time()

print(f"Time taken: {end - start} seconds")

print(response.get("overall_sentiment", "Not Provided"))
print(response.get("confidence_score", "Not Provided"))
print(response.get("positive_points", []))
print(response.get("negative_points", []))
print(response.get("final_summary", "Not Provided"))
print(response.get("suggested_improvements", []))
print(response.get("recommendation", "Not Provided"))
print(response.get("emotion", "Not Provided"))
