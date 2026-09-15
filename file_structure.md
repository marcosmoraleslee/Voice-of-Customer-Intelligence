Project Structure Breakdown
src/: Houses all core production code, ensuring clear separation of concerns across data cleaning, machine learning inference, semantic clustering, and LLM prompt templates.

models/: Stores the serialized fine-tuned RoBERTa model artifacts required for real-time sentiment scoring.

notebooks/: Contains the documented notebooks used for exploratory data analysis, model training, and the comprehensive backend integration tests we just completed.

app.py: The upcoming user-facing dashboard script that will import these backend modules to deliver real-time cluster intelligence and product audits through an interactive Streamlit interface.



sentiment_business_intelligence/
│
├── data/
│   ├── raw/
│   │   └── womens_clothing_reviews_raw.csv
│   └── processed/
│       ├── womens_clothing_balanced_reviews.csv
│       ├── womens_clothing_balanced_roberta_reviews.csv
│       └── clustered_reviews.json
│
├── notebooks/
│   ├── 01_experimentation_pipeline.ipynb
│   └── 02_clustering_and_summarization.ipynb
│
├── models/
│   ├── fine_tuned_roberta/
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