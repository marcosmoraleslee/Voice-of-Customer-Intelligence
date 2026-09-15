import streamlit as st
import pandas as pd


def render_kpi_overview(df, text_col, product_col):
    """
    Render the Executive Overview with high-level customer perception metrics.
    """

    if df is None or df.empty:
        st.warning("No review data is available for the Executive Overview.")
        return

    total_rows = len(df)

    positive_count = (df["predicted_sentiment"] == "Positive").sum()
    neutral_count = (df["predicted_sentiment"] == "Neutral").sum()
    negative_count = (df["predicted_sentiment"] == "Negative").sum()

    positive_pct = positive_count / total_rows * 100
    neutral_pct = neutral_count / total_rows * 100
    negative_pct = negative_count / total_rows * 100

    # Detect an available rating column without assuming one specific name.
    rating_col = None

    rating_candidates = [
        "Rating",
        "rating",
        "Review Rating",
        "review_rating",
        "review rating",
    ]

    for candidate in rating_candidates:
        if candidate in df.columns:
            rating_col = candidate
            break

    average_rating = None

    if rating_col:
        rating_values = pd.to_numeric(
            df[rating_col],
            errors="coerce"
        ).dropna()

        if not rating_values.empty:
            average_rating = rating_values.mean()

    # Identify the product/category with the highest review volume.
    largest_product = None
    largest_product_count = None

    if product_col in df.columns:
        product_counts = (
            df[product_col]
            .dropna()
            .astype(str)
            .value_counts()
        )

        if not product_counts.empty:
            largest_product = product_counts.index[0]
            largest_product_count = product_counts.iloc[0]

    # Executive Overview header.
    st.markdown(
        """
        <div class="flat-section">
            <div class="card">
                <h2>Executive Overview</h2>
                <p style="font-size:0.95rem; color:#C7C9D3;">
                    What is happening with our customers?
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Main customer perception metrics.
    metric_count = 5 if average_rating is not None else 4
    columns = st.columns(metric_count)

    with columns[0]:
        st.metric("Reviews", f"{total_rows:,}")

    with columns[1]:
        st.metric("Positive", f"{positive_pct:.1f}%")

    with columns[2]:
        st.metric("Neutral", f"{neutral_pct:.1f}%")

    with columns[3]:
        st.metric("Negative", f"{negative_pct:.1f}%")

    if average_rating is not None:
        with columns[4]:
            st.metric(
                "Average Rating",
                f"{average_rating:.1f} / 5"
            )

    # Additional context.
    if largest_product is not None:
        st.markdown(
            f"""
            <div class="card">
                <p style="font-size:0.8rem; color:#9FA4AE; margin-bottom:0.35rem;">
                    Largest Review Category
                </p>
                <p style="font-size:1.05rem; font-weight:600; margin:0;">
                    {largest_product} · {largest_product_count:,} reviews
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )