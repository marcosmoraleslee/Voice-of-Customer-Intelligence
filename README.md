# Voice of Customer Intelligence

An AI-powered customer reviews intelligence application that transforms unstructured customer feedback into **sentiment insights, customer patterns, product-level analysis, and actionable business recommendations**.

The project combines **NLP, sentiment analysis, semantic clustering, and Generative AI** in a Streamlit application designed to help e-commerce, marketing, product, and customer experience teams understand what customers love, what they dislike, and where the business should act.

The core idea is simple:

> **Customer Reviews → Sentiment → Patterns → Business Insights → Recommended Actions**

---

# Overview

Customer reviews contain valuable information about product quality, customer expectations, recurring problems, and purchase drivers.

However, manually analyzing large volumes of reviews makes it difficult to identify recurring signals and translate them into useful business decisions.

Customer Reviews Intelligence addresses this problem by providing a Streamlit application where users can **upload their own customer review dataset**, configure the relevant columns, and generate an AI-powered analysis.

The application can:

- Classify reviews as **Positive, Neutral, or Negative**
- Calculate sentiment and confidence metrics
- Analyze customer feedback by product or category
- Identify products or categories receiving strong positive or negative feedback
- Surface recurring customer feedback patterns
- Generate business-oriented interpretations using an LLM
- Produce strategic recommendations for selected products

The application is designed as a **generic review-analysis workflow** rather than a dashboard tied to a single training dataset.

---

# Business Problem

Customer reviews can reveal important information about:

- Product quality
- Fit and comfort
- Materials and durability
- Customer expectations
- Product perception
- Recurring complaints
- Customer experience
- Product strengths
- Potential marketing opportunities

But raw review data does not immediately answer questions such as:

- Which products are generating customer satisfaction?
- Which products are creating dissatisfaction?
- What do customers repeatedly praise?
- What problems appear across negative feedback?
- Which product attributes are most valued?
- Where should product or marketing teams investigate further?
- What actions could the business consider?

Traditional sentiment analysis answers:

> **"Is this review positive, neutral, or negative?"**

This project goes one step further:

> **"What does this customer feedback tell us about the business, and where should we investigate or act?"**

---

# Solution

The project combines traditional NLP and machine learning with Generative AI to create a business-oriented customer feedback workflow.

```text
                Customer Review CSV
                        │
                        ▼
                 Dataset Configuration
                        │
                        ▼
                Sentiment Analysis
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Positive       Neutral      Negative
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                Customer Feedback
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   Positive Signals            Negative Signals
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 Product Deep Dive
                        │
                        ▼
                  LLM Analysis
                        │
                        ▼
             Business Interpretation
                        │
                        ▼
             Strategic Recommendations
```

Separately, the data science notebooks provide the model development and semantic clustering workflow used to explore the review dataset and validate the project's backend components.

---

# Streamlit Application

The main application is designed for users who want to analyze a **new customer review dataset**, rather than only the dataset used during model development.

A user can upload a CSV and configure:

- Review text column
- Product or category column

<img width="1910" height="642" alt="image" src="https://github.com/user-attachments/assets/53c81ea1-9607-4652-acff-bfb00ecdd2a6" />


The application then processes the uploaded data and presents the analysis through a business-oriented interface.

<img width="1907" height="535" alt="image" src="https://github.com/user-attachments/assets/af4ae6cf-94ea-4f16-93cb-ef2b8163147d" />


The main workflow is:

```text
Upload Customer Reviews
          ↓
Analyze Reviews
          ↓
Executive Overview
          ↓
What Customers Love
          ↓
What Customers Dislike
          ↓
Product Deep Dive
          ↓
AI Business Analysis
```

---

# Executive Overview

The Executive Overview answers:

> **What is happening with our customers?**

It provides a high-level view of the uploaded dataset, including:

- Total number of reviews
- Positive sentiment percentage
- Neutral sentiment percentage
- Negative sentiment percentage
- Largest review category or product group
- Sentiment distribution across the selected dimension

The goal is to provide a quick understanding of the overall customer feedback landscape before moving into deeper analysis.

<img width="1905" height="850" alt="image" src="https://github.com/user-attachments/assets/565d9d1b-a180-4f04-8d14-e322a5148d96" />


---

# What Customers Love

The application identifies products or categories receiving strong positive customer feedback.

The analysis can reveal:

- Product strengths
- Attributes customers value
- Positive customer experiences
- Potential marketing messages
- Customer value drivers
- Opportunities to reinforce successful product characteristics

The objective is not simply to identify the products with the most positive reviews, but to understand **why customers respond positively**.

---

# What Customers Dislike

The application identifies products or categories receiving strong negative customer feedback.

The analysis can reveal:

- Quality problems
- Durability issues
- Fit or sizing problems
- Expectation gaps
- Recurring customer complaints
- Potential customer experience risks
- Areas that may require further investigation

