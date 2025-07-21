import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.getenv('secret_key')

def weather(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+apikey

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'index.html', {'weather_data': weather_data})