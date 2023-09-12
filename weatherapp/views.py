from django.shortcuts import render
import requests
from django.conf import settings

def get_info(request):
    api_key = settings.WEATHER_API_KEY
    city = 'New York'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = request.get(url)
    data = response.json()  

    context = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
    }
    
    return render(request, 'weatherapp/weather.html', context)

# Create your views here.