<img width="1907" height="853" alt="image" src="https://github.com/user-attachments/assets/5db159e4-f830-4417-be4b-d7b82c528fa3" />


This helps move from:

> **"Customers are unhappy."**

to:

> **"What specifically is creating that dissatisfaction?"**

---

# Product Deep Dive

The Product Deep Dive allows the user to select a product or category and investigate the customer feedback behind it.

The analysis separates positive and negative customer feedback.

For positive feedback, the application can identify areas such as:

- Sales & Customer Value
- Promotional Opportunities
- Marketing Opportunities
- Competitive Intelligence
- Strategic Recommendations

For negative feedback, the analysis can identify areas such as:

- Early Warnings
- Product Issues
- Operational or Logistics Issues when supported by the reviews
- Customer Experience Risks
- Strategic Recommendations

The LLM is used to interpret the available review evidence and translate it into business-oriented insights.

The system is designed to avoid inventing unsupported business facts such as revenue, conversion rates, or financial impact.

---

# Generative AI Layer

Sentiment classification alone does not explain **why** customers feel a certain way or what a business could investigate next.

The project therefore uses an LLM as an **interpretation and recommendation layer**.

The LLM receives structured information derived from the customer reviews and generates business-oriented analysis.

Its role is to:

1. Interpret customer feedback
2. Identify relevant strengths or weaknesses
3. Translate review signals into business language
4. Suggest potential actions

The underlying sentiment analysis remains separate from the Generative AI layer.

This creates a simple architecture:

```text
Customer Reviews
       ↓
NLP / Sentiment Analysis
       ↓
Structured Review Signals
       ↓
LLM Interpretation
       ↓
Business Insights
       ↓
Strategic Recommendations
```

<img width="1907" height="855" alt="image" src="https://github.com/user-attachments/assets/5452b9cd-2702-4a92-b764-280f64532ea2" />


---

# From Sentiment Analysis to Business Intelligence

The main objective of the project is to demonstrate the transition from an AI prediction to a business decision-support workflow.

```text
                 AI / NLP
                    │
                    ▼
            Sentiment Detection
                    │
                    ▼
          Customer Feedback Signals
                    │
                    ▼
           Product-Level Analysis
                    │
                    ▼
             LLM Interpretation
                    │
                    ▼
            Business Opportunities
                    │
                    ▼
          Strategic Recommendations
```

The sentiment model helps answer:

> **What is happening?**

The review patterns help answer:

> **What are customers repeatedly saying?**

The LLM helps answer:

> **What could these signals mean for the business?**

The final recommendations answer:

> **What could the business consider doing next?**

---

# Machine Learning Pipeline

The project separates model development and experimentation from the user-facing application.

## Notebook 1 — Sentiment Model Development

The first notebook contains the sentiment model development workflow.

It includes:

- Review data preparation
- Sentiment label preparation
- Neutral-review curation
- Dataset balancing
- Training and validation split
- Tokenization
- RoBERTa fine-tuning
- Model evaluation
- Best-model export

The resulting fine-tuned model is stored under:

```text
models/fine_tuned_roberta/best_model/
```

The model was developed as part of the project's machine learning experimentation workflow.

---

## Notebook 2 — Semantic Clustering & Backend Validation

The second notebook contains the semantic clustering workflow and backend validation tests.

It includes:

- Sentence-Transformer embeddings
- UMAP dimensionality reduction
- HDBSCAN clustering
- Cluster artifact export
- Backend module validation
- Cluster-level AI simulation
- Product-level AI simulation

The clustering workflow produces:

```text
models/vector_store/
├── umap_reducer.pkl
└── hdbscan_clusterer.pkl
```

and:

```text
data/processed/clustered_reviews.json
```

The notebook also validates the reusable backend modules and tests the LLM analysis workflow using controlled examples.

---

# Model Architecture

The project uses different components for different stages of the workflow.

### Sentiment Analysis

The Streamlit application uses:

```text
cardiffnlp/twitter-roberta-base-sentiment
```

to classify uploaded reviews into:

- Negative
- Neutral
- Positive

The data science notebooks additionally contain a fine-tuned RoBERTa model developed specifically for the project's sentiment experimentation and backend validation.

### Semantic Representation

The clustering workflow uses:

```text
all-MiniLM-L6-v2
```

to generate semantic review embeddings.

### Dimensionality Reduction

```text
UMAP
```

is used to reduce the semantic representations for clustering and visualization.

### Clustering

```text
HDBSCAN
```

is used to discover groups of semantically related reviews.

### Generative AI

```text
OpenAI API
```

is used to interpret structured review information and generate business-oriented analysis and recommendations.

---

# Technology Stack

## Machine Learning & NLP

- Python
- PyTorch
- Hugging Face Transformers
- RoBERTa
- Sentence Transformers
- NLP / Sentiment Analysis

## Unsupervised Learning

- UMAP
- HDBSCAN
- Semantic embeddings

