import streamlit as st
import pandas as pd


def render_upload_section():
    """
    Upload section: CSV upload, column mapping, preview, and pipeline trigger.
    Returns a dict with df, text_col, product_col, run_pipeline.
    """

    # --- Upload ---
    st.subheader("Upload Customer Reviews")
    st.caption(
        "Upload a CSV file containing customer reviews to begin."
    )

    uploaded_file = st.file_uploader(
        "Choose CSV file",
        type=["csv"],
        key="upload_csv"
    )

    if uploaded_file is None:
        return None

    # --- Load CSV ---
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return None

    # --- Dataset Configuration ---
    st.subheader("Dataset Configuration")
    st.caption(
        "Upload a CSV containing reviews, product names, and categories. Use the dropdowns to select the review column and the product/category column."
    )


    col_names = list(df.columns)

    # Heuristic defaults
    default_text_idx = next(
        (
            i
            for i, col in enumerate(col_names)
            if col.lower() in [
                "review text",
                "text",
                "review",
                "comment"
            ]
        ),
        0
    )

    default_prod_idx = next(
        (
            i
            for i, col in enumerate(col_names)
            if col.lower() in [
                "title",
                "product_name",
                "product",
                "department name",
                "clothing id"
            ]
        ),
        min(1, len(col_names) - 1)
    )

    c1, c2 = st.columns(2)

    with c1:
        text_col = st.selectbox(
            "Review text column",
            col_names,
            index=default_text_idx,
            key="select_text_col"
        )

    with c2:
        product_col = st.selectbox(
            "Product / category column",
            col_names,
            index=default_prod_idx,
            key="select_prod_col"
        )

    # --- Dataset Preview ---
    st.subheader("Dataset Preview")
    st.caption(
        f"{len(df):,} rows · {len(df.columns):,} columns"
    )

    st.dataframe(
        df.head(5),
        use_container_width=True,
        hide_index=True
    )

   # --- Analysis ---
    st.subheader("Ready to Analyze")
    st.caption(
        "Everything is set. Hit *Analyze Reviews* to let the AI extract sentiment, patterns, and business opportunities from your data."
    )


    run_pipeline = st.button(
        "Analyze Reviews",
        key="run_pipeline_btn"
    )

    return {
        "df": df,
        "text_col": text_col,
        "product_col": product_col,
        "run_pipeline": run_pipeline
    }