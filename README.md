# LLM-eCommerce-Customer-Experience-Reviews
End -to-End LLM model for sentiment analysis on ecommerce customer reviews. Used Langchain, Pydantic, and nesting structured models

# 🛒 Olist E-Commerce LLM Sentiment Analysis & Aspect-Based Opinion Mining

An end-to-end GenAI data processing pipeline that extracts fine-grained, aspect-based sentiment and structured opinions from customer reviews on **Olist** (Brazil's largest e-commerce platform).

This project uses **LangChain**, **Pydantic**, and **OpenAI (`gpt-4o-mini`)** to parse unstructured customer feedback into strongly-typed, nested JSON objects—disentangling opinions on product quality from logistically complex topics like shipping delays.

---

## 🎯 Business Problem & Context
In multi-vendor e-commerce marketplaces like Olist, overall star ratings often obscure critical operational root causes. A customer might leave a 3-star review for a "great product" simply because delivery was delayed by logistics partners. 

Standard aggregate metrics fail to separate seller product quality from platform logistics. This pipeline was built to:
1. **Extract Granular Aspect Sentiment:** Isolate specific topics (e.g., product quality vs. app search vs. shipping delays).
2. **Identify Actionable Feedback:** Extract explicit customer problems and suggested remedies (e.g., *"implement category filters"*).
3. **Enforce Structural Governance:** Leverage LLM structured outputs via Pydantic to ensure 100% schema compliance for downstream analytics warehouses.

---

## 🏗️ Technical Architecture & Workflow

┌───────────────────────────┐
│   Olist Review Payload    │  (Unstructured JSON with review_id, rating, & text)
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│     Prompt Template       │  (Guides LLM on aspect extraction & shipping rules)
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│  OpenAI LLM (gpt-4o-mini) │  (Invoked via LangChain with_structured_output)
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│  Pydantic Schema Validation│  (Enforces nested StructuredReview -> Opinion models)
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│ Structured JSON Analytics │  (Extracted overall sentiment, notable phrases, & opinions)
└───────────────────────────┘


---

## 📐 Data Schema & Model Design

The solution relies on a hierarchical, nested Pydantic schema to capture multiple distinct opinions within a single review.

### 1. Nested Opinion Model (`Opinion`)
Captures fine-grained topic-level breakdown:
* `topic` *(str)*: Specific aspect referenced (e.g., "Discount Program", "Search Algorithm", "Delivery").
* `sentiment` *(str)*: Target sentiment for that specific aspect (Positive/Negative/Neutral).
* `Problem` *(Optional[str])*: Specific bottleneck or issue mentioned by the customer.
* `suggested_solution` *(Optional[str])*: Explicit feature requests or recommendations made by the customer.

### 2. Root Review Model (`StructuredReview`)
Wraps the full analysis into a validated contract:
* `review_id` *(str)*: Unique identifier for the transaction review.
* `overall_sentiment` *(str)*: Macro-level sentiment of the full text.
* `notable_phrases` *(list[str])*: High-impact verbatim excerpts.
* `opinions` *(list[Opinion])*: Array of nested `Opinion` objects representing every distinct claim.

---

## 💻 Tech Stack & API Integration
* **Language:** Python 3.10+
* **LLM Orchestration:** LangChain (`init_chat_model`)
* **Model Provider:** OpenAI (`gpt-4o-mini`)
* **Data Governance & Validation:** Pydantic v2
* **Target Domain:** Olist E-Commerce Brazilian Public Dataset

---

## 📂 Repository Structure

```text
olist-llm-sentiment-analysis/
├── design.md              # Input/Output model design documentation
├── main.py                # LangChain pipeline & Pydantic models execution script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
🚀 Quickstart & How to Run
1. Prerequisites
Set your OpenAI API key as an environment variable:

Bash
export OPENAI_API_KEY="your-openai-api-key-here"
2. Installation
Clone the repository and install required packages:

Bash
git clone [https://github.com/your-username/olist-llm-sentiment-analysis.git](https://github.com/your-username/olist-llm-sentiment-analysis.git)
cd olist-llm-sentiment-analysis
pip install -r requirements.txt
3. Execution
Run the pipeline script:

Bash
python main.py
🔍 Sample Execution Output
Input Text:

"I love the discount program in this app... However, the search functionality is really frustrating... They should implement category filters. The item is great but arrived 3 days after expected..."

Structured Output:

Plaintext
Review ID: R12345
Overall Sentiment: Mixed / Negative
Notable Phrases: saved 30% on my last order, search functionality is really frustrating, arrived 3 days after expected

Opinions:
  - Topic: Discount Program | Sentiment: Positive
  - Topic: Search Functionality | Sentiment: Negative
    Problem: Results are rarely relevant
    Suggestion: Implement category filters and improve search algorithm
  - Topic: Product Quality | Sentiment: Positive
  - Topic: Shipping & Logistics | Sentiment: Negative
    Problem: Arrived 3 days after expected date

---

### How to add this to your GitHub repository:
1. Open VS Code in your local project folder.
2. Create a file named **`README.md`** in the root directory.
3. Paste the markdown code above into the file and save.
4. Run these terminal commands to push it to GitHub:

```bash
git add .
git commit -m "Add README documentation for Olist LLM Sentiment Analysis project"
git push
