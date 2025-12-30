import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    SHEET_NAME = os.getenv('SHEET_NAME')
    SHEET_CREDS = os.getenv('GOOGLE_SHEET_CREDS')
