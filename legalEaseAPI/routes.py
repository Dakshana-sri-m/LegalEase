from fastapi import APIRouter
from pydantic import BaseModel
import sys
import os

# Add parent directory to path so ai_core can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_core.groq_generator import GroqDocumentGenerator

router = APIRouter()

try:
    groq_generator = GroqDocumentGenerator()
except Exception as e:
    print(f"Warning: {e}")
    groq_generator = None

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    if not groq_generator:
        # Re-try initialization in case .env was updated
        try:
            global groq_generator_instance 
            groq_generator_instance = GroqDocumentGenerator()
        except Exception as e:
            return {"error": f"Groq API is not configured properly: {e}"}
    else:
        groq_generator_instance = groq_generator
        
    try:
        response = groq_generator_instance.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )
        return {"document": response}
    except Exception as e:
        return {"error": str(e)}
