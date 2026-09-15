import streamlit as st
import pandas as pd


def render_sentiment_rankings(df, product_col):
    """
    Render the top customer love and customer dislike rankings.

    Positive and negative feedback are ranked independently.
    Neutral feedback does not influence either ranking.

    Selecting a product stores the selected product and analysis direction
    in Streamlit session state for the Product Deep Dive.
    """

    if df is None or df.empty:
        st.warning("No processed dataset available for customer insights.")
        return

    if "predicted_sentiment" not in df.columns:
        st.warning("Sentiment results are not available.")
        return

    if product_col not in df.columns:
        st.warning("The selected product/category column is not available.")
        return

    ranking_df = df[[product_col, "predicted_sentiment"]].copy()
    ranking_df = ranking_df.dropna(subset=[product_col])

    if ranking_df.empty:
        st.warning("No valid product/category data is available.")
        return

    ranking_df[product_col] = ranking_df[product_col].astype(str)

    grouped = (
        ranking_df.groupby(product_col)["predicted_sentiment"]
        .value_counts()
        .unstack(fill_value=0)
    )

    for sentiment in ["Positive", "Negative"]:
        if sentiment not in grouped.columns:
            grouped[sentiment] = 0

    grouped = grouped[["Positive", "Negative"]]

    grouped["decision_reviews"] = (
        grouped["Positive"] + grouped["Negative"]
    )

    grouped = grouped[grouped["decision_reviews"] > 0].copy()

    positive_global_rate = (
        grouped["Positive"].sum()
        / grouped["decision_reviews"].sum()
    )

    grouped["positive_share"] = (
        grouped["Positive"]
        / grouped["decision_reviews"]
    )

    smoothing_strength = 20

    grouped["positive_score"] = (
        (
            grouped["decision_reviews"]
            / (
                grouped["decision_reviews"]
                + smoothing_strength
            )
        )
        * grouped["positive_share"]
        + (
            smoothing_strength
            / (
                grouped["decision_reviews"]
                + smoothing_strength
            )
        )
        * positive_global_rate
    )

    top_positive = (
        grouped
        .sort_values(
            by=["positive_score", "decision_reviews"],
            ascending=[False, False],
        )
        .head(20)
        .reset_index()
    )

    negative_global_rate = (
        grouped["Negative"].sum()
        / grouped["decision_reviews"].sum()
    )

    grouped["negative_share"] = (
        grouped["Negative"]
        / grouped["decision_reviews"]
    )

    grouped["negative_score"] = (
        (
            grouped["decision_reviews"]
            / (
                grouped["decision_reviews"]
                + smoothing_strength
            )
        )
        * grouped["negative_share"]
        + (
            smoothing_strength
            / (
                grouped["decision_reviews"]
                + smoothing_strength
            )
        )
        * negative_global_rate
    )

    top_negative = (
        grouped
        .sort_values(
            by=["negative_score", "decision_reviews"],
            ascending=[False, False],
        )
        .head(20)
        .reset_index()
    )

    if "selected_deep_dive_product" not in st.session_state:
        st.session_state.selected_deep_dive_product = None

    if "selected_deep_dive_sentiment" not in st.session_state:
        st.session_state.selected_deep_dive_sentiment = None

    st.markdown(
    """
    <div class="flat-section">
        <div class="card">
            <h2>Customer Feedback Signals</h2>
            <p style="font-size:0.95rem; color:#C7C9D3;">
                Explore the 10 best‑rated and 10 worst‑rated products or categories based on customer sentiment. 
                Select any item to open its detailed analysis with strategic insights and recommended actions.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(
            """
            <div class="card" style="margin-top:1rem;">
                <h3>What Customers Love</h3>
                <p style="font-size:0.9rem; color:#C7C9D3;">
                    Top products based on positive customer feedback.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if top_positive.empty:
            st.info("No positive reviews are available.")
        else:
            for rank, row in enumerate(
                top_positive.itertuples(index=False),
                start=1,
            ):
                product_name = getattr(row, product_col)
                positive_share = row.positive_share * 100
                review_count = int(row.decision_reviews)

                button_label = (
                    f"{rank}. {product_name}  ·  "
                    f"{positive_share:.1f}% positive  ·  "
                    f"{review_count} reviews"
                )

                if st.button(
                    button_label,
                    key=f"positive_product_{rank}_{product_name}",
                    use_container_width=True,
                ):
                    st.session_state.selected_deep_dive_product = product_name
                    st.session_state.selected_deep_dive_sentiment = "Positive"

    with right_column:
        st.markdown(
            """
            <div class="card" style="margin-top:1rem;">
                <h3>What Customers Dislike</h3>
                <p style="font-size:0.9rem; color:#C7C9D3;">
                    Top products based on negative customer feedback.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if top_negative.empty:
            st.info("No negative reviews are available.")
        else:
            for rank, row in enumerate(
                top_negative.itertuples(index=False),
                start=1,
            ):
                product_name = getattr(row, product_col)
                negative_share = row.negative_share * 100
                review_count = int(row.decision_reviews)

                button_label = (
                    f"{rank}. {product_name}  ·  "
                    f"{negative_share:.1f}% negative  ·  "
                    f"{review_count} reviews"
                )

                if st.button(
                    button_label,
                    key=f"negative_product_{rank}_{product_name}",
                    use_container_width=True,
                ):
                    st.session_state.selected_deep_dive_product = product_name
                    st.session_state.selected_deep_dive_sentiment = "Negative"

    selected_product = st.session_state.selected_deep_dive_product
    selected_sentiment = st.session_state.selected_deep_dive_sentiment

    if selected_product is not None:
        st.markdown(
            f"""
            <div class="card" style="margin-top:1rem;">
                <p style="font-size:0.8rem; color:#9FA4AE; margin-bottom:0.35rem;">
                    Selected for Product Deep Dive
                </p>
                <p style="font-size:1.05rem; font-weight:600; margin:0;">
                    {selected_product} · {selected_sentiment} feedback
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )