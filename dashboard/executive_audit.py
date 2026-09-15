import streamlit as st

from typing import cast


def render_executive_audit(df, product_col, text_col, openai_client):
    """
    Render the Product Deep Dive for the product selected from the
    Customer Feedback Signals rankings.

    The selected product and sentiment are read from Streamlit session state.
    Positive and negative analyses use different business frameworks.
    """

    if df is None or df.empty:
        return

    if "predicted_sentiment" not in df.columns:
        st.warning("Sentiment results are not available.")
        return

    if product_col not in df.columns:
        st.warning("The selected product/category column is not available.")
        return

    if text_col not in df.columns:
        st.warning("The selected review text column is not available.")
        return

    # ------------------------------------------------------------------
    # Read selection created by sentiment_rankings.py
    # ------------------------------------------------------------------

    selected_product = st.session_state.get(
        "selected_deep_dive_product"
    )

    selected_sentiment = st.session_state.get(
        "selected_deep_dive_sentiment"
    )

    # No product has been selected yet.
    if selected_product is None or selected_sentiment is None:
        st.markdown(
            """
            <div class="flat-section">
                <div class="card">
                    <h2>Product Deep Dive</h2>
                    <p style="font-size:0.95rem; color:#C7C9D3;">
                        Select a product from Customer Feedback Signals above
                        to investigate the customer feedback behind it.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    # ------------------------------------------------------------------
    # Validate selected sentiment
    # ------------------------------------------------------------------

    if selected_sentiment not in ["Positive", "Negative"]:
        st.warning("Invalid feedback type selected.")
        return

    # ------------------------------------------------------------------
    # Filter selected product and sentiment
    # ------------------------------------------------------------------

    product_df = df[
        df[product_col].astype(str) == str(selected_product)
    ]

    feedback_df = product_df[
        product_df["predicted_sentiment"] == selected_sentiment
    ]

    feedback_count = len(feedback_df)

    if feedback_count == 0:
        st.warning(
            f"No {selected_sentiment.lower()} reviews are available "
            f"for '{selected_product}'."
        )
        return

    # ------------------------------------------------------------------
    # Define analysis framework
    # ------------------------------------------------------------------

    if selected_sentiment == "Positive":

        section_titles = [
            "Sales & Customer Value",
            "Marketing Opportunities",
            "Promotional Opportunities",
            "Competitive Intelligence",
            "Strategic Recommendations",
        ]

        analysis_instruction = """
Analyze the positive customer feedback to identify the value customers
associate with this product or category.

Focus on:

1. Sales & Customer Value:
   Explain what positive customer perceptions could support commercially.
   Discuss perceived customer value, purchase appeal, and product strengths.
   Do not invent conversion rates, revenue, GMV, or other financial metrics.

2. Marketing Opportunities:
   Identify customer-valued attributes, emotional drivers, benefits,
   or product characteristics that could strengthen marketing communication.

3. Promotional Opportunities:
   Identify messages, product benefits, or customer motivations that could
   be emphasized in promotional campaigns.

4. Competitive Intelligence:
   Identify perceived strengths or differentiators that may matter for
   market positioning. Only infer competitive relevance from the reviews.
   Do not claim facts about competitors that are not present in the data.

5. Strategic Recommendations:
   Provide concise, practical actions the business could consider based
   strictly on the evidence in the reviews.
"""

    else:

        section_titles = [
            "Early Warnings",
            "Product Issues",
            "Operational & Logistics Issues",
            "Customer Experience Risks",
            "Strategic Recommendations",
        ]

        analysis_instruction = """
Analyze the negative customer feedback to identify risks and areas
requiring attention.

Focus on:

1. Early Warnings:
   Identify recurring or particularly concerning negative signals.
   If no date information is available, do not claim that a problem is
   increasing over time or describe it as a temporal spike.

2. Product Issues:
   Identify specific product defects, quality problems, sizing issues,
   material problems, appearance issues, or unmet expectations mentioned
   in the reviews.

3. Operational & Logistics Issues:
   Identify shipping, delivery, packaging, fulfillment, service, or other
   operational problems mentioned in the reviews.

4. Customer Experience Risks:
   Explain how recurring negative experiences could affect customer
   perception, satisfaction, trust, or future purchase consideration.
   Do not invent measurable business impact.

5. Strategic Recommendations:
   Provide concise, practical actions the business could consider based
   strictly on the evidence in the reviews.
"""

    # ------------------------------------------------------------------
    # Build a cache key
    # ------------------------------------------------------------------

    dataset_id = id(df)

    analysis_key = (
        f"{dataset_id}|"
        f"{selected_product}|"
        f"{selected_sentiment}|"
        f"{feedback_count}"
    )

    cached_key = st.session_state.get(
        "deep_dive_analysis_key"
    )

    cached_sections = cast(
        list[str] | None,
        st.session_state.get("deep_dive_analysis_sections")
    )

    # ------------------------------------------------------------------
    # Generate analysis only when the selected product changes
    # ------------------------------------------------------------------

    if cached_key != analysis_key:

        if openai_client is None:
            st.error(
                "OpenAI client is not initialized. "
                "Check your OPENAI_API_KEY."
            )
            return

        # Build review evidence.
        review_lines = []

        for review in feedback_df[text_col].astype(str).tolist():
            review_lines.append(f'- "{review}"')

        reviews_text = "\n".join(review_lines)

        prompt = f"""
You are a senior e-commerce business analyst.

Analyze customer feedback for the following product or category:

Product / Category:
{selected_product}

Feedback type:
{selected_sentiment}

Number of reviews:
{feedback_count}

{analysis_instruction}

IMPORTANT RULES:

- Use only the information contained in the provided reviews.
- Do not invent revenue, GMV, conversion rates, ROI, LTV, market share,
  competitor facts, or other unsupported metrics.
- Clearly distinguish observed customer feedback from business inference.
- Focus on recurring patterns rather than isolated comments.
- Keep the analysis concise and business-oriented.
- Return exactly {len(section_titles)} sections.
- Separate each section with the delimiter "---".
- Do not add introductory text before the first section.
- Do not add a conclusion after the final section.
- Do not repeat the section title at the beginning of each section.
- Do not number the sections.

Customer reviews:
{reviews_text}
"""

        with st.spinner(
            f"Analyzing {selected_sentiment.lower()} feedback "
            f"for '{selected_product}'..."
        ):
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a precise senior business analyst. "
                                "Base every conclusion on the provided evidence."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0.2,
                    max_tokens=1600,
                )

                content = response.choices[0].message.content or ""

                sections = [
                    section.strip()
                    for section in content.split("---")
                    if section.strip()
                ]

            except Exception as err:
                st.error(
                    f"Unable to generate the product analysis: {err}"
                )
                return

        # Ensure the expected number of sections.
        while len(sections) < len(section_titles):
            sections.append(
                "No additional evidence was identified."
            )

        sections = sections[:len(section_titles)]

        # Store the result so another Streamlit rerun does not
        # generate the same LLM request again.
        st.session_state.deep_dive_analysis_key = analysis_key
        st.session_state.deep_dive_analysis_sections = sections

    else:
        sections = cached_sections

    if sections is None:
        return

    # ------------------------------------------------------------------
    # Product Deep Dive header
    # ------------------------------------------------------------------

    sentiment_label = (
        "POSITIVE FEEDBACK"
        if selected_sentiment == "Positive"
        else "NEGATIVE FEEDBACK"
    )

    st.markdown(
        """
        <div style="margin-top:1.5rem; margin-bottom:1.5rem;">
            <h2 style="margin-bottom:0.25rem;">
                Product Deep Dive
            </h2>
            <p style="
                font-size:0.95rem;
                color:#9FA4AE;
                margin-top:0;
            ">
                Investigate the customer feedback behind a selected
                product and identify where the business should act.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # Selected product context
    # ------------------------------------------------------------------

    st.markdown(
        f"**● {sentiment_label}**"
    )

    st.markdown(
        f"### {selected_product}"
    )

    st.caption(
        f"Analysis based on {feedback_count:,} "
        f"{selected_sentiment.lower()} reviews."
    )

    # ------------------------------------------------------------------
    # Analysis introduction
    # ------------------------------------------------------------------

    if selected_sentiment == "Positive":
        analysis_heading = "What customers value about this product"
    else:
        analysis_heading = "What customers are telling us about this product"

    st.markdown(
        f"""
        <div style="
            margin-top:1.75rem;
            margin-bottom:1rem;
        ">
            <h3 style="margin-bottom:0.25rem;">
                {analysis_heading}
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # Render the first four analysis sections in two columns
    # ------------------------------------------------------------------

    left_column, right_column = st.columns(2)

    analysis_columns = [
        left_column,
        right_column,
        left_column,
        right_column,
    ]

    for index in range(4):

        title = section_titles[index]
        section = sections[index]

        with analysis_columns[index]:

            st.markdown(
                f"""
                <div class="card">
                    <h4 style="
                        margin-top:0;
                        margin-bottom:0.85rem;
                    ">
                        {title}
                    </h4>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(section)

    # ------------------------------------------------------------------
    # Strategic recommendations
    # ------------------------------------------------------------------

    strategic_title = section_titles[4]
    strategic_section = sections[4]

    st.markdown(
        f"""
        <div class="card" style="margin-top:1rem;">
            <h3 style="
                margin-top:0;
                margin-bottom:0;
            ">
                {strategic_title}
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(strategic_section)