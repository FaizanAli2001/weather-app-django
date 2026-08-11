from django.shortcuts import render
import datetime
import requests


def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Karachi'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf9a041f15700d7dafd00c9990b23b29'
    PARAMS = {
        'units': 'metric'
    }

    response = requests.get(url, params=PARAMS)

    print("STATUS CODE:", response.status_code)
    print("API RESPONSE:", response.json())

    data = response.json()

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
        }
    )