## Generative AI

- OpenAI API
- Large Language Models
- Prompt engineering
- AI-powered business analysis

## Application

- Streamlit
- Pandas
- Custom CSS

## Development

- Jupyter Notebooks
- Python modules
- Serialized ML artifacts
- Environment variables for API configuration

---

# Project Structure

```text
sentiment_business_intelligence/
│
├── data/
│   ├── raw/
│   │   └── womens_clothing_reviews_raw.csv
│   │
│   └── processed/
│       ├── womens_clothing_reviews_cleaned.csv
│       ├── womens_clothing_reviews_roberta.csv
│       ├── womens_clothing_balanced_roberta_reviews.csv
│       └── clustered_reviews.json
│
├── notebooks/
│   ├── 01_experimentation_pipeline.ipynb
│   └── 02_clustering_and_summarization.ipynb
│
├── models/
│   ├── fine_tuned_roberta/
│   │   └── best_model/
│   │
│   └── vector_store/
│       ├── umap_reducer.pkl
│       └── hdbscan_clusterer.pkl
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── model_training.py
│   ├── clustering.py
│   └── llm_analyzer.py
│
├── styles/
│   ├── __init__.py
│   ├── theme.py
│   └── custom_css.py
│
├── assets/
│   └── fonts/
│
├── .env
├── .gitignore
├── requirements.txt
└── app.py
```

> **Note:** `.env` should remain local and must never contain API keys in the GitHub repository.

---

# Application Architecture

The project uses a simple separation between the data science workflow, reusable backend modules, and the Streamlit application.

```text
┌─────────────────────────────────┐
│       Data Science Layer        │
│                                 │
│  Sentiment Model Development    │
│  Semantic Embeddings            │
│  UMAP                           │
│  HDBSCAN                        │
│  Model / Cluster Artifacts      │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│        Backend Modules          │
│                                 │
│  Text Preprocessing             │
│  Sentiment Inference            │
│  Review Clustering              │
│  LLM Prompt Generation          │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│       Streamlit Application     │
│                                 │
│  Upload CSV                     │
│  Dataset Configuration          │
│  Sentiment Analysis             │
│  Executive Overview             │
│  Positive / Negative Signals    │
│  Product Deep Dive              │
│  LLM Business Analysis          │
└─────────────────────────────────┘
```

The application is intentionally kept simple: the user does not need to understand the underlying NLP or clustering implementation to use the analysis.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd sentiment_business_intelligence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

Upload a CSV containing customer reviews.

Then:

1. Select the review text column.
2. Select the product or category column.
3. Run the analysis.
4. Explore the Executive Overview.
5. Review positive and negative customer signals.
6. Select a product or category for a deeper analysis.
7. Review the AI-generated business insights and recommendations.

---

# Example Dataset

The project was developed and tested using a women's clothing customer review dataset.

The Streamlit application is **not limited to that dataset**.

Users can upload another CSV containing customer review data and select the relevant review and product/category columns.

For portfolio demonstrations, smaller datasets can also be used to keep the application responsive while preserving the complete analysis workflow.

---

# Potential Business Use Cases

## E-commerce

Identify products generating customer satisfaction or dissatisfaction.

## Product Management

Discover recurring quality, durability, fit, sizing, or expectation issues.

## Marketing

Identify product attributes that customers value and translate them into potential marketing messages.

## Customer Experience

Detect recurring sources of customer frustration and identify areas that may require investigation.

## Brand Management

Identify positive associations and potential risks in customer perception.

## Business Intelligence

Transform large volumes of unstructured customer feedback into structured information that can support business decisions.

---

# Business Value

The project demonstrates how traditional machine learning and Generative AI can be combined to solve a practical business problem.

Rather than stopping at sentiment classification, the system translates customer feedback into a workflow that business users can understand:

```text
Raw Customer Feedback
        ↓
AI Analysis
        ↓
Customer Signals
        ↓
Business Interpretation
        ↓
Potential Actions
```

The core value proposition is:

> **Turn customer reviews into a clear picture of what customers value, what is going wrong, and where the business should investigate or act.**

---

# Future Improvements

Potential future extensions include:

- Topic-level trend analysis over time
- Detection of emerging negative issues
- Sentiment trends by product category
- Integration with e-commerce platforms
- Integration with customer service data
- Review analysis by customer journey stage
- Automated monitoring of new reviews
- Competitive review intelligence
- Multilingual sentiment analysis
- Automated reporting for marketing and product teams

---

# Project Objective

This project was built as a practical demonstration of applying AI and NLP to a real business problem.

The objective is not only to build a machine-learning model, but to demonstrate how AI can connect:

> **Data → AI → Insights → Business Decisions**

The project combines:

- Machine learning
- Natural language processing
- Semantic clustering
- Generative AI
- Business analysis
- A user-facing Streamlit application

The final result is a project focused on **turning unstructured customer feedback into actionable business intelligence**.
