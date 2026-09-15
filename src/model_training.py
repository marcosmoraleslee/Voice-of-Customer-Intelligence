## Model Inference Module
#This module loads the fine-tuned RoBERTa best model from disk to perform real-time sentiment classification on new review texts.
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

class SentimentInference:
    def __init__(self, model_path='../models/fine_tuned_roberta/best_model'):
        """Load the fine-tuned RoBERTa model and tokenizer for inference."""
        print("Loading fine-tuned RoBERTa model for inference...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.model.eval()
        
        # Mapping labels according to business targets
        self.id2label = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

    def predict(self, text):
        """Predict the sentiment of a given review text with explicit type casting."""
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            
            # Explicitly cast to Python int and float to satisfy static type checkers
            pred_class = int(torch.argmax(probs, dim=-1).item())
            confidence = float(probs[0][pred_class].item())
            
        return {
            'sentiment': self.id2label[pred_class],
            'confidence': round(confidence, 4)
        }