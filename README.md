# Portfolio Website Chatbot Integration with Together API

This README provides instructions and details for setting up and running a chatbot on a portfolio website using the Together API.

---

## Features
- Frontend chatbot interface using HTML and JavaScript.
- Backend integration with Django for handling chatbot communication.
- Together API utilized for generating chatbot responses.

---

## Prerequisites

### Software Requirements
- Python (>= 3.8)
- Django (>= 3.2)
- Together API access (API key required)
- A web browser (Chrome, Firefox, etc.)

### Environment Setup
- Ensure Python and Django are installed.
- Use a virtual environment to isolate dependencies.

---

## Project Structure

```
![image](https://github.com/user-attachments/assets/ed5467c2-f925-45e1-bbd2-8eb2ec0994a1)



```
![image](https://github.com/user-attachments/assets/f31b6229-edc1-489a-a932-d4247782e3d1)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django requests
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Collect static files (if in production):
   ```bash
   python manage.py collectstatic
   ```

---

## Frontend Setup

The chatbot frontend is located in `templates/chatbot/chatbot.html`. It uses a simple JavaScript-based UI for user interaction.

### Key Files
- **HTML**: `templates/chatbot/chatbot.html`
- **CSS/JS**: Static files in `static/`

---

## Backend Setup

The backend logic is implemented in Django views. Communication is established via an AJAX POST request.

### Key Files
- **Views**: `chatbot/views.py`
- **URLs**: `chatbot/urls.py`
- **Main URLs**: `project/urls.py`

### Together API Integration

Add your Together API key in `settings.py`:
```python
TOGETHER_API_KEY = "your_api_key_here"
```

Update the chatbot view in `views.py` to use the Together API:

```python
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Together API call
        api_url = "https://api.together.xyz/chat"
        headers = {"Authorization": f"Bearer {settings.TOGETHER_API_KEY}"}
        payload = {"input": user_message}

        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            bot_response = response.json().get('output', 'Sorry, I didn\'t understand that.')
        else:
            bot_response = "Error: Unable to fetch response from Together API."

        return JsonResponse({'response': bot_response})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
```

---

## URLs: Add Endpoint
In your `urls.py`, add a route for the chatbot view.

#### `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
]
```

In `project/urls.py`, include the app's URLs:

```python
from django.urls import include, path

urlpatterns = [
    path('', include('chatbot.urls')),
]
```

---

## Running the Project

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/chatbot/
   ```

3. Interact with the chatbot and verify functionality.

---

## Debugging

### Common Issues
1. **CSRF Token Missing**:
   Ensure `{% csrf_token %}` is included in the HTML template and passed in the AJAX request.

2. **404 Not Found**:
   Verify the `/chatbot/` endpoint is correctly defined in `urls.py`.

3. **JavaScript Errors**:
   Open browser developer tools (F12) to check for console errors.

4. **Static Files Not Loading**:
   Ensure `collectstatic` is run if in production mode.

5. **Together API Errors**:
   Check API key validity and API endpoint availability.

### Logs
- Check the Django development server logs for backend errors.
- Use browser developer tools for frontend debugging.

---

## Customization

1. Modify **chatbot response logic** in `views.py` to implement custom behavior:
   ```python
   bot_response = response.json().get('output', 'Sorry, I didn\'t understand that.')
   ```

2. Update **CSS styles** in `static/css/chatbot.css` to customize the chatbot appearance.

3. Enhance the **JavaScript logic** in `static/js/chatbot.js` for advanced features.

---

## Deployment

1. Configure your production environment.
2. Set `DEBUG = True` in `settings.py`.
3. Use a WSGI/ASGI server like Gunicorn or Daphne.

---


---

## Contact
For issues or suggestions, feel free to reach out via bhanups292004@gmail.com.

