import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqDocumentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        self.client = Groq(api_key=self.api_key)
        self.model = "mixtral-8x7b-32768" # Fast and capable for text generation

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
Generate a comprehensive legal document titled '{document_type}'
Involved parties: {parties}
Effective Date: {dates}
Terms and conditions: {terms}

Ensure formal legal structure with multiple sections and legal clauses. 
Do not use markdown backticks around the entire output, just output the plain document text.
"""
        
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert legal drafter. Produce a formal, structured legal document based on the user's instructions. Do not include introductory or concluding conversational text. Output only the document content."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
        )
        
        return response.choices[0].message.content
