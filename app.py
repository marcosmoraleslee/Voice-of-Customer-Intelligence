import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# --- ENV & OPENAI ---
from dotenv import load_dotenv
import os
from openai import OpenAI

# --- Import Dashboard Modules ---
from src.dashboard.header import render_header
from src.dashboard.upload_section import render_upload_section
from src.dashboard.sentiment_kpis import render_kpi_overview
from src.dashboard.category_charts import render_category_charts
from src.dashboard.sentiment_rankings import render_sentiment_rankings
from src.dashboard.executive_audit import render_executive_audit

# --- Load CSS Theme ---
from styles.theme import apply_theme


# --- Load CSS ---
def load_css():
    apply_theme(st)


# --- Load RoBERTa Model ---
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    return tokenizer, model


# --- Sentiment Inference ---
def run_sentiment_pipeline(df, text_col):
    tokenizer, model = load_model()

    sentiments = []
    confidences = []

    for text in df[text_col].astype(str).tolist():
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            scores = torch.softmax(outputs.logits, dim=1).tolist()[0]

        labels = ["Negative", "Neutral", "Positive"]
        pred_label = labels[scores.index(max(scores))]
        pred_conf = max(scores)

        sentiments.append(pred_label)
        confidences.append(pred_conf)

    df["predicted_sentiment"] = sentiments
    df["confidence"] = confidences

    return df


# --- Streamlit App ---
def main():

    # --- SESSION STATE INITIALIZATION ---
    if "df" not in st.session_state:
        st.session_state.df = None

    if "processed_df" not in st.session_state:
        st.session_state.processed_df = None

    if "openai_client" not in st.session_state:
        st.session_state.openai_client = None

    if "pipeline_ran" not in st.session_state:
        st.session_state.pipeline_ran = False

    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None

    # --- PAGE CONFIG ---
    st.set_page_config(
        page_title="Sentiment & AI Intelligence Dashboard",
        layout="wide"
    )

    # Load CSS
    load_css()

    # --- LOAD ENV ---
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # --- INITIALIZE OPENAI CLIENT ---
    if OPENAI_API_KEY:
        st.session_state.openai_client = OpenAI(api_key=OPENAI_API_KEY)
    else:
        st.error("OPENAI_API_KEY not loaded. Check your .env file.")

    # Header
    render_header()

    # Upload Section
    upload_data = render_upload_section()
    if upload_data is None:
        st.stop()

    # Save uploaded data in session
    st.session_state.df = upload_data["df"]
    text_col = upload_data["text_col"]
    product_col = upload_data["product_col"]
    run_pipeline = upload_data["run_pipeline"]

    # --- Run Pipeline ---
    if run_pipeline:
        with st.spinner("Running RoBERTa sentiment pipeline..."):
            st.session_state.processed_df = run_sentiment_pipeline(st.session_state.df, text_col)

        st.session_state.pipeline_ran = True
        st.success("Pipeline completed successfully.")

    # --- If pipeline already ran, show dashboard ---
    if st.session_state.pipeline_ran:

        processed_df = st.session_state.processed_df

        # KPI Overview
        render_kpi_overview(processed_df, text_col, product_col)

        # Category Charts
        render_category_charts(processed_df, product_col)

        # Rankings
        render_sentiment_rankings(processed_df, product_col)

        # Executive Audit
        st.markdown("<hr/>", unsafe_allow_html=True)

        render_executive_audit(
            processed_df,
            product_col,
            text_col,
            st.session_state.openai_client
        )

    else:
        st.info("Upload a dataset and click the pipeline button to generate insights.")


if __name__ == "__main__":
    main()
