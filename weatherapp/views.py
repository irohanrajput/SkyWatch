from django.shortcuts import render
import requests
from django.conf import settings

def get_info(request):
    api_key = settings.WEATHER_API_KEY
    city = 'delhi, in'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()  
    temp_in_kelvin = data['main']['temp']
    temp_in_celsius = round(temp_in_kelvin -273.15, 3)

    context = {
        'temperature': temp_in_celsius,
        'description': data['weather'][0]['description'],
        'city': city
    }
    
    return render(request, 'index.html', context)

# Create your views here.
