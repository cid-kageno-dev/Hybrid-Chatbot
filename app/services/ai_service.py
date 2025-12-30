import google.generativeai as genai
from config import Config

# Configure the library once
genai.configure(api_key=Config.GOOGLE_API_KEY)

def get_gemini_response(prompt):
    """
    Sends the prompt to Google Gemini 1.5 Flash.
    Returns the text response or None if it fails.
    """
    try:
        # 'gemini-2.5-flash' is faster and cheaper for chatbots
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        return response.text.strip()
    except Exception as e:
        print(f"[AI Service Error]: {e}")
        return None
      
