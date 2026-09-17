from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Optional


# from dotenv import load_dotenv
# load_dotenv()


llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#Opinion Model
class Opinion(BaseModel):
  topic: str=Field(description="The topic of the opinion")
  sentiment: str=Field(description="The sentiment of the opinion")
  Problem: Optional[str]=Field(description = "the problem of the opinion, if any")
  suggested_solution: Optional[str]=Field(description = 'The suggested solution of the opinion, if any')

#Structured Review Model
class StructuredReview (BaseModel):
  review_id: str=Field(description="The ID of the review")
  overall_sentiment: str=Field(description = "the sentiment of the review")
  notable_phrases: list[str]=Field(description ="The notable phrases of the review")
  opinions: list[Opinion]=Field(description="The opinions of the review")

#create structured LLM 
structured_llm = llm.with_structured_output(StructuredReview)

prompt_template_str = """
With the Olist data, go through the opinions from the reviews and provide
overall sentiment, notable phrases and any opinions in the review. 
Note if customers opinions are based on shipping delays (if any) or  product reviews
{input}

"""
# Define the review string
review_str_1 = """
{
    "review_id": "R12345",
    "Customer_id": "C0001",
    "date": "2025-01-01",
    "rating": "★★★☆☆ (3 stars)",
    "text": "I love the discount program in this app - saved 30% on my last order! However, the search functionality is really frustrating. Results are rarely relevant to what I'm looking for. They should implement category filters and improve their search algorithm.The item is great but arrived 3 days after expected. I needed it for an event, and I didn’t receive it in time. I will be returning. Very disappointed because this would have been perfect at my event",
} """
review_str_2 = """{
    "review_id": "R96042",
    "Customer_id": "C0002",
    "date": "2025-01-01",
    "rating" : "★★★☆☆ (3 stars)", 
    "text": " Great product and received on time. Highly recommend"
}"""
prompt_template = PromptTemplate.from_template(prompt_template_str)


def get_response(input):
    prompt = prompt_template.format(input=input)
    response = structured_llm.invoke(prompt)
    return response

for review in [review_str_1, review_str_2]:
  response_content = get_response(review)
  print(f"Review ID: {response_content.review_id}")
  print(f"Overall Sentiment: {response_content.overall_sentiment}")
  print(f"Notable Phrases: {', '.join(response_content.notable_phrases)}")
  print("\nOpinions:")
  for op in response_content.opinions:
      print(f"  - Topic: {op.topic} | Sentiment: {op.sentiment}")
      if op.Problem:
          print(f"    Problem: {op.Problem}")
      if op.suggested_solution:
          print(f"    Suggestion: {op.suggested_solution}")

