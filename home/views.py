import email
from email import message
from os import name
from django.shortcuts import render, HttpResponse

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from home import models
from .pdf_chat import chat_with_together_ai, extract_text_from_pdf

# API view for chatbot
@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_query = data.get('query', '')

        # Path to the PDF
        pdf_path = "static\files\Bhanu_Bert.pdf"  # Update this with your PDF path

        # Extract text from PDF
        pdf_text = extract_text_from_pdf(pdf_path)
        context = f"The following content is extracted from a PDF:\n\n{pdf_text}\n\nAnswer questions about it."

        # Call the Together.ai API
        response_message = chat_with_together_ai(user_query, context)

        return JsonResponse({"response": response_message})
    return JsonResponse({"error": "Invalid request"}, status=400)



def home(request):
    #contact form database
    # if request.method == 'POST':
    #     name == request.POST['name']
    #     email == request.POST['email']
    #     subject == request.POST['subject']
    #     message == request.POST['message']
    #     contact = models.Home(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    #contact form database
    if request.method == "POST":
        name == request.POST['name']
        email == request.POST['email']
        object == request.POST['subject']
        message == request.POST['message']
        contact = models.Home(name=name, email=email, subject=object, message=message)
        contact.save()
    return render(request, 'home.html')

