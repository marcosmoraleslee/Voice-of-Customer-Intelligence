## LLM Summarization and Prompt Engineering Module
#This module provides structured prompt generators for Large Language Models to analyze review clusters, specific products, and entire product categories[cite: 1].
class LLMReviewAnalyzer:
    def __init__(self):
        """Initialize the LLM analyzer for prompt structuring."""
        pass

    def build_prompt_cluster(self, cluster_data):
        """Generate a comprehensive prompt to analyze a specific review cluster[cite: 1]."""
        prompt = f"""
        Act as an expert e-commerce data analyst. Analyze the following review cluster data and provide:
        1. A summary of the main themes.
        2. Dominant sentiment trends.
        3. Key products involved.
        4. Actionable business insights.

        Cluster Data:
        {cluster_data}
        """
        return prompt.strip()

    def build_prompt_product(self, product_data):
        """Generate a prompt to detail a specific product's strengths, weaknesses, and recommendations[cite: 1]."""
        prompt = f"""
        Act as a product strategy expert. Based on the reviews data for this specific product, detail:
        1. Core strengths.
        2. Weaknesses or recurring complaints.
        3. Ideal user profile.
        4. Actionable recommendations for improvement.

        Product Data:
        {product_data}
        """
        return prompt.strip()

    def build_prompt_category(self, category_data):
        """Generate a prompt to analyze an entire product category[cite: 1]."""
        prompt = f"""
        Act as a retail market analyst. Evaluate the overall performance of this product category, identifying:
        1. Positive and negative thematic drivers.
        2. Top-performing products.
        3. Overall market positioning and customer perception.

        Category Data:
        {category_data}
        """
        return prompt.strip()