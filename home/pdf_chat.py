# import requests
# from PyPDF2 import PdfReader
# from .config import TOGETHER_API_KEY, TOGETHER_AI_MODEL, TOGETHER_AI_URL


# # Constants
# # TOGETHER_API_KEY = "c849a64789c9d5386edbfde68053abb598eca6e37d8b63f3fcb38f743e65dcd2"
# # TOGETHER_AI_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
# # TOGETHER_AI_URL = "https://api.together.xyz/v1/chat/completions"

# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         reader = PdfReader(pdf_path)
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text()
#         return text
#     except Exception as e:
#         raise Exception(f"Error reading PDF: {e}")

# # Chat with Together.ai
# def chat_with_together_ai(prompt, context=None):
#     headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
#     data = {
#         "model": TOGETHER_AI_MODEL,
#         "messages": [
#             {"role": "system", "content": context or "You are a helpful assistant."},
#             {"role": "user", "content": prompt},
#         ],
#     }
#     response = requests.post(TOGETHER_AI_URL, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
#     else:
#         raise Exception(f"API Error: {response.json()}")

# def chat_with_pdf(pdf_path, user_query):
#     pdf_text = extract_text_from_pdf(r"C:\Users\hp\Desktop\PT3\static\files\Bhanu_Bert.pdf")
#     context = f"The following content is extracted from a PDF:\n\n{pdf_text}\n\nAnswer questions about it."
#     response = chat_with_together_ai(user_query, context)
#     return response

import requests
from PyPDF2 import PdfReader
from .config import TOGETHER_API_KEY, TOGETHER_AI_MODEL, TOGETHER_AI_URL

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")

# Chat with Together.ai
def chat_with_together_ai(prompt, context=None):
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}
    data = {
        "model": TOGETHER_AI_MODEL,
        "messages": [
            {"role": "system", "content": context or "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(TOGETHER_AI_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        raise Exception(f"API Error: {response.json()}")
