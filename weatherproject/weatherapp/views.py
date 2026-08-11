from django.shortcuts import render
from django.contrib import messages
import datetime
import requests


def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Lahore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf9a041f15700d7dafd00c9990b23b29'
    PARAMS = {
        'units': 'metric'
    }

    try:
        data = requests.get(url, params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(
            request,
            'weatherapp/index.html',
            {
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'city': city,
                'exception_occurred': False
            }
        )

    except Exception:
        messages.error(
            request,
            'City not found. Please enter a valid city name.'
        )

        day = datetime.date.today()

        return render(
            request,
            'weatherapp/index.html',
            {
                'description': 'clear sky',
                'icon': '01d',
                'temp': 25,
                'day': day,
                'city': city,
                'exception_occurred': True
            }
        )