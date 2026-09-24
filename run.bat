@echo off
echo ==============================================
echo LegalEase - AI Legal Document Generator
echo ==============================================
echo.

echo Installing required packages (if not already installed)...
python -m pip install -r requirements.txt

echo.
echo Starting LegalEase Backend (FastAPI on Port 8000)...
start "LegalEase Backend" cmd /k "python -m uvicorn legalEaseAPI.main:app --reload"

echo Starting LegalEase Frontend (Streamlit on Port 8501)...
start "LegalEase Frontend" cmd /k "python -m streamlit run frontend/app.py"

echo.
echo Setup Complete! 
echo Frontend should open in your browser automatically at http://localhost:8501
echo To stop the servers, close the command prompt windows that opened.
pause
