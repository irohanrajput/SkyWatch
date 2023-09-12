from django.shortcuts import render
import requests
from django.conf import settings

def get_info(request):
    api_key = settings.WEATHER_API_KEY
    city = 'India'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()  

    context = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
    }
    
    return render(request, 'index.html', context)

# Create your views here.
