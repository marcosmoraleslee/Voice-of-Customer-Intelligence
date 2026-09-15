## Text Preprocessing Module
#This module cleans raw e-commerce review texts by removing HTML tags, URLs, and unwanted noise while preserving critical sentiment punctuation.
import re

class TextPreprocessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        """Clean raw text for sentiment classification and clustering."""
        if not isinstance(text, str):
            return ""
        
        # Remove HTML tags and URLs
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'http\S+', '', text)
        
        # Strip excessive whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text