## Clustering Module
#This module handles Sentence-BERT embedding generation, UMAP dimensionality reduction, and HDBSCAN semantic clustering for e-commerce reviews.
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import umap
import hdbscan
import joblib
import os

class ReviewClusterer:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """Initialize the embedding model for semantic analysis."""
        self.embedding_model = SentenceTransformer(model_name)
        self.umap_10d = None
        self.umap_2d = None
        self.clusterer = None

    def generate_embeddings(self, texts):
        """Generate high-dimensional semantic embeddings from text list."""
        print("Generating sentence embeddings...")
        return self.embedding_model.encode(texts, show_progress_bar=True)

    def fit_transform_umap(self, embeddings):
        """Reduce embeddings to 10D for clustering and 2D for visualization."""
        print("Applying UMAP dimensionality reduction...")
        self.umap_10d = umap.UMAP(n_neighbors=15, n_components=10, min_dist=0.1, metric='cosine', random_state=42)
        embeddings_10d = self.umap_10d.fit_transform(embeddings)

        self.umap_2d = umap.UMAP(n_neighbors=15, n_components=2, min_dist=0.1, metric='cosine', random_state=42)
        embeddings_2d = self.umap_2d.fit_transform(embeddings)

        return embeddings_10d, embeddings_2d

    def fit_hdbscan(self, embeddings_10d):
        """Apply HDBSCAN density-based clustering."""
        print("Running HDBSCAN clustering...")
        self.clusterer = hdbscan.HDBSCAN(min_cluster_size=15, min_samples=5, metric='euclidean', prediction_data=True)
        return self.clusterer.fit_predict(embeddings_10d)

    def save_artifacts(self, vector_store_dir='../models/vector_store'):
        """Persist fitted UMAP and HDBSCAN models to disk."""
        os.makedirs(vector_store_dir, exist_ok=True)
        joblib.dump(self.umap_10d, os.path.join(vector_store_dir, 'umap_reducer.pkl'))
        joblib.dump(self.clusterer, os.path.join(vector_store_dir, 'hdbscan_clusterer.pkl'))
        print("Clustering artifacts successfully saved!")