import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def render_category_charts(df, product_col):
    if df is None or df.empty or "predicted_sentiment" not in df.columns or product_col not in df.columns:
        return

    chart_df = df[[product_col, "predicted_sentiment"]].dropna(subset=[product_col]).copy()
    chart_df[product_col] = chart_df[product_col].astype(str)

    sentiment_counts = chart_df.groupby([product_col, "predicted_sentiment"]).size().unstack(fill_value=0)
    for sentiment in ["Positive", "Neutral", "Negative"]:
        if sentiment not in sentiment_counts.columns:
            sentiment_counts[sentiment] = 0

    sentiment_counts = sentiment_counts[["Positive", "Neutral", "Negative"]]
    sentiment_counts["Total"] = sentiment_counts.sum(axis=1)

    sentiment_percentages = sentiment_counts[["Positive", "Neutral", "Negative"]].div(sentiment_counts["Total"], axis=0) * 100
    sentiment_percentages = sentiment_percentages.sort_values(by="Positive", ascending=True)

    max_categories = 15
    if len(sentiment_percentages) > max_categories:
        sentiment_percentages = sentiment_percentages.tail(max_categories)

    st.markdown(
    """
    <div class="flat-section" style="margin-bottom: 1rem;">
        <div class="card">
            <h2>Customer Sentiment by Category or Product</h2>
            <p style="font-size:0.95rem; color:#4F5A54;">
                View sentiment across your selected dimension. Depending on your configuration above, 
                you’ll see either product‑level or category‑level insights. 
                <i>Tip: Click any item below to open its executive audit.</i>
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=sentiment_percentages.index, x=sentiment_percentages["Positive"],
        name="Positive", orientation="h", marker_color="#70C04B",
        hovertemplate="%{y}<br>Positive: %{x:.1f}%<extra></extra>"
    ))
    fig.add_trace(go.Bar(
        y=sentiment_percentages.index, x=sentiment_percentages["Neutral"],
        name="Neutral", orientation="h", marker_color="#6B7075",
        hovertemplate="%{y}<br>Neutral: %{x:.1f}%<extra></extra>"
    ))
    fig.add_trace(go.Bar(
        y=sentiment_percentages.index, x=sentiment_percentages["Negative"],
        name="Negative", orientation="h", marker_color="#D95C5C",
        hovertemplate="%{y}<br>Negative: %{x:.1f}%<extra></extra>"
    ))

    fig.update_layout(
        barmode="stack",
        height=max(420, len(sentiment_percentages) * 38),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#111111", size=13, family="Mulish"),
        margin=dict(t=20, b=20, l=20, r=20),
        xaxis=dict(
            title="Share of Reviews", range=[0, 100], ticksuffix="%",
            gridcolor="rgba(26,26,26,0.1)", zeroline=False, title_font=dict(color="#111111")
        ),
        yaxis=dict(
            title=None, gridcolor="rgba(0,0,0,0)",
            tickfont=dict(color="#111111", size=13, family="Mulish")
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_color="#111111", font_family="Mulish"),
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})